import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Lis • Celebration Night",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Página praticamente toda em HTML (cinemático + ultra leve)
components.html(
    """
<!doctype html>
<html lang="pt-br">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  :root{
    --gold:#D4AF37;
    --ice:#F4F6FF;
    --ink:#0A0B12;
    --glass:rgba(10,11,18,0.55);
    --glass2:rgba(10,11,18,0.35);
  }

  html, body { height: 100%; margin: 0; }
  body {
    overflow: hidden;
    background: radial-gradient(1200px circle at 30% 25%, rgba(137, 92, 255, 0.25), transparent 55%),
                radial-gradient(900px circle at 80% 30%, rgba(0, 217, 255, 0.18), transparent 50%),
                radial-gradient(900px circle at 55% 85%, rgba(212,175,55, 0.12), transparent 45%),
                linear-gradient(180deg, #05060a 0%, #070818 40%, #0a0b12 100%);
    font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
  }

  /* Canvas em tela cheia */
  #fx {
    position: fixed;
    inset: 0;
    width: 100vw;
    height: 100vh;
  }

  /* Aurora suave (camada extra) */
  .aurora {
    position: fixed;
    inset: -20vh -20vw;
    background:
      radial-gradient(40vw 35vh at 20% 35%, rgba(0, 217, 255, 0.16), transparent 60%),
      radial-gradient(40vw 35vh at 70% 30%, rgba(137, 92, 255, 0.14), transparent 60%),
      radial-gradient(35vw 30vh at 55% 75%, rgba(212,175,55, 0.10), transparent 60%);
    filter: blur(30px);
    opacity: 0.9;
    animation: drift 10s ease-in-out infinite;
    pointer-events: none;
  }
  @keyframes drift {
    0%,100%{ transform: translate3d(0,0,0) scale(1); }
    50%{ transform: translate3d(2vw,-1vh,0) scale(1.03); }
  }

  /* HUD (conteúdo) */
  .wrap {
    position: relative;
    height: 100vh;
    display: grid;
    place-items: center;
    padding: 28px;
  }

  .card {
    width: min(920px, 92vw);
    background: linear-gradient(180deg, var(--glass), var(--glass2));
    border: 1px solid rgba(212,175,55,0.28);
    border-radius: 22px;
    padding: 56px 42px;
    box-shadow: 0 24px 70px rgba(0,0,0,0.65);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    position: relative;
    overflow: hidden;
  }

  .card:before{
    content:"";
    position:absolute;
    inset:-2px;
    background: conic-gradient(from 210deg,
      transparent,
      rgba(0,217,255,0.10),
      rgba(212,175,55,0.16),
      rgba(137,92,255,0.10),
      transparent);
    filter: blur(18px);
    opacity: 0.55;
    animation: halo 7s linear infinite;
  }
  @keyframes halo { to { transform: rotate(360deg);} }
  .card > *{ position: relative; z-index: 1; }

  .kicker{
    text-align:center;
    letter-spacing:0.34em;
    text-transform:uppercase;
    font-size:12px;
    color: rgba(212,175,55,0.92);
    margin-bottom: 14px;
  }

  .title{
    font-family: Cinzel, serif;
    font-size: 64px;
    line-height: 1.05;
    margin: 0;
    text-align: center;
    color: var(--ice);
    text-shadow: 0 0 18px rgba(0,217,255,0.14);
  }

  .subtitle{
    text-align:center;
    color: rgba(244,246,255,0.78);
    margin-top: 10px;
    font-size: 16px;
    letter-spacing: 0.10em;
    text-transform: uppercase;
  }

  .divider{
    height: 1px;
    margin: 26px 0;
    background: linear-gradient(90deg, transparent, rgba(212,175,55,0.65), transparent);
  }

  .msg{
    color: rgba(244,246,255,0.86);
    font-size: 18px;
    line-height: 1.95;
    font-weight: 300;
  }

  .msg strong{ color: rgba(212,175,55,0.96); font-weight: 600; }

  .actions{
    display:flex;
    gap: 14px;
    justify-content:center;
    flex-wrap: wrap;
    margin-top: 26px;
  }

  .btn{
    appearance:none;
    border-radius: 999px;
    padding: 14px 18px;
    min-width: 220px;
    font-family: Inter, sans-serif;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    font-size: 12px;
    cursor:pointer;
    transition: all .25s ease;
  }

  .btn.primary{
    background: rgba(212,175,55,0.12);
    border: 1px solid rgba(212,175,55,0.72);
    color: rgba(212,175,55,0.96);
  }
  .btn.primary:hover{
    background: rgba(212,175,55,0.22);
    box-shadow: 0 0 26px rgba(212,175,55,0.18);
    transform: translateY(-1px);
  }

  .btn.ghost{
    background: transparent;
    border: 1px solid rgba(244,246,255,0.25);
    color: rgba(244,246,255,0.80);
  }
  .btn.ghost:hover{
    border-color: rgba(0,217,255,0.55);
    box-shadow: 0 0 28px rgba(0,217,255,0.12);
    transform: translateY(-1px);
  }

  .hint{
    margin-top: 18px;
    text-align:center;
    color: rgba(244,246,255,0.42);
    font-size: 12px;
  }

  /* Assinatura “caligrafia” */
  .sigWrap{
    display:none;
    margin-top: 22px;
    justify-content: center;
  }
  .sig{
    width: min(520px, 86vw);
    height: 120px;
    opacity: 0.95;
  }
  .sig path{
    fill: none;
    stroke: rgba(212,175,55,0.92);
    stroke-width: 3.2;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-dasharray: 1200;
    stroke-dashoffset: 1200;
    filter: drop-shadow(0 0 10px rgba(212,175,55,0.18));
    animation: sign 2.8s ease forwards;
  }
  @keyframes sign { to { stroke-dashoffset: 0; } }

  /* Pequeno “selo” */
  .seal{
    display:inline-flex;
    margin: 18px auto 0;
    width: 86px;
    height: 86px;
    border-radius: 50%;
    border: 1px solid rgba(212,175,55,0.72);
    align-items:center;
    justify-content:center;
    color: rgba(212,175,55,0.95);
    letter-spacing: 0.20em;
    text-transform: uppercase;
    font-size: 10px;
    background: radial-gradient(circle at 30% 30%, rgba(212,175,55,0.16), transparent 70%);
    box-shadow: inset 0 0 18px rgba(212,175,55,0.18);
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
    pointer-events: none;
  }
</style>
</head>
<body>
  <canvas id="fx"></canvas>
  <div class="aurora"></div>

  <div class="wrap">
    <div class="card" role="article" aria-label="Cartão de aniversário">
      <div class="kicker">Celebration Night • Edição Especial</div>
      <h1 class="title">Lis</h1>
      <div class="subtitle">Uma homenagem sofisticada a um novo ciclo</div>
      <div class="divider"></div>

      <div class="msg">
        Prezada Lis,<br><br>
        Que este aniversário represente um marco de <strong>renovação</strong> e de merecido reconhecimento.
        Que o novo ciclo lhe traga serenidade, saúde e conquistas construídas com propósito —
        com a elegância de quem segue adiante sem perder a essência.<br><br>
        Receba, com respeito e admiração, estes votos sinceros.
      </div>

      <div style="text-align:center;"><div class="seal">Premium</div></div>

      <div class="actions">
        <button class="btn primary" id="celebrateBtn">✨ Celebrar</button>
        <button class="btn ghost" id="signBtn">✍️ Assinar Mensagem</button>
      </div>

      <div class="sigWrap" id="sigWrap" aria-hidden="true">
        <svg class="sig" viewBox="0 0 600 140" aria-label="Assinatura">
          <!-- Traço estilizado (simula caligrafia) -->
          <path d="M40,90 C80,30 140,30 160,88 C175,130 210,120 222,88 C240,40 272,42 290,84 C305,120 340,120 360,86 C390,35 430,40 448,82 C465,116 500,120 525,92 C545,70 565,68 585,78" />
          <path d="M70,100 C120,120 200,120 270,108" />
        </svg>
      </div>

      <div class="hint">Dica: clique em qualquer lugar da tela para lançar fogos discretos.</div>
    </div>
  </div>

  <div class="footer">Cinematic Canvas • 2025</div>

<script>
  // ---------- Canvas Fireworks (sem libs) ----------
  const canvas = document.getElementById('fx');
  const ctx = canvas.getContext('2d');

  let w, h, dpr;
  function resize(){
    dpr = Math.min(2, window.devicePixelRatio || 1);
    w = canvas.width  = Math.floor(window.innerWidth  * dpr);
    h = canvas.height = Math.floor(window.innerHeight * dpr);
    canvas.style.width  = window.innerWidth + 'px';
    canvas.style.height = window.innerHeight + 'px';
    ctx.setTransform(1,0,0,1,0,0);
    ctx.scale(dpr, dpr);
  }
  window.addEventListener('resize', resize);
  resize();

  // Estrelas fixas
  const stars = Array.from({length: 140}, () => ({
    x: Math.random()*window.innerWidth,
    y: Math.random()*window.innerHeight,
    r: Math.random()*1.4 + 0.2,
    a: Math.random()*0.6 + 0.15,
    tw: Math.random()*0.02 + 0.005,
  }));

  const particles = [];
  const trails = [];

  function rand(min, max){ return min + Math.random()*(max-min); }

  function makeFirework(x, y){
    // Traço inicial subindo
    trails.push({
      x0: window.innerWidth*0.5,
      y0: window.innerHeight + 30,
      x1: x,
      y1: y,
      t: 0,
      speed: rand(0.012, 0.02),
      hue: rand(40, 55), // dourado
    });

    // Explosão: partículas
    const count = Math.floor(rand(70, 110));
    for(let i=0;i<count;i++){
      const ang = rand(0, Math.PI*2);
      const sp  = rand(1.2, 4.4);
      particles.push({
        x, y,
        vx: Math.cos(ang)*sp,
        vy: Math.sin(ang)*sp,
        life: rand(60, 110),
        max: 0,
        hue: rand(38, 58),
        sat: rand(55, 85),
        lum: rand(55, 70),
        g: rand(0.02, 0.06),
      });
    }
  }

  function drawStars(){
    for(const s of stars){
      s.a += (Math.random()-0.5)*s.tw;
      s.a = Math.max(0.12, Math.min(0.85, s.a));
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

      // brilho do rastro
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

      // glitter
      if(Math.random() < 0.06){
        ctx.fillStyle = `rgba(212,175,55,${alpha*0.5})`;
        ctx.fillRect(p.x, p.y, 1, 1);
      }

      if(p.life <= 0){
        particles.splice(i,1);
      }
    }
  }

  function frame(){
    // efeito de "persistência" (cinema)
    ctx.fillStyle = 'rgba(10, 11, 18, 0.22)';
    ctx.fillRect(0,0,window.innerWidth, window.innerHeight);

    drawStars();
    drawTrails();
    drawParticles();

    requestAnimationFrame(frame);
  }
  // inicia com fundo limpo
  ctx.fillStyle = 'rgba(10, 11, 18, 1)';
  ctx.fillRect(0,0,window.innerWidth, window.innerHeight);
  requestAnimationFrame(frame);

  // Clique = fogos
  window.addEventListener('click', (e) => {
    // evitar disparar quando clica nos botões (para não duplicar), mas ainda permitir fogos no card
    const isButton = (e.target && (e.target.id === 'celebrateBtn' || e.target.id === 'signBtn'));
    const x = e.clientX;
    const y = Math.max(90, e.clientY - 40);
    if(!isButton) makeFirework(x, y);
  });

  // Botão celebrar: 3 explosões coreografadas
  document.getElementById('celebrateBtn').addEventListener('click', () => {
    const cx = window.innerWidth*0.5;
    const cy = window.innerHeight*0.34;
    makeFirework(cx, cy);
    setTimeout(() => makeFirework(cx - 180, cy + 60), 240);
    setTimeout(() => makeFirework(cx + 180, cy + 60), 480);
  });

  // Botão assinar: revela assinatura
  document.getElementById('signBtn').addEventListener('click', () => {
    const sw = document.getElementById('sigWrap');
    sw.style.display = 'flex';
    sw.setAttribute('aria-hidden', 'false');
    // fogos discretos no topo
    makeFirework(window.innerWidth*0.5, window.innerHeight*0.25);
  });

</script>
</body>
</html>
""",
    height=900,
    scrolling=False,
)
