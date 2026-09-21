const grid    = document.getElementById('grid');
const q       = document.getElementById('q');
const countEl = document.getElementById('count');
const overlay = document.getElementById('overlay');
const mBody   = document.getElementById('m-body');

let currentId = 1;
let timer = null;

function esc(s){
  return String(s).replace(/[&<>"']/g, c => (
    {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]
  ));
}

/* ---------- load the grid from the backend ---------- */
async function loadNames(term=''){
  try{
    const url = term ? `/api/names?q=${encodeURIComponent(term)}` : '/api/names';
    const res = await fetch(url);
    if(!res.ok) throw new Error('Request failed');
    const data = await res.json();

    countEl.textContent = data.count === 99 ? '99 names' : `${data.count} of 99`;

    grid.innerHTML = data.names.length
      ? data.names.map(n => `
        <article class="card" data-id="${n.id}" tabindex="0">
          <div class="num">${n.id}</div>
          <div class="ar">${esc(n.arabic)}</div>
          <div class="tr">${esc(n.transliteration)}</div>
          <div class="mn">${esc(n.meaning)}</div>
        </article>`).join('')
      : `<div class="empty">No name matches that search.</div>`;
  }catch(err){
    grid.innerHTML = `<div class="empty">Could not load the names. Is the server running?</div>`;
    countEl.textContent = '—';
    console.error(err);
  }
}

/* ---------- fetch full detail for one name ---------- */
async function openName(id){
  currentId = id;
  overlay.classList.add('open');
  mBody.innerHTML = `<div class="loader">Loading…</div>`;
  try{
    const res = await fetch(`/api/names/${id}`);
    if(!res.ok) throw new Error('Not found');
    const n = await res.json();
    mBody.innerHTML = `
      <div class="m-head">
        <div class="num">${n.id}</div>
        <div class="ar">${esc(n.arabic)}</div>
        <div class="tr">${esc(n.transliteration)}</div>
        <div class="mn">${esc(n.meaning)}</div>
      </div>
      <div class="block">
        <h3>Meaning in depth</h3>
        <p>${esc(n.detail)}</p>
      </div>
      <div class="block quote">
        <h3>In the Qur'an</h3>
        <p>${esc(n.quran)}</p>
      </div>
      <div class="block">
        <h3>Reflection</h3>
        <p>${esc(n.reflection)}</p>
      </div>
      <div class="nav">
        <button data-go="${n.prev_id}">← Previous</button>
        <button data-go="${n.next_id}">Next →</button>
      </div>`;
  }catch(err){
    mBody.innerHTML = `<div class="loader">Could not load this name.</div>`;
    console.error(err);
  }
}

function closeModal(){ overlay.classList.remove('open'); }

/* ---------- events ---------- */
grid.addEventListener('click', e => {
  const c = e.target.closest('.card');
  if(c) openName(+c.dataset.id);
});
grid.addEventListener('keydown', e => {
  const c = e.target.closest('.card');
  if(c && (e.key === 'Enter' || e.key === ' ')){ e.preventDefault(); openName(+c.dataset.id); }
});

mBody.addEventListener('click', e => {
  const b = e.target.closest('[data-go]');
  if(b) openName(+b.dataset.go);
});

document.getElementById('close').onclick = closeModal;
overlay.addEventListener('click', e => { if(e.target === overlay) closeModal(); });

document.addEventListener('keydown', e => {
  if(!overlay.classList.contains('open')) return;
  if(e.key === 'Escape') closeModal();
  if(e.key === 'ArrowRight') openName(currentId === 99 ? 1 : currentId + 1);
  if(e.key === 'ArrowLeft')  openName(currentId === 1 ? 99 : currentId - 1);
});

q.addEventListener('input', () => {
  clearTimeout(timer);
  timer = setTimeout(() => loadNames(q.value.trim()), 180);
});

document.getElementById('random').onclick = async () => {
  const res = await fetch('/api/random');
  const n = await res.json();
  openName(n.id);
};

const tbtn = document.getElementById('theme');
try{
  const saved = localStorage.getItem('aah-theme');
  if(saved) document.documentElement.setAttribute('data-theme', saved);
}catch(e){}
tbtn.onclick = () => {
  const next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  try{ localStorage.setItem('aah-theme', next); }catch(e){}
};

loadNames();
