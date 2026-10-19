const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#primary-nav');
if (toggle && nav) {
  const close = () => {nav.classList.remove('open'); toggle.setAttribute('aria-expanded','false'); toggle.textContent='Menu';};
  toggle.addEventListener('click', () => {const open = toggle.getAttribute('aria-expanded') !== 'true'; nav.classList.toggle('open',open); toggle.setAttribute('aria-expanded',String(open)); toggle.textContent=open?'Close':'Menu';});
  nav.querySelectorAll('a').forEach(link=>link.addEventListener('click',close));
  document.addEventListener('keydown',event=>{if(event.key==='Escape' && nav.classList.contains('open')){close();toggle.focus();}});
  window.matchMedia('(min-width:701px)').addEventListener('change',close);
}
