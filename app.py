import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Lis • Pegadinha de Aniversário",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="collapsed",
)

components.html(
    """
<!doctype html>
<html lang="pt-br">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;800;900&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
<style>
  :root{
    --bg1:#070711;
    --bg2:#0b0b18;
    --gold:#D4AF37;
    --ice:#F4F6FF;
    --accent:#00d9ff;
    --rose:#ff4d6d;
  }
  *{box-sizing:border-box;}
  html,body{height:100%; margin:0; overflow:hidden;}
  body{
    font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
    background: radial-gradient(900px circle at 20% 20%, rgba(0,217,255,0.14), transparent 55%),
                radial-gradient(900px circle at 80% 30%, rgba(212,175,55,0.10), transparent 55%),
                linear-gradient(180deg, var(--bg1) 0%, var(--bg2) 100%);
    color: var(--ice);
  }

  /* Canvas de fogos (fundo) */
  #fx{
    position:fixed;
    inset:0;
    width:100vw;
    height:100vh;
    z-index:0;
    pointer-events:none;
  }

  /* Confetes (DOM) */
  .confetti{
    position:fixed;
    inset:0;
    z-index:1;
    pointer-events:none;
    overflow:hidden;
    display:none;
  }
  .confetti i{
    position:absolute;
    top:-10vh;
    width:10px;
    height:16px;
    opacity:0.85;
    border-radius:2px;
    transform: rotate(0deg);
    animation: confFall linear infinite;
    filter: drop-shadow(0 6px 10px rgba(0,0,0,0.35));
  }
  @keyframes confFall{
    to { transform: translateY(120vh) rotate(720deg); }
  }

  /* Bolos girando */
  .cakes{
    position:fixed;
    inset:0;
    z-index:2;
    pointer-events:none;
    display:none;
  }
  .cake{
    position:absolute;
    font-size:42px;
    opacity:0.9;
    filter: drop-shadow(0 10px 18px rgba(0,0,0,0.45));
    animation: cakeFloat 6s ease-in-out infinite;
  }
  @keyframes cakeFloat{
    0%{ transform: translateY(0) rotate(0deg) scale(1); }
    50%{ transform: translateY(-22px) rotate(180deg) scale(1.05); }
    100%{ transform: translateY(0) rotate(360deg) scale(1); }
  }

  /* Layout: ocupar a tela inteira de verdade */
  .wrap{
    position:relative;
    z-index:10;
    height:100vh;
    padding: 22px;
    display:flex;
    align-items: stretch;
    justify-content: center;
  }

  .panel{
    width: min(1400px, 96vw);
    height: calc(100vh - 44px);
    display:flex;
    flex-direction: column;
    gap: 18px;
    background: rgba(10, 11, 18, 0.55);
    border: 1px solid rgba(244,246,255,0.16);
    border-radius: 26px;
    padding: 28px 28px;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    box-shadow: 0 24px 70px rgba(0,0,0,0.68);
    position:relative;
    overflow:hidden;
  }

  .panel:before{
    content:"";
    position:absolute;
    inset:-2px;
    background: conic-gradient(from 200deg,
      transparent,
      rgba(0,217,255,0.14),
      rgba(212,175,55,0.14),
      rgba(255,77,109,0.12),
      transparent);
    filter: blur(18px);
    opacity:0.65;
    animation: halo 8s linear infinite;
  }
  @keyframes halo{ to{ transform: rotate(360deg);} }
  .panel>*{position:relative; z-index:1;}

  .top{
    display:flex;
    flex-direction: column;
    gap: 10px;
    align-items:center;
  }

  .kicker{
    text-align:center;
    letter-spacing:0.34em;
    text-transform:uppercase;
    font-size:12px;
    color: rgba(212,175,55,0.90);
  }

  .title{
    font-family: Playfair Display, serif;
    font-size: 64px;
    line-height: 1.02;
    text-align:center;
    margin:0;
    background: linear-gradient(135deg, #ffffff 0%, #ffe29a 35%, #ffd700 65%, #ffffff 100%);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
    text-shadow: 0 0 24px rgba(0,217,255,0.10);
  }

  .sub{
    text-align:center;
    color: rgba(244,246,255,0.75);
    letter-spacing: 0.14em;
    text-transform: uppercase;
    font-size: 13px;
  }

  .divider{
    height:1px;
    width: min(860px, 92vw);
    background: linear-gradient(90deg, transparent, rgba(212,175,55,0.65), transparent);
    margin-top: 6px;
  }

  .mid{
    display:grid;
    grid-template-columns: 1fr;
    gap: 16px;
    align-items: start;
    flex: 1;
    min-height: 0;
  }

  .chat{
    width: 100%;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(244,246,255,0.12);
    border-radius: 18px;
    padding: 18px 18px;
  }
  .line{
    font-size: 16px;
    line-height: 1.75;
    color: rgba(244,246,255,0.88);
  }
  .line strong{ color: rgba(0,217,255,0.92); font-weight: 600; }
  .tease{ margin-top:10px; font-size: 13px; color: rgba(244,246,255,0.60); }

  /* Arena maior, para usar a tela inteira */
  .arena{
    position: relative;
    width: 100%;
    height: min(420px, 44vh);
    border-radius: 20px;
    border: 1px dashed rgba(244,246,255,0.18);
    background: radial-gradient(700px circle at 50% 50%, rgba(0,217,255,0.06), transparent 60%);
    overflow: hidden;
  }

  .btn{
    appearance:none;
    border-radius: 999px;
    padding: 16px 20px;
    min-width: 260px;
    font-family: Inter, sans-serif;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    font-size: 12px;
    cursor:pointer;
    transition: transform .18s ease, box-shadow .18s ease;
    user-select: none;
  }

  .btn.prank{
    position:absolute;
    left: 50%;
    top: 54%;
    transform: translate(-50%, -50%);
    background: rgba(0,217,255,0.10);
    border: 1px solid rgba(0,217,255,0.65);
    color: rgba(0,217,255,0.95);
    box-shadow: 0 18px 40px rgba(0,0,0,0.35);
  }
  .btn.prank:hover{ transform: translate(-50%, -50%) scale(1.02); }

  .btn.big{
    display:none;
    position:absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    background: linear-gradient(135deg, #FFD700, #FFA500);
    border: none;
    color: #0a0a0f;
    font-family: Playfair Display, serif;
    font-size: 22px;
    font-weight: 900;
    letter-spacing: 0.18em;
    min-width: min(720px, 86vw);
    padding: 24px 28px;
    box-shadow: 0 22px 60px rgba(255,215,0,0.35);
  }
  .btn.big:hover{ transform: translate(-50%, -50%) scale(1.03); box-shadow: 0 26px 70px rgba(255,215,0,0.45); }

  .final{
    display:none;
    width: 100%;
    text-align:center;
    padding: 18px 18px;
    border-radius: 18px;
    background: rgba(10,11,18,0.42);
    border: 1px solid rgba(212,175,55,0.32);
  }
  .final h2{
    font-family: Playfair Display, serif;
    font-size: 36px;
    margin: 0 0 8px;
    color: rgba(212,175,55,0.95);
  }
  .final p{
    margin:0;
    color: rgba(244,246,255,0.86);
    font-size: 16px;
    line-height: 1.8;
  }

  .footer{
    position: fixed;
    bottom: 12px;
    width: 100%;
    text-align:center;
    color: rgba(244,246,255,0.22);
    font-size: 10px;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    z-index: 20;
    pointer-events:none;
  }

  @media (max-width: 620px){
    .title{ font-size: 52px; }
    .btn.big{ font-size: 18px; letter-spacing: 0.12em; }
  }
</style>
</head>
<body>
  <canvas id="fx"></canvas>

  <div class="confetti" id="confetti"></div>
  <div class="cakes" id="cakes"></div>

  <div class="wrap">
    <div class="panel" role="article" aria-label="Cartão de aniversário">

      <div class="top">
        <div class="kicker">Pegadinha • Edição Especial</div>
        <h1 class="title">Lis</h1>
        <div class="sub">Hoje é o seu dia — e a missão é simples 😄</div>
        <div class="divider"></div>
      </div>

      <div class="mid">
        <div class="chat">
          <div class="line"><strong>Mensagem:</strong> Existe um presente pra você… mas primeiro precisamos confirmar se você tem reflexo de campeã.</div>
          <div class="tease" id="tease">Missão: clique no botão. (Aviso: ele é ligeiro.)</div>
        </div>

        <div class="arena" id="arena">
          <button class="btn prank" id="prankBtn">🎁 Resgatar Presente</button>
          <button class="btn big" id="bigBtn">AGORA PODE APERTAR 😌</button>
        </div>

        <div class="final" id="finalMsg">
          <h2>Feliz Aniversário, Lis! 🎉</h2>
          <p>
            Que seu novo ciclo seja leve, próspero e cheio de motivos para sorrir. 
            Que nunca falte saúde, paz e gente querida por perto.<br><br>
            <strong>Lucas Duarte</strong>
          </p>
        </div>
      </div>

    </div>
  </div>

  <div class="footer">Celebration FX • Confetes • Fogos • Bolos no ar</div>

<script>
  // ---------- FOGOS AUTOMÁTICOS (Canvas) ----------
  const canvas = document.getElementById('fx');
  const ctx = canvas.getContext('2d');
  let W, H, DPR;

  function resize(){
    DPR = Math.min(2, window.devicePixelRatio || 1);
    W = canvas.width = Math.floor(window.innerWidth * DPR);
    H = canvas.height = Math.floor(window.innerHeight * DPR);
    canvas.style.width = window.innerWidth + 'px';
    canvas.style.height = window.innerHeight + 'px';
    ctx.setTransform(1,0,0,1,0,0);
    ctx.scale(DPR, DPR);
  }
  window.addEventListener('resize', resize);
  resize();

  const particles = [];
  const trails = [];
  const stars = Array.from({length: 120}, () => ({
    x: Math.random()*window.innerWidth,
    y: Math.random()*window.innerHeight,
    r: Math.random()*1.4 + 0.2,
    a: Math.random()*0.55 + 0.12,
  }));

  function rand(min,max){ return min + Math.random()*(max-min); }

  function launchFirework(x, y, hueBase=45){
    trails.push({
      x0: rand(window.innerWidth*0.2, window.innerWidth*0.8),
      y0: window.innerHeight + 30,
      x1: x,
      y1: y,
      t: 0,
      speed: rand(0.012, 0.02),
      hue: rand(hueBase-8, hueBase+8)
    });

    const count = Math.floor(rand(70, 115));
    for(let i=0;i<count;i++){
      const ang = rand(0, Math.PI*2);
      const sp = rand(1.2, 4.2);
      particles.push({
        x, y,
        vx: Math.cos(ang)*sp,
        vy: Math.sin(ang)*sp,
        life: rand(55, 105),
        hue: rand(hueBase-10, hueBase+12),
        sat: rand(60, 90),
        lum: rand(55, 70),
        g: rand(0.02, 0.06),
      });
    }
  }

  function drawStars(){
    for(const s of stars){
      const tw = (Math.random()-0.5)*0.03;
      s.a = Math.max(0.10, Math.min(0.75, s.a + tw));
      ctx.fillStyle = `rgba(244,246,255,${s.a})`;
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI*2);
      ctx.fill();
    }
  }

  function drawTrails(){
    for(let i=trails.length-1;i>=0;i--){
      const tr = trails[i];
      tr.t += tr.speed;
      const t = Math.min(1, tr.t);
      const x = tr.x0 + (tr.x1 - tr.x0)*t;
      const y = tr.y0 + (tr.y1 - tr.y0)*t;

      ctx.strokeStyle = `hsla(${tr.hue}, 90%, 65%, ${0.55*(1-t)})`;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(tr.x0, tr.y0);
      ctx.lineTo(x, y);
      ctx.stroke();

      if(t >= 1){
        trails.splice(i,1);
      }
    }
  }

  function drawParticles(){
    for(let i=particles.length-1;i>=0;i--){
      const p = particles[i];
      p.x += p.vx;
      p.y += p.vy;
      p.vy += p.g;
      p.vx *= 0.985;
      p.vy *= 0.985;
      p.life -= 1;

      const alpha = Math.max(0, p.life/110);
      ctx.fillStyle = `hsla(${p.hue}, ${p.sat}%, ${p.lum}%, ${alpha})`;
      ctx.beginPath();
      ctx.arc(p.x, p.y, 1.6, 0, Math.PI*2);
      ctx.fill();

      if(Math.random() < 0.06){
        ctx.fillStyle = `rgba(212,175,55,${alpha*0.5})`;
        ctx.fillRect(p.x, p.y, 1, 1);
      }

      if(p.life <= 0){
        particles.splice(i,1);
      }
    }
  }

  let celebrateMode = false;
  let autoTimer = 0;

  function tick(){
    ctx.fillStyle = 'rgba(10, 11, 18, 0.22)';
    ctx.fillRect(0,0,window.innerWidth, window.innerHeight);

    drawStars();
    drawTrails();
    drawParticles();

    autoTimer++;
    const every = celebrateMode ? 22 : 70;
    if(autoTimer % every === 0){
      const x = rand(120, window.innerWidth-120);
      const y = rand(90, window.innerHeight*0.55);
      const hue = celebrateMode ? rand(35, 55) : rand(40, 52);
      launchFirework(x, y, hue);
    }

    requestAnimationFrame(tick);
  }
  ctx.fillStyle = 'rgba(10, 11, 18, 1)';
  ctx.fillRect(0,0,window.innerWidth, window.innerHeight);
  requestAnimationFrame(tick);


  // ---------- PEGADINHA: BOTÃO FUGINDO ----------
  const arena = document.getElementById('arena');
  const prankBtn = document.getElementById('prankBtn');
  const bigBtn = document.getElementById('bigBtn');
  const tease = document.getElementById('tease');
  const finalMsg = document.getElementById('finalMsg');

  let dodges = 0;
  const DODGE_TARGET = 9;

  const roasts = [
    'Quase… quase… quase… 😄',
    'Atenção: botão com vida própria!',
    'Tá achando que é fácil?',
    'Se pegar, ganha bolo. Se não pegar, ganha bolo também.',
    'Calma, Lis… ele tá tímido!',
    'Cuidado! Esse presente é arisco 🤭',
  ];

  function clamp(v, min, max){ return Math.max(min, Math.min(max, v)); }

  function moveButtonAway(mouseX, mouseY){
    const rect = arena.getBoundingClientRect();
    const b = prankBtn.getBoundingClientRect();

    const btnW = b.width;
    const btnH = b.height;

    let x, y, tries = 0;
    do {
      x = rect.left + 18 + Math.random()*(rect.width - btnW - 36);
      y = rect.top  + 18 + Math.random()*(rect.height - btnH - 36);
      tries++;
      if(tries > 16) break;
    } while (Math.hypot((x+btnW/2)-mouseX, (y+btnH/2)-mouseY) < 160);

    const left = clamp(x - rect.left, 10, rect.width - btnW - 10);
    const top  = clamp(y - rect.top , 10, rect.height - btnH - 10);

    prankBtn.style.left = left + 'px';
    prankBtn.style.top  = top + 'px';
    prankBtn.style.transform = 'none';
  }

  function centerPrank(){
    prankBtn.style.left = '50%';
    prankBtn.style.top = '54%';
    prankBtn.style.transform = 'translate(-50%, -50%)';
  }
  centerPrank();

  arena.addEventListener('mousemove', (e) => {
    if(prankBtn.style.display === 'none') return;

    const b = prankBtn.getBoundingClientRect();
    const bx = b.left + b.width/2;
    const by = b.top + b.height/2;
    const d = Math.hypot(bx - e.clientX, by - e.clientY);

    if(d < 150){
      dodges++;
      tease.textContent = roasts[dodges % roasts.length] + ` (Tentativas: ${dodges})`;
      moveButtonAway(e.clientX, e.clientY);

      // fogos discretos ao “desviar”
      launchFirework(rand(140, window.innerWidth-140), rand(90, window.innerHeight*0.45), rand(40,55));

      if(dodges >= DODGE_TARGET){
        prankBtn.style.display = 'none';
        bigBtn.style.display = 'inline-block';
        tease.textContent = 'Ok ok… agora pode apertar (sem correr) 😌';
      }
    }
  });

  prankBtn.addEventListener('click', () => {
    dodges += 2;
    tease.textContent = 'Eita! Quase pegou… mas não valeu 😄';
    moveButtonAway(window.innerWidth/2, window.innerHeight/2);
    if(dodges >= DODGE_TARGET){
      prankBtn.style.display = 'none';
      bigBtn.style.display = 'inline-block';
      tease.textContent = 'Agora sim. Aperta o grandão 😌';
    }
  });


  // ---------- REVELAÇÃO FINAL (CONFETES + BOLOS + FOGOS AUTOMÁTICOS) ----------
  const confetti = document.getElementById('confetti');
  const cakes = document.getElementById('cakes');

  function startConfetti(){
    confetti.style.display = 'block';
    confetti.innerHTML = '';
    const cols = ['#FFD700', '#FFA500', '#00d9ff', '#ff4d6d', '#7c3aed', '#34d399'];
    for(let i=0;i<110;i++){
      const el = document.createElement('i');
      el.style.left = Math.random()*100 + '%';
      el.style.background = cols[Math.floor(Math.random()*cols.length)];
      el.style.animationDuration = (Math.random()*2.8 + 2.8) + 's';
      el.style.animationDelay = (Math.random()*1.8) + 's';
      el.style.width  = (Math.random()*7 + 5) + 'px';
      el.style.height = (Math.random()*12 + 8) + 'px';
      confetti.appendChild(el);
    }
  }

  function startCakes(){
    cakes.style.display = 'block';
    cakes.innerHTML = '';
    const emojis = ['🎂','🍰','🧁','🍩'];
    for(let i=0;i<16;i++){
      const el = document.createElement('div');
      el.className = 'cake';
      el.textContent = emojis[Math.floor(Math.random()*emojis.length)];
      el.style.left = (Math.random()*92 + 2) + '%';
      el.style.top  = (Math.random()*80 + 6) + '%';
      el.style.animationDuration = (Math.random()*3.6 + 4.2) + 's';
      el.style.animationDelay = (Math.random()*1.2) + 's';
      el.style.fontSize = (Math.random()*22 + 34) + 'px';
      cakes.appendChild(el);
    }
  }

  bigBtn.addEventListener('click', () => {
    finalMsg.style.display = 'block';
    startConfetti();
    startCakes();
    celebrateMode = true;

    // sequência coreografada
    setTimeout(() => launchFirework(window.innerWidth*0.50, window.innerHeight*0.28, 45), 120);
    setTimeout(() => launchFirework(window.innerWidth*0.33, window.innerHeight*0.36, 48), 320);
    setTimeout(() => launchFirework(window.innerWidth*0.67, window.innerHeight*0.36, 42), 520);
    setTimeout(() => launchFirework(window.innerWidth*0.50, window.innerHeight*0.22, 50), 820);
  });

</script>
</body>
</html>
""",
    height=900,
    scrolling=False,
)
