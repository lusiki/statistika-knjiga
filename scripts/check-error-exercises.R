# Independent numerical checks for the 2026-10-21 exercise revision.
# No chapter code or solution record is evaluated.
source("R/podaci-nastavni.R", encoding = "UTF-8")
read_data <- function(path) read.csv(path, fileEncoding = "UTF-8", check.names = FALSE)
near <- function(actual, expected, tolerance = 1e-6) {
  stopifnot(length(actual) == length(expected), all(abs(actual - expected) < tolerance))
}
near(c(15101, 13378, 10827, 5839, 4855) |> sum(), 50000)
near(c(15101/50000*100, 3514/15101*100, 1289/4855*100),
     c(30.202, 23.2699821203894, 26.5499485066941))
stopifnot(2154733 + 60476 == 2215209, 2216763 - 2215209 == 1554)
near(1554/2216763*100, .07010221)

m <- read_data("data/digikat-platforme-mjesecno.csv")
y <- read_data("data/digikat-platforme-godisnje.csv")
bad <- merge(m, y, by = "godina", all.x = TRUE)
good <- merge(m, y, by = c("godina", "platforma"), all.x = TRUE)
stopifnot(nrow(m) == 438, nrow(bad) == 3571, nrow(good) == 438)
stopifnot(sum(m$objave) == 710307, sum(bad$objave.x) == 5959081,
          sum(good$objave.x) == 710307)
near(.9/.6, 1.5)

a <- read_data("data/anketa-mreze.csv")
young <- a[a$dob >= 18 & a$dob <= 24, ]
stopifnot(nrow(a) == 300, nrow(young) == 90)
near(round(c(cor(a$dob,a$minute_dnevno), cor(young$dob,young$minute_dnevno)),2), c(-.56,.18))
near(1-.98^5, .0960792032, 1e-12)
near(20/sqrt(c(25,100)), c(4,2))

set.seed(505)
small <- populacija_medija[sample.int(nrow(populacija_medija),60), ]
ix <- replicate(4000,sample.int(60,replace=TRUE))
med <- apply(ix,2,function(i) median(small$minute_medija[i]))
near(c(median(small$minute_medija), quantile(med,c(.025,.975))),c(173.5,155,194))

set.seed(1011)
eligible <- populacija_medija[populacija_medija$izvor_vijesti %in% c("portal","tisak"), ]
u <- eligible[sample.int(nrow(eligible),300), ]
g <- as.character(u$izvor_vijesti); z <- u$povjerenje_medijima
diffmean <- function(labels) mean(z[labels=="tisak"])-mean(z[labels=="portal"])
d <- diffmean(g)
null <- replicate(4000,diffmean(sample(g)))
b <- sum(abs(null)>=abs(d))
stopifnot(b == 64)
se <- sqrt(var(z[g=="tisak"])/sum(g=="tisak") + var(z[g=="portal"])/sum(g=="portal"))
near(c(d,d-1.96*se,d+1.96*se),c(.6409389898,.1748111931,1.1070667865))
near((b+1)/4001,.0162459385154)
near(power.t.test(n=30,delta=.78,sd=1,sig.level=.05,type="two.sample")$power,.8438926)
stopifnot(ceiling(power.t.test(delta=.5/1.9,sd=1,power=.8,type="two.sample")$n)==228)

set.seed(1313)
u <- populacija_medija[sample.int(nrow(populacija_medija),800), ]
age <- cut(u$dob,c(17,29,44,59,Inf),labels=c("18-29","30-44","45-59","60+"))
tab <- table(age,u$izvor_vijesti)
expected <- outer(rowSums(tab),colSums(tab))/sum(tab)
chi <- sum((tab-expected)^2/expected)
v <- sqrt(chi/(sum(tab)*(min(dim(tab))-1)))
near(min(expected),14.34375)
near(round(chi,1),149.8); near(round(v,2),.25)
stopifnot(prod(dim(tab)-1)==12, pchisq(chi,12,lower.tail=FALSE)<.001)
tv <- 100*tab[c(1,4),"TV"]/rowSums(tab)[c(1,4)]
social <- 100*tab[c(1,4),2]/rowSums(tab)[c(1,4)]
near(round(c(tv,social),1),c(12.2,45.2,42.1,2.2))

set.seed(1414)
eligible <- populacija_medija[populacija_medija$izvor_vijesti %in% c("TV",levels(populacija_medija$izvor_vijesti)[2]), ]
u <- eligible[sample.int(nrow(eligible),120), ]
u <- u[u$dob>=30 & u$dob<=49, ]
tv <- u$povjerenje_medijima[u$izvor_vijesti=="TV"]
social <- u$povjerenje_medijima[u$izvor_vijesti!= "TV"]
stopifnot(nrow(u)==55)
d <- mean(tv)-mean(social)
w1 <- var(tv)/length(tv); w2 <- var(social)/length(social)
df <- (w1+w2)^2/(w1^2/(length(tv)-1)+w2^2/(length(social)-1))
ci <- d+c(-1,1)*qt(.975,df)*sqrt(w1+w2)
near(c(d,ci), c(.770270270270,-.335616307975,1.876156848515))
stopifnot(choose(5,2)==10)

u <- populacija_medija[1:200, ]
X <- model.matrix(~ dob+izvor_vijesti+obrazovanje+minute_medija+spol,u)
z <- u$povjerenje_medijima
beta <- qr.solve(X,z); errors <- z-drop(X%*%beta)
rmse <- sqrt(sum(errors^2)/nrow(u)); r2 <- 1-sum(errors^2)/sum((z-mean(z))^2)
stopifnot(rmse < 2, r2>=0, r2<=1)
cat(sprintf("EXERCISE_NUMERICS_OK units=00,01,03,04,05,06,07,08,09,10,11,13,14,15,16\n"))
cat(sprintf("unit13 chi=%.9f V=%.9f; unit16 n=200 R2=%.9f RMSE=%.9f\n",chi,v,r2,rmse))
