import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Lis • Caça ao Tesouro",
    page_icon="🎁",
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
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Raleway:wght@300;400;600&display=swap" rel="stylesheet">
<style>
  :root{
    --night:#0d0d15;
    --purple:#7c3aed;
    --cyan:#06b6d4;
    --gold:#fbbf24;
    --rose:#f43f5e;
    --mint:#10b981;
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  html,body{height:100%; overflow:hidden;}
  body{
    font-family: Raleway, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
    background: radial-gradient(1000px circle at 25% 15%, rgba(124,58,237,0.18), transparent 55%),
                radial-gradient(900px circle at 80% 40%, rgba(251,191,36,0.12), transparent 50%),
                linear-gradient(180deg, #0a0a12 0%, var(--night) 100%);
    color: #f9fafb;
  }

  /* Canvas (fundo estrelas + meteoros) */
  #sky{
    position:fixed;
    inset:0;
    z-index:0;
    pointer-events:none;
  }

  /* Balões flutuando (DOM) */
  .balloons{
    position:fixed;
    inset:0;
    z-index:1;
    pointer-events:none;
    display:none;
  }
  .balloon{
    position:absolute;
    font-size:48px;
    opacity:0.92;
    filter: drop-shadow(0 8px 16px rgba(0,0,0,0.4));
    animation: balloonFloat 7s ease-in-out infinite;
  }
  @keyframes balloonFloat{
    0%{ transform: translateY(120vh) scale(0.8); }
    100%{ transform: translateY(-120px) scale(1.1); }
  }

  /* Confetes */
  .confetti{
    position:fixed;
    inset:0;
    z-index:2;
    pointer-events:none;
    display:none;
    overflow:hidden;
  }
  .confetti i{
    position:absolute;
    top:-10vh;
    width:9px;
    height:15px;
    opacity:0.88;
    border-radius:2px;
    animation: confFall linear infinite;
    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
  }
  @keyframes confFall{
    to { transform: translateY(120vh) rotate(720deg); }
  }

  /* HUD principal */
  .scene{
    position:relative;
    z-index:10;
    height:100vh;
    display:flex;
    align-items: stretch;
    justify-content: center;
    padding: 18px;
  }

  .stage{
    width: min(1500px, 96vw);
    height: calc(100vh - 36px);
    display:flex;
    flex-direction: column;
    gap: 16px;
    background: rgba(13,13,21,0.58);
    border: 1px solid rgba(249,250,251,0.14);
    border-radius: 28px;
    padding: 26px 26px;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    box-shadow: 0 28px 80px rgba(0,0,0,0.72);
    position:relative;
    overflow:hidden;
  }

  .stage:before{
    content:"";
    position:absolute;
    inset:-3px;
    background: conic-gradient(from 180deg,
      transparent,
      rgba(124,58,237,0.16),
      rgba(251,191,36,0.14),
      rgba(6,182,212,0.12),
      transparent);
    filter: blur(20px);
    opacity:0.70;
    animation: orbit 9s linear infinite;
  }
  @keyframes orbit{ to{ transform: rotate(360deg);} }
  .stage>*{position:relative; z-index:1;}

  .header{
    display:flex;
    flex-direction: column;
    gap: 8px;
    align-items:center;
  }

  .badge{
    display:inline-flex;
    padding: 6px 18px;
    border-radius: 999px;
    background: rgba(124,58,237,0.18);
    border: 1px solid rgba(124,58,237,0.45);
    color: rgba(167,139,250,0.95);
    font-size: 11px;
    letter-spacing: 0.28em;
    text-transform: uppercase;
    font-weight: 600;
  }

  .title{
    font-family: Cinzel, serif;
    font-size: 68px;
    line-height: 1.02;
    text-align:center;
    margin:0;
    background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 45%, #fbbf24 100%);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
    text-shadow: 0 0 28px rgba(251,191,36,0.12);
    animation: titleShine 3s ease-in-out infinite;
  }
  @keyframes titleShine{
    0%,100%{ filter: brightness(1); }
    50%{ filter: brightness(1.15); }
  }

  .tagline{
    text-align:center;
    color: rgba(249,250,251,0.72);
    letter-spacing: 0.16em;
    text-transform: uppercase;
    font-size: 13px;
  }

  .sep{
    height:1px;
    width: min(920px, 92vw);
    background: linear-gradient(90deg, transparent, rgba(251,191,36,0.60), transparent);
    margin-top: 4px;
  }

  .body{
    flex: 1;
    display:grid;
    grid-template-columns: 1fr;
    gap: 14px;
    min-height: 0;
  }

  .info{
    width: 100%;
    background: rgba(249,250,251,0.04);
    border: 1px solid rgba(249,250,251,0.10);
    border-radius: 18px;
    padding: 16px 16px;
  }
  .info-line{
    font-size: 16px;
    line-height: 1.75;
    color: rgba(249,250,251,0.88);
  }
  .info-line strong{ color: rgba(6,182,212,0.95); font-weight: 600; }
  .hint{ margin-top:10px; font-size: 13px; color: rgba(249,250,251,0.58); }

  /* Zona de caça (maior que antes) */
  .hunt{
    position: relative;
    width: 100%;
    height: min(460px, 46vh);
    border-radius: 22px;
    border: 1px dashed rgba(249,250,251,0.16);
    background: radial-gradient(800px circle at 50% 50%, rgba(124,58,237,0.08), transparent 65%);
    overflow: hidden;
  }

  /* Alvos (caixas) para clicar */
  .target{
    position:absolute;
    width: 70px;
    height: 70px;
    font-size: 46px;
    display:flex;
    align-items:center;
    justify-content:center;
    cursor:pointer;
    transition: transform .2s ease, filter .2s ease;
    filter: drop-shadow(0 8px 16px rgba(0,0,0,0.35));
    animation: float 3s ease-in-out infinite;
  }
  .target:hover{
    transform: scale(1.12);
    filter: drop-shadow(0 12px 24px rgba(0,0,0,0.45));
  }
  @keyframes float{
    0%,100%{ transform: translateY(0); }
    50%{ transform: translateY(-12px); }
  }

  /* Botão grande revelação */
  .reveal{
    display:none;
    position:absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    background: linear-gradient(135deg, #fbbf24, #f59e0b);
    border: none;
    color: #0a0a12;
    font-family: Cinzel, serif;
    font-size: 24px;
    font-weight: 900;
    letter-spacing: 0.20em;
    text-transform: uppercase;
    min-width: min(820px, 88vw);
    padding: 26px 28px;
    border-radius: 18px;
    cursor:pointer;
    box-shadow: 0 24px 70px rgba(251,191,36,0.40);
    transition: all .3s ease;
  }
  .reveal:hover{ transform: translate(-50%, -50%) scale(1.04); box-shadow: 0 28px 80px rgba(251,191,36,0.50); }

  .final{
    display:none;
    width: 100%;
    text-align:center;
    padding: 18px 18px;
    border-radius: 18px;
    background: rgba(13,13,21,0.45);
    border: 1px solid rgba(251,191,36,0.32);
  }
  .final h2{
    font-family: Cinzel, serif;
    font-size: 40px;
    margin: 0 0 10px;
    background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 50%, #fbbf24 100%);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
  }
  .final p{
    margin:0;
    color: rgba(249,250,251,0.88);
    font-size: 16px;
    line-height: 1.9;
  }

  .foot{
    position: fixed;
    bottom: 12px;
    width: 100%;
    text-align:center;
    color: rgba(249,250,251,0.20);
    font-size: 10px;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    z-index: 20;
    pointer-events:none;
  }

  @media (max-width: 620px){
    .title{ font-size: 54px; }
    .reveal{ font-size: 20px; letter-spacing: 0.14em; }
  }
</style>
</head>
<body>
  <canvas id="sky"></canvas>

  <div class="balloons" id="balloons"></div>
  <div class="confetti" id="confetti"></div>

  <div class="scene">
    <div class="stage" role="article" aria-label="Cartão interativo">

      <div class="header">
        <div class="badge">🎯 Missão Especial</div>
        <h1 class="title">Lis</h1>
        <div class="tagline">Caça ao Tesouro de Aniversário</div>
        <div class="sep"></div>
      </div>

      <div class="body">
        <div class="info">
          <div class="info-line"><strong>Objetivo:</strong> Encontre e clique nas 5 caixas mágicas escondidas na zona de caça.</div>
          <div class="hint" id="hint">Caixas encontradas: <span id="count">0</span>/5 | Dica: elas se movem lentamente…</div>
        </div>

        <div class="hunt" id="hunt">
          <!-- Alvos gerados via JS -->
          <button class="reveal" id="revealBtn">🎉 Abrir Presente</button>
        </div>

        <div class="final" id="finalMsg">
          <h2>Feliz Aniversário, Lis! 🎊</h2>
          <p>
            Parabéns por completar a missão! Que seu novo ciclo seja repleto de conquistas, 
            alegrias e momentos inesquecíveis. Você merece toda a felicidade do mundo.<br><br>
            <strong>Lucas Duarte</strong>
          </p>
        </div>
      </div>

    </div>
  </div>

  <div class="foot">Celebration FX • Estrelas • Balões • Confetes</div>

<script>
  // ---------- ESTRELAS + METEOROS (Canvas) ----------
  const canvas = document.getElementById('sky');
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

  const stars = Array.from({length: 140}, () => ({
    x: Math.random()*window.innerWidth,
    y: Math.random()*window.innerHeight,
    r: Math.random()*1.5 + 0.2,
    a: Math.random()*0.60 + 0.12,
  }));

  const meteors = [];

  function rand(min,max){ return min + Math.random()*(max-min); }

  function spawnMeteor(){
    meteors.push({
      x: rand(0, window.innerWidth),
      y: rand(-50, window.innerHeight*0.3),
      vx: rand(3, 6),
      vy: rand(1.8, 3.2),
      life: rand(35, 65),
      hue: rand(40, 52),
    });
  }

  function drawStars(){
    for(const s of stars){
      const tw = (Math.random()-0.5)*0.03;
      s.a = Math.max(0.10, Math.min(0.75, s.a + tw));
      ctx.fillStyle = `rgba(249,250,251,${s.a})`;
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI*2);
      ctx.fill();
    }
  }

  function drawMeteors(){
    for(let i=meteors.length-1;i>=0;i--){
      const m = meteors[i];
      m.x += m.vx;
      m.y += m.vy;
      m.life -= 1;

      const alpha = Math.max(0, m.life/65);
      ctx.strokeStyle = `hsla(${m.hue}, 85%, 65%, ${alpha})`;
      ctx.lineWidth = 2.2;
      ctx.beginPath();
      ctx.moveTo(m.x, m.y);
      ctx.lineTo(m.x - m.vx*6, m.y - m.vy*6);
      ctx.stroke();

      if(m.life <= 0 || m.y > window.innerHeight){
        meteors.splice(i,1);
      }
    }
  }

  let meteorTimer = 0;
  let celebrateMode = false;

  function tick(){
    ctx.fillStyle = 'rgba(13, 13, 21, 0.24)';
    ctx.fillRect(0,0,window.innerWidth, window.innerHeight);

    drawStars();
    drawMeteors();

    meteorTimer++;
    const every = celebrateMode ? 18 : 60;
    if(meteorTimer % every === 0){
      spawnMeteor();
    }

    requestAnimationFrame(tick);
  }
  ctx.fillStyle = 'rgba(13, 13, 21, 1)';
  ctx.fillRect(0,0,window.innerWidth, window.innerHeight);
  requestAnimationFrame(tick);


  // ---------- CAÇA AO TESOURO (CAIXAS CLICÁVEIS) ----------
  const hunt = document.getElementById('hunt');
  const revealBtn = document.getElementById('revealBtn');
  const hint = document.getElementById('hint');
  const count = document.getElementById('count');
  const finalMsg = document.getElementById('finalMsg');

  const emojis = ['🎁','🎀','💎','🌟','🏆'];
  let found = 0;
  const TARGET_COUNT = 5;

  function createTarget(emoji){
    const el = document.createElement('div');
    el.className = 'target';
    el.textContent = emoji;
    el.style.left = rand(10, 92) + '%';
    el.style.top = rand(10, 82) + '%';
    el.style.animationDelay = rand(0, 1.5) + 's';

    // Movimento aleatório suave
    setInterval(() => {
      if(el.parentNode){
        const newX = Math.max(2, Math.min(94, parseFloat(el.style.left) + rand(-2.5, 2.5)));
        const newY = Math.max(2, Math.min(86, parseFloat(el.style.top) + rand(-2.5, 2.5)));
        el.style.transition = 'left 1.8s ease, top 1.8s ease';
        el.style.left = newX + '%';
        el.style.top = newY + '%';
      }
    }, 2000);

    el.addEventListener('click', () => {
      el.style.transition = 'transform 0.4s ease, opacity 0.4s ease';
      el.style.transform = 'scale(2) rotate(360deg)';
      el.style.opacity = '0';

      // Meteoro extra
      spawnMeteor();

      setTimeout(() => {
        el.remove();
        found++;
        count.textContent = found;

        if(found >= TARGET_COUNT){
          revealBtn.style.display = 'inline-block';
          hint.textContent = '🎯 Missão cumprida! Clique no botão grande para revelar o presente.';
        }
      }, 400);
    });

    hunt.appendChild(el);
  }

  // Spawnar caixas
  emojis.forEach(em => createTarget(em));


  // ---------- REVELAÇÃO FINAL (BALÕES + CONFETES + METEOROS) ----------
  const balloons = document.getElementById('balloons');
  const confetti = document.getElementById('confetti');

  function startBalloons(){
    balloons.style.display = 'block';
    balloons.innerHTML = '';
    const balloonEmojis = ['🎈','🎈','🎈','🎈','🎉','🎊'];
    for(let i=0;i<18;i++){
      const el = document.createElement('div');
      el.className = 'balloon';
      el.textContent = balloonEmojis[Math.floor(Math.random()*balloonEmojis.length)];
      el.style.left = (Math.random()*96 + 2) + '%';
      el.style.animationDuration = (Math.random()*3.5 + 5.5) + 's';
      el.style.animationDelay = (Math.random()*2) + 's';
      el.style.fontSize = (Math.random()*18 + 42) + 'px';
      balloons.appendChild(el);
    }
  }

  function startConfetti(){
    confetti.style.display = 'block';
    confetti.innerHTML = '';
    const cols = ['#fbbf24', '#f59e0b', '#7c3aed', '#06b6d4', '#10b981', '#f43f5e'];
    for(let i=0;i<120;i++){
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

  revealBtn.addEventListener('click', () => {
    finalMsg.style.display = 'block';
    startBalloons();
    startConfetti();
    celebrateMode = true; // mais meteoros

    // Meteoros em sequência
    for(let i=0;i<8;i++){
      setTimeout(() => spawnMeteor(), i * 280);
    }
  });

</script>
</body>
</html>
""",
    height=900,
    scrolling=False,
)
