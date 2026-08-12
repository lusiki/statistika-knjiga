#!/usr/bin/env node
// Numeric adapters for the claims made by the seventeen OJS widgets.
// The adapters intentionally omit layout, colours, labels, and point coordinates.

import fs from "node:fs";
import path from "node:path";

const root = path.resolve(process.argv[2] ?? ".");
const fixture = process.argv[3] ?? "";
const registry = JSON.parse(
  fs.readFileSync(path.join(root, "data", "widgets.json"), "utf8")
);

function lcg(seed) {
  const epsilon = 1 / 4294967296;
  let state = ((seed >= 0 && seed < 1 ? seed / epsilon : Math.abs(seed)) | 0);
  return () => {
    state = (1664525 * state + 1013904223) | 0;
    return epsilon * (state >>> 0);
  };
}

function normal(source, meanValue = 0, sdValue = 1) {
  return () => {
    let x;
    let y;
    let radius;
    do {
      x = source() * 2 - 1;
      y = source() * 2 - 1;
      radius = x * x + y * y;
    } while (!radius || radius > 1);
    return meanValue + sdValue * x * Math.sqrt(-2 * Math.log(radius) / radius);
  };
}

// Fixture-only variant. It deliberately consumes the cached second polar
// variate so the negative gate proves that the live w09 stream and its adapter
// cannot drift to different normal-generator semantics unnoticed.
function normalCached(source, meanValue = 0, sdValue = 1) {
  let cached = null;
  return () => {
    if (cached !== null) {
      const value = cached;
      cached = null;
      return meanValue + sdValue * value;
    }
    let x;
    let y;
    let radius;
    do {
      x = source() * 2 - 1;
      y = source() * 2 - 1;
      radius = x * x + y * y;
    } while (!radius || radius > 1);
    const scale = Math.sqrt(-2 * Math.log(radius) / radius);
    cached = y * scale;
    return meanValue + sdValue * x * scale;
  };
}

const sum = values => values.reduce((total, value) => total + value, 0);
const mean = values => sum(values) / values.length;

function sampleSd(values) {
  const center = mean(values);
  return Math.sqrt(sum(values.map(value => (value - center) ** 2)) / (values.length - 1));
}

function quantile(values, probability) {
  const sorted = [...values].sort((a, b) => a - b);
  const index = (sorted.length - 1) * probability;
  const lower = Math.floor(index);
  const fraction = index - lower;
  return sorted[lower] + fraction * (sorted[Math.min(lower + 1, sorted.length - 1)] - sorted[lower]);
}

function correlation(x, y) {
  const mx = mean(x);
  const my = mean(y);
  const numerator = sum(x.map((value, index) => (value - mx) * (y[index] - my)));
  const denominator = Math.sqrt(
    sum(x.map(value => (value - mx) ** 2)) *
    sum(y.map(value => (value - my) ** 2))
  );
  return numerator / denominator;
}

function regression(x, y) {
  const mx = mean(x);
  const my = mean(y);
  const slope = sum(x.map((value, index) => (value - mx) * (y[index] - my))) /
    sum(x.map(value => (value - mx) ** 2));
  return {intercept: my - slope * mx, slope};
}

function skewness(values) {
  const center = mean(values);
  const second = mean(values.map(value => (value - center) ** 2));
  const third = mean(values.map(value => (value - center) ** 3));
  return third / second ** 1.5;
}

function erf(x) {
  const sign = x < 0 ? -1 : 1;
  const z = Math.abs(x);
  const t = 1 / (1 + 0.3275911 * z);
  const y = 1 - (((((1.061405429 * t - 1.453152027) * t) +
    1.421413741) * t - 0.284496736) * t + 0.254829592) *
    t * Math.exp(-z * z);
  return sign * y;
}

const normalCdf = x => 0.5 * (1 + erf(x / Math.SQRT2));

function normalQuantile(probability) {
  let lower = -8;
  let upper = 8;
  for (let i = 0; i < 60; i += 1) {
    const middle = (lower + upper) / 2;
    if (normalCdf(middle) < probability) lower = middle;
    else upper = middle;
  }
  return (lower + upper) / 2;
}

function flatten(prefix, values, output = {}) {
  for (const [key, value] of Object.entries(values)) {
    const next = prefix ? `${prefix}.${key}` : key;
    if (value && typeof value === "object" && !Array.isArray(value)) {
      flatten(next, value, output);
    } else {
      output[next] = value;
    }
  }
  return output;
}

function w01(parameters) {
  const p = parameters.scenarios[0];
  return flatten("default", {
    aggregate_a: p.share_a_easy * 0.8 + (1 - p.share_a_easy) * 0.2,
    aggregate_b: p.share_b_easy * 0.9 + (1 - p.share_b_easy) * 0.3,
    easy_a: 0.8,
    easy_b: 0.9,
    hard_a: 0.2,
    hard_b: 0.3
  });
}

function w02(parameters) {
  const p = parameters.scenarios[0];
  const rows = Array.from({length: 32}, (_, i) => {
    const high = i >= 16;
    const row = i % 16;
    const u = (row - 7.5) / 7.5;
    const exposure = (high ? 6.6 : 2.8) + 1.6 * u;
    const noise = 0.28 * Math.sin((row + 1) * 2.3) + 0.10 * Math.cos((row + 1) * 1.1);
    return {high, exposure, outcome: 7.2 - 0.55 * exposure + (high ? p.shift : 0) + noise};
  });
  const slope = subset => regression(subset.map(d => d.exposure), subset.map(d => d.outcome)).slope;
  return flatten("default", {
    pooled_slope: slope(rows),
    low_slope: slope(rows.filter(d => !d.high)),
    high_slope: slope(rows.filter(d => d.high))
  });
}

function w03(parameters) {
  const result = {};
  for (const p of parameters.scenarios) {
    const estimate = p.share;
    const margin = 1.96 * Math.sqrt(estimate * (1 - estimate) / p.n);
    result[`${p.id}.estimate`] = estimate;
    result[`${p.id}.truth`] = estimate - p.bias;
    result[`${p.id}.margin`] = margin;
    result[`${p.id}.lower`] = Math.max(0, estimate - margin);
    result[`${p.id}.upper`] = Math.min(1, estimate + margin);
  }
  return result;
}

function w04(parameters) {
  const deviations = [-3, -2, -1, -1, 0, 1, 1, 2, 3];
  const result = {};
  for (const p of parameters.scenarios) {
    const values = [...deviations.map(value => 11 + value * p.spread), p.extreme].sort((a, b) => a - b);
    result[`${p.id}.mean`] = mean(values);
    result[`${p.id}.median`] = quantile(values, 0.5);
    result[`${p.id}.sd`] = sampleSd(values);
    result[`${p.id}.iqr`] = quantile(values, 0.75) - quantile(values, 0.25);
  }
  return result;
}

function w05(parameters) {
  const p = parameters.scenarios[0];
  const rng = lcg(p.seed);
  const randomNormal = normal(rng, 0, p.noise_sd);
  const rows = Array.from({length: p.n}, (_, i) => {
    const group = i < p.n / 2 ? "a" : "b";
    const x = 1 + (i % (p.n / 2)) * 9 / (p.n / 2 - 1);
    const y = 1.5 + 0.55 * x + (group === "b" ? p.group_shift : 0) + randomNormal();
    return {group, x, y};
  });
  const a = rows.filter(d => d.group === "a").map(d => d.y);
  const b = rows.filter(d => d.group === "b").map(d => d.y);
  return flatten("default", {
    overall_mean: mean(rows.map(d => d.y)),
    overall_sd: sampleSd(rows.map(d => d.y)),
    group_a_mean: mean(a),
    group_b_mean: mean(b),
    group_difference: mean(b) - mean(a),
    slope: regression(rows.map(d => d.x), rows.map(d => d.y)).slope
  });
}

function w06(parameters) {
  const result = {};
  parameters.scenarios.forEach((p, index) => {
    const rng = lcg(p.seed);
    const randomNormal = normal(rng);
    const x = [];
    const y = [];
    for (let i = 0; i < p.n; i += 1) {
      const xv = randomNormal();
      const z = randomNormal();
      x.push(xv);
      y.push(p.rho * xv + Math.sqrt(1 - p.rho ** 2) * z);
    }
    result[`cloud_${index + 1}.correlation`] = correlation(x, y);
  });
  return result;
}

function w07(parameters) {
  const result = {};
  for (const p of parameters.scenarios) {
    const rng = lcg(p.seed);
    const rates = Array.from({length: p.repetitions}, () => {
      let successes = 0;
      for (let i = 0; i < p.n; i += 1) if (rng() < p.probability) successes += 1;
      return successes / p.n;
    });
    result[`${p.id}.mean`] = mean(rates);
    result[`${p.id}.sd`] = sampleSd(rates);
    result[`${p.id}.q05`] = quantile(rates, 0.05);
    result[`${p.id}.q95`] = quantile(rates, 0.95);
  }
  result.width_ratio = result[`${parameters.scenarios[0].id}.sd`] / result[`${parameters.scenarios[1].id}.sd`];
  return result;
}

function w08(parameters) {
  const result = {};
  for (const p of parameters.scenarios) {
    const rng = lcg(p.seed);
    const draw = () => -Math.log(1 - rng()) - 1;
    const population = Array.from({length: p.population_n}, draw);
    const sampleMeans = Array.from({length: p.repetitions}, () => {
      let total = 0;
      for (let i = 0; i < p.n; i += 1) total += draw();
      return total / p.n;
    });
    result[`${p.id}.se_ratio`] = sampleSd(sampleMeans) / sampleSd(population);
    result[`${p.id}.mean_skewness`] = skewness(sampleMeans);
    result[`${p.id}.center_offset_sd`] = (mean(sampleMeans) - mean(population)) / sampleSd(population);
  }
  result.skew_reduction = Math.abs(result[`${parameters.scenarios[0].id}.mean_skewness`]) -
    Math.abs(result[`${parameters.scenarios[1].id}.mean_skewness`]);
  return result;
}

function w09(parameters) {
  const p = parameters.scenarios[0];
  const rng = lcg(p.seed);
  const randomNormal = fixture === "w09-cached-normal" ? normalCached(rng) : normal(rng);
  const estimates = [];
  let covered = 0;
  const margin = p.critical / Math.sqrt(p.n);
  for (let i = 0; i < p.intervals; i += 1) {
    let total = 0;
    for (let j = 0; j < p.n; j += 1) total += randomNormal();
    const estimate = total / p.n;
    estimates.push(estimate);
    if (estimate - margin <= 0 && estimate + margin >= 0) covered += 1;
  }
  return flatten("default", {
    coverage_rate: covered / p.intervals,
    mean_width: 2 * margin,
    mean_estimate: mean(estimates)
  });
}

function w10(parameters) {
  const p = parameters.scenarios[0];
  const rng = lcg(p.seed);
  const randomNormal = normal(rng);
  const shift = p.effect * Math.sqrt(p.n / 2);
  const simulate = center => Array.from({length: p.repetitions}, () => {
    const z = center + randomNormal();
    return 2 * (1 - normalCdf(Math.abs(z)));
  });
  const nullP = simulate(0);
  const effectP = simulate(shift);
  return flatten("default", {
    null_rejection_rate: mean(nullP.map(value => value <= p.threshold ? 1 : 0)),
    effect_rejection_rate: mean(effectP.map(value => value <= p.threshold ? 1 : 0)),
    null_p_mean: mean(nullP),
    effect_p_mean: mean(effectP)
  });
}

function w11(parameters) {
  const result = {};
  for (const effect of parameters.effects) {
    const rng = lcg(parameters.seed);
    const randomNormal = normal(rng);
    const critical = normalQuantile(1 - parameters.threshold / 2);
    const powers = [];
    for (let n = 10; n <= 300; n += 10) {
      const center = effect * Math.sqrt(n / 2);
      let rejections = 0;
      for (let i = 0; i < parameters.repetitions; i += 1) {
        if (Math.abs(center + randomNormal()) >= critical) rejections += 1;
      }
      powers.push({n, power: rejections / parameters.repetitions});
    }
    for (const n of parameters.report_n) {
      result[`d${effect}.n${n}.power`] = powers.find(row => row.n === n).power;
    }
    result[`d${effect}.first_n_80`] = powers.find(row => row.n >= 20 && row.power >= 0.8)?.n ?? null;
  }
  return result;
}

function w12(parameters) {
  const result = {};
  for (const paths of parameters.paths) {
    const rng = lcg(parameters.seed);
    const minima = Array.from({length: parameters.repetitions}, () => {
      let minimum = 1;
      for (let i = 0; i < paths; i += 1) minimum = Math.min(minimum, rng());
      return minimum;
    });
    result[`paths${paths}.nominal_rate`] = mean(minima.map(value => value <= 0.05 ? 1 : 0));
    result[`paths${paths}.corrected_rate`] = mean(minima.map(value => value <= 0.05 / paths ? 1 : 0));
    result[`paths${paths}.cdf_001`] = mean(minima.map(value => value <= 0.01 ? 1 : 0));
  }
  return result;
}

function w13(parameters) {
  const result = {};
  for (const p of parameters.scenarios) {
    const expected = p.n / 2;
    const shift = Math.round(expected * p.shift_percent / 100);
    const contribution = shift ** 2 / expected;
    const chi_square = 4 * contribution;
    result[`${p.id}.expected`] = expected;
    result[`${p.id}.shift`] = shift;
    result[`${p.id}.cell_contribution`] = contribution;
    result[`${p.id}.chi_square`] = chi_square;
    result[`${p.id}.cramers_v`] = Math.sqrt(chi_square / (2 * p.n));
  }
  return result;
}

function w14(parameters) {
  const result = {};
  for (const p of parameters.scenarios) {
    const rng = lcg(parameters.seed);
    const randomNormal = normal(rng);
    const paired = p.design === "paired";
    if (paired) {
      for (let i = 0; i < p.n; i += 1) {
        const z1 = randomNormal();
        const z2 = randomNormal();
        void (p.sd * z1 + p.difference + p.sd * (parameters.correlation * z1 + Math.sqrt(1 - parameters.correlation ** 2) * z2));
      }
    } else {
      for (let i = 0; i < 2 * p.n; i += 1) randomNormal();
    }
    const standardError = paired
      ? p.sd * Math.sqrt(2 * (1 - parameters.correlation) / p.n)
      : p.sd * Math.sqrt(2 / p.n);
    const estimates = Array.from({length: parameters.ojs_repetitions}, () => p.difference + standardError * randomNormal());
    result[`${p.id}.theoretical_se`] = standardError;
    result[`${p.id}.estimate_mean`] = mean(estimates);
    result[`${p.id}.estimate_sd`] = sampleSd(estimates);
  }
  result.se_ratio = result["paired.theoretical_se"] / result["independent.theoretical_se"];
  return result;
}

function w15(parameters) {
  const result = {};
  const n = parameters.n_per_group;
  for (const p of parameters.scenarios) {
    const grand = mean(p.means);
    const ssBetween = n * sum(p.means.map(value => (value - grand) ** 2));
    const msBetween = ssBetween / (p.means.length - 1);
    const msWithin = p.sd ** 2;
    result[`${p.id}.grand_mean`] = grand;
    result[`${p.id}.ms_between`] = msBetween;
    result[`${p.id}.ms_within`] = msWithin;
    result[`${p.id}.f_ratio`] = msBetween / msWithin;
  }
  return result;
}

function w16(parameters) {
  const p = parameters.scenarios[0];
  const rng = lcg(p.seed);
  const randomNormal = normal(rng);
  const rows = Array.from({length: p.n}, () => {
    const interest = randomNormal();
    const time = Math.max(0, 5 + 1.8 * interest + 1.5 * randomNormal());
    const engagement = 20 + 2.3 * time + 7 * interest + 4.5 * randomNormal();
    return {interest, time, engagement};
  });
  const x = rows.map(d => d.time);
  const y = rows.map(d => d.engagement);
  const z = rows.map(d => d.interest);
  const aggregate = regression(x, y);
  const xOnZ = regression(z, x);
  const yOnZ = regression(z, y);
  const xResidual = x.map((value, i) => value - xOnZ.intercept - xOnZ.slope * z[i]);
  const yResidual = y.map((value, i) => value - yOnZ.intercept - yOnZ.slope * z[i]);
  const adjustedSlope = sum(xResidual.map((value, i) => value * yResidual[i])) /
    sum(xResidual.map(value => value ** 2));
  const sseMinimum = sum(rows.map(d => (d.engagement - aggregate.intercept - aggregate.slope * d.time) ** 2));
  const userSse = sum(rows.map(d => (d.engagement - p.user_intercept - p.user_slope * d.time) ** 2));
  return flatten("default", {
    aggregate_intercept: aggregate.intercept,
    aggregate_slope: aggregate.slope,
    adjusted_slope: adjustedSlope,
    sse_minimum: sseMinimum,
    user_sse: userSse,
    user_to_minimum_ratio: userSse / sseMinimum
  });
}

function w17(parameters) {
  const p = parameters.scenarios[0];
  const rng = lcg(p.seed);
  const randomNormal = normal(rng);
  const clamp = value => Math.max(0, Math.min(1, value));
  const negative = Array.from({length: p.n_per_class}, () => clamp(0.30 + 0.18 * randomNormal()));
  const positive = Array.from({length: p.n_per_class}, () => clamp(0.70 + 0.18 * randomNormal()));
  const fpr = mean(negative.map(value => value >= p.threshold ? 1 : 0));
  const fnr = mean(positive.map(value => value < p.threshold ? 1 : 0));
  const tpr = 1 - fnr;
  const tnr = 1 - fpr;
  const group = baseRate => ({
    ppv: baseRate * tpr / (baseRate * tpr + (1 - baseRate) * fpr),
    accuracy: baseRate * tpr + (1 - baseRate) * tnr
  });
  return flatten("default", {
    fpr,
    fnr,
    group_a: group(p.base_rate_a),
    group_b: group(p.base_rate_b)
  });
}

const adapters = {w01, w02, w03, w04, w05, w06, w07, w08, w09, w10, w11, w12, w13, w14, w15, w16, w17};
const results = {};
for (const widget of registry.widgets) {
  if (!widget.parity) throw new Error(`${widget.id}: missing parity record`);
  results[widget.id] = adapters[widget.id](widget.parity.parameters);
}

process.stdout.write(`${JSON.stringify({schema_version: 1, adapter: "ojs", results}, null, 2)}\n`);
