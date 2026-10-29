const menu=document.querySelector('.menu'),nav=document.querySelector('#navigation');
menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Chiudi menu':'Apri menu');nav.classList.toggle('open',open)});
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Apri menu')}));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Apri menu');menu.focus()}});
const topics={cute:{title:'Leggerezza, dalla radice.',copy:'Cute che si appesantisce e punte secche possono avere esigenze diverse. Parliamone insieme, per scegliere una cura mirata.',message:'la cute che si appesantisce'},lengths:{title:'Attenzione, fino alle punte.',copy:'Lunghezze secche, spente o difficili da gestire? Iniziamo dalle tue abitudini e dall’osservazione del capello, per individuare il percorso adatto.',message:'le lunghezze secche o spente'},season:{title:'Ogni stagione, una nuova cura.',copy:'Dopo l’estate o durante il cambio di stagione, potresti notare esigenze diverse. Raccontami cosa è cambiato e approfondiamolo in consulenza.',message:'la cura dei capelli al cambio di stagione'},routine:{title:'La cura comincia anche a casa.',copy:'Prodotti, lavaggi e piccoli gesti quotidiani: rivediamo insieme la tua routine per costruire attenzioni coerenti con le esigenze di cute e lunghezze.',message:'la mia routine di cura dei capelli'}};
document.querySelectorAll('.choice').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('.choice').forEach(b=>{b.classList.remove('selected');b.setAttribute('aria-pressed','false')});button.classList.add('selected');button.setAttribute('aria-pressed','true');const t=topics[button.dataset.topic];document.querySelector('#topic-title').textContent=t.title;document.querySelector('#topic-copy').textContent=t.copy;document.querySelector('#topic-link').href='https://wa.me/393294664438?text='+encodeURIComponent('Ciao Vita, vorrei richiedere una consulenza per '+t.message+'. Possiamo concordare un appuntamento?')}));
document.querySelectorAll('[data-wa]').forEach(a=>a.href='https://wa.me/393294664438?text='+encodeURIComponent('Ciao Vita, vorrei informazioni sulla consulenza personalizzata per cute e capelli. Possiamo concordare un appuntamento?'));
document.querySelector('#year').textContent=new Date().getFullYear();
// Scorrimento naturale: nessun controllo artificiale della posizione della pagina.
const motionPreference=matchMedia('(prefers-reduced-motion: reduce)');
const progress=document.createElement('div');progress.className='reading-progress';progress.setAttribute('aria-hidden','true');progress.innerHTML='<span></span>';document.body.append(progress);
const scrollStatus=document.createElement('div');scrollStatus.className='scroll-status';scrollStatus.innerHTML='<span aria-hidden="true">01</span><p></p><a href="#approfondimenti" aria-label="Torna all’indice degli argomenti">↑</a>';document.body.append(scrollStatus);
const chapterLinks=Array.from(document.querySelectorAll('.topic-nav a'));
const chapters=chapterLinks.map(a=>document.getElementById(a.hash.slice(1))).filter(Boolean);
const animatedPhotos=new Set();let scrollFrame=0;
document.querySelectorAll('.topic-body').forEach(body=>{body.classList.remove('reveal');body.querySelectorAll(':scope > h2,:scope > p,:scope > .conversation-note,:scope > .topic-explainer,:scope > .routine-points,:scope > .text-link').forEach(el=>el.classList.add('reveal'))});
document.querySelectorAll('.topic-nav,.steps,.reels,.treatment-columns').forEach(group=>Array.from(group.children).forEach((el,i)=>{el.classList.add('reveal');el.style.setProperty('--reveal-delay',`${Math.min(i,3)*85}ms`)}));
if('IntersectionObserver'in window){
 const revealObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');revealObserver.unobserve(entry.target)}}),{threshold:.035,rootMargin:'0px 0px -25px 0px'});
 document.querySelectorAll('.reveal').forEach(el=>revealObserver.observe(el));
 const photoObserver=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting)animatedPhotos.add(entry.target);else animatedPhotos.delete(entry.target)});scheduleScrollFrame()},{rootMargin:'100px 0px'});
 document.querySelectorAll('[data-parallax]').forEach(el=>photoObserver.observe(el));
 document.body.classList.toggle('js-motion',!motionPreference.matches);
}
function updateScrollEffects(){
 scrollFrame=0;
 const y=window.scrollY,viewport=window.innerHeight,total=document.documentElement.scrollHeight-viewport;
 progress.style.setProperty('--read-progress',String(total>0?Math.min(1,Math.max(0,y/total)):0));
 document.querySelector('.header').classList.toggle('scrolled',y>30);
 let active=-1;
 chapters.forEach((section,i)=>{const rect=section.getBoundingClientRect();if(rect.top<viewport*.45&&rect.bottom>130)active=i});
 scrollStatus.classList.toggle('active',active>=0);
 chapterLinks.forEach((link,i)=>{link.classList.toggle('current',i===active);if(i===active)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current')});
 if(active>=0){scrollStatus.querySelector('span').textContent=String(active+1).padStart(2,'0');scrollStatus.querySelector('p').textContent=chapterLinks[active].childNodes[0].textContent.trim()}
 if(!motionPreference.matches){animatedPhotos.forEach(photo=>{const rect=photo.getBoundingClientRect();const amount=(viewport*.5-(rect.top+rect.height*.5))/viewport;photo.style.setProperty('--photo-shift',`${Math.max(-16,Math.min(16,amount*22)).toFixed(2)}px`)})}
}
function scheduleScrollFrame(){if(!scrollFrame)scrollFrame=requestAnimationFrame(updateScrollEffects)}
window.addEventListener('scroll',scheduleScrollFrame,{passive:true});window.addEventListener('resize',scheduleScrollFrame,{passive:true});
motionPreference.addEventListener('change',()=>{document.body.classList.toggle('js-motion',!motionPreference.matches&&'IntersectionObserver'in window);scheduleScrollFrame()});
scheduleScrollFrame();
