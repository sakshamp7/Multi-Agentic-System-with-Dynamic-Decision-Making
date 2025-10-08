async function postJSON(url, data){
  const res = await fetch(url, {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(data)});
  return res.json();
}
document.getElementById('ask').onclick = async ()=>{
  const q = document.getElementById('query').value;
  const f = document.getElementById('file').files[0];
  if (f){
    const form = new FormData(); form.append('file', f);
    const r = await fetch('/upload_pdf', {method:'POST', body: form});
    const j = await r.json();
    const res = await postJSON('/ask', {text:q, file_id: j.file_id});
    document.getElementById('out').textContent = JSON.stringify(res, null, 2);
  } else {
    const res = await postJSON('/ask', {text:q});
    document.getElementById('out').textContent = JSON.stringify(res, null, 2);
  }
}
