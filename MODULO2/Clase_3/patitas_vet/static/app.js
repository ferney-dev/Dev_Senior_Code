const ownersCache = { list: [], map: new Map() };

function escapeHtml(text){
  return String(text||'')
    .replace(/&/g,'&amp;')
    .replace(/</g,'&lt;')
    .replace(/>/g,'&gt;')
    .replace(/"/g,'&quot;')
    .replace(/'/g,'&#039;');
}

async function fetchJson(url, opts){
  const res = await fetch(url, opts);
  if(!res.ok){
    const err = await res.json().catch(()=>({detail:res.statusText}));
    throw new Error(err.detail || res.statusText);
  }
  return res.status===204 ? null : res.json();
}

async function listarDuenos(){
  const listEl = document.getElementById('duenos-list');
  listEl.innerHTML = 'Cargando...';
  try{
    const data = await fetchJson('/duenos');
    ownersCache.list = data;
    ownersCache.map = new Map(data.map(o=>[o.id,o]));
    if(data.length===0){ listEl.innerHTML = '<p>No hay dueños registrados.</p>'; return }
    listEl.innerHTML = '';
    data.forEach(d=>{
      const card = document.createElement('div'); card.className='card';
      const left = document.createElement('div'); left.className='left';
      left.innerHTML = `<strong>${escapeHtml(d.nombre)}</strong><span>${escapeHtml(d.email)}</span><small>${escapeHtml(d.telefono)}</small>`;
      const actions = document.createElement('div');
      const edit = document.createElement('button'); edit.textContent='Editar'; edit.style.marginRight='8px';
      edit.onclick = ()=>prefillDueno(d);
      const del = document.createElement('button'); del.textContent='Eliminar'; del.style.background='#c0392b';
      del.onclick = async ()=>{
        if(!confirm(`Eliminar dueño ${d.nombre}?`)) return;
        await fetchJson(`/duenos/${d.id}`,{method:'DELETE'});
        await refreshAll();
      }
      actions.appendChild(edit); actions.appendChild(del);
      card.appendChild(left); card.appendChild(actions);
      listEl.appendChild(card);
    })
  }catch(e){ listEl.innerHTML = `<p style="color:#c0392b">${escapeHtml(e.message)}</p>` }
}

function prefillDueno(d){
  document.getElementById('dueno-id').value = d.id;
  document.getElementById('nombre').value = d.nombre;
  document.getElementById('telefono').value = d.telefono;
  document.getElementById('email').value = d.email;
  document.getElementById('dueno-cancel').style.display='inline-block';
}

function resetDuenoForm(){
  document.getElementById('dueno-form').reset();
  document.getElementById('dueno-id').value = '';
  document.getElementById('dueno-cancel').style.display='none';
}

document.getElementById('dueno-cancel').addEventListener('click', ()=>resetDuenoForm());

document.getElementById('dueno-form').addEventListener('submit', async (ev)=>{
  ev.preventDefault();
  const id = document.getElementById('dueno-id').value || null;
  const nombre = document.getElementById('nombre').value.trim();
  const telefono = document.getElementById('telefono').value.trim();
  const email = document.getElementById('email').value.trim();
  try{
    if(id){
      await fetchJson(`/duenos/${id}`,{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify({nombre,telefono,email})});
    }else{
      await fetchJson('/duenos',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({nombre,telefono,email})});
    }
    resetDuenoForm();
    await refreshAll();
  }catch(e){ alert('Error: '+e.message) }
});

// VETERINARIOS
async function listarVets(){
  const el = document.getElementById('vets-list'); el.innerHTML='Cargando...';
  try{
    const data = await fetchJson('/veterinarios');
    el.innerHTML='';
    if(data.length===0){ el.innerHTML='<p>No hay veterinarios registrados.</p>'; return }
    data.forEach(v=>{
      const card = document.createElement('div'); card.className='card';
      const left = document.createElement('div'); left.className='left';
      left.innerHTML = `<strong>${escapeHtml(v.nombre)}</strong><small>${escapeHtml(v.especialidad)}</small>`;
      const actions = document.createElement('div');
      const edit = document.createElement('button'); edit.textContent='Editar'; edit.style.marginRight='8px'; edit.onclick=()=>prefillVet(v);
      const del = document.createElement('button'); del.textContent='Eliminar'; del.style.background='#c0392b'; del.onclick=async ()=>{ if(!confirm('Eliminar?')) return; await fetchJson(`/veterinarios/${v.id}`,{method:'DELETE'}); await refreshAll(); }
      actions.appendChild(edit); actions.appendChild(del);
      card.appendChild(left); card.appendChild(actions);
      el.appendChild(card);
    })
  }catch(e){ el.innerHTML=`<p style="color:#c0392b">${escapeHtml(e.message)}</p>` }
}

function prefillVet(v){ document.getElementById('vet-id').value=v.id; document.getElementById('v-nombre').value=v.nombre; document.getElementById('v-especialidad').value=v.especialidad; document.getElementById('vet-cancel').style.display='inline-block'; }
function resetVetForm(){ document.getElementById('vet-form').reset(); document.getElementById('vet-id').value=''; document.getElementById('vet-cancel').style.display='none'; }
document.getElementById('vet-cancel').addEventListener('click', ()=>resetVetForm());
document.getElementById('vet-form').addEventListener('submit', async (ev)=>{ ev.preventDefault(); const id=document.getElementById('vet-id').value||null; const nombre=document.getElementById('v-nombre').value.trim(); const especialidad=document.getElementById('v-especialidad').value.trim(); try{ if(id){ await fetchJson(`/veterinarios/${id}`,{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify({nombre,especialidad})}); }else{ await fetchJson('/veterinarios',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({nombre,especialidad})}); } resetVetForm(); await refreshAll(); }catch(e){ alert('Error: '+e.message) } });

// MASCOTAS
async function populateDuenoSelect(){
  const sel = document.getElementById('m-dueno'); sel.innerHTML='';
  ownersCache.list.forEach(o=>{ const opt=document.createElement('option'); opt.value=o.id; opt.textContent=`${o.nombre} (${o.id})`; sel.appendChild(opt); });
}

async function listarMascotas(){
  const el = document.getElementById('mascotas-list'); el.innerHTML='Cargando...';
  try{
    const data = await fetchJson('/mascotas');
    el.innerHTML='';
    if(data.length===0){ el.innerHTML='<p>No hay mascotas registradas.</p>'; return }
    data.forEach(m=>{
      const card=document.createElement('div'); card.className='card';
      const left=document.createElement('div'); left.className='left';
      const owner = ownersCache.map.get(m.dueno_id);
      left.innerHTML = `<strong>${escapeHtml(m.nombre)}</strong><span>${escapeHtml(m.especie)} ${m.raza?('- '+escapeHtml(m.raza)):''}</span><small>Dueño: ${escapeHtml(owner?owner.nombre:('id:'+m.dueno_id))}</small>`;
      const actions=document.createElement('div');
      const edit=document.createElement('button'); edit.textContent='Editar'; edit.style.marginRight='8px'; edit.onclick=()=>prefillMascota(m);
      const del=document.createElement('button'); del.textContent='Eliminar'; del.style.background='#c0392b'; del.onclick=async ()=>{ if(!confirm('Eliminar mascota?')) return; await fetchJson(`/mascotas/${m.id}`,{method:'DELETE'}); await refreshAll(); }
      actions.appendChild(edit); actions.appendChild(del);
      card.appendChild(left); card.appendChild(actions); el.appendChild(card);
    })
  }catch(e){ el.innerHTML=`<p style="color:#c0392b">${escapeHtml(e.message)}</p>` }
}

function prefillMascota(m){ document.getElementById('mascota-id').value=m.id; document.getElementById('m-nombre').value=m.nombre; document.getElementById('m-especie').value=m.especie; document.getElementById('m-raza').value=m.raza||''; document.getElementById('m-fecha').value=m.fecha_nacimiento||''; document.getElementById('m-dueno').value=m.dueno_id; document.getElementById('mascota-cancel').style.display='inline-block'; }
function resetMascotaForm(){ document.getElementById('mascota-form').reset(); document.getElementById('mascota-id').value=''; document.getElementById('mascota-cancel').style.display='none'; }
document.getElementById('mascota-cancel').addEventListener('click', ()=>resetMascotaForm());
document.getElementById('mascota-form').addEventListener('submit', async (ev)=>{ ev.preventDefault(); const id=document.getElementById('mascota-id').value||null; const nombre=document.getElementById('m-nombre').value.trim(); const especie=document.getElementById('m-especie').value.trim(); const raza=document.getElementById('m-raza').value.trim()||null; const fecha=document.getElementById('m-fecha').value||null; const dueno_id=Number(document.getElementById('m-dueno').value); try{ const body={nombre,especie,raza,fecha_nacimiento: fecha, dueno_id}; if(id){ await fetchJson(`/mascotas/${id}`,{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}); }else{ await fetchJson('/mascotas',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}); } resetMascotaForm(); await refreshAll(); }catch(e){ alert('Error: '+e.message) } });

async function refreshAll(){ await listarDuenos(); await populateDuenoSelect(); await listarMascotas(); await listarVets(); }

// Inicializar
refreshAll();
