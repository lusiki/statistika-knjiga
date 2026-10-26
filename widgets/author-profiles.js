(() => {
 const root=document.querySelector('.author-profile');if(!root)return;
 const button=root.querySelector('.composition-button');button.hidden=false;
 button.addEventListener('click',()=>{const active=root.classList.toggle('alternate');button.setAttribute('aria-pressed',String(active));});
})();
