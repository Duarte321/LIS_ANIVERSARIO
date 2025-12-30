import streamlit as st
import streamlit.components.v1 as components
import random

st.set_page_config(
    page_title="Lis • Memory Constellation",
    page_icon="🌠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Gera frases inspiradoras aleatórias
quotes = [
    "Brilhe como se ninguém estivesse assistindo.",
    "Cada ano é um capítulo, mas você é a autora.",
    "A vida é curta demais para não celebrar cada conquista.",
    "Idade é apenas a contagem de suas vitórias.",
    "Você não envelhece, você evolui.",
    "Seu melhor ano ainda está por vir.",
    "Celebre o caminho, não apenas o destino.",
]
random_quote = random.choice(quotes)

# Interface 100% customizada em HTML/CSS/JS
components.html(
    f"""
<!doctype html>
<html lang="pt-br">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{ height: 100%; overflow: hidden; }}
  body {{
    font-family: 'Space Grotesk', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    position: relative;
  }}

  /* Canvas para constelacao interativa */
  #constellation {{
    position: fixed;
    inset: 0;
    width: 100vw;
    height: 100vh;
  }}

  /* Container principal */
  .scene {{
    position: relative;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    z-index: 10;
  }}

  /* Logo/Badge animado */
  .badge {{
    width: 140px;
    height: 140px;
    border-radius: 50%;
    background: linear-gradient(135deg, rgba(255,255,255,0.25), rgba(255,255,255,0.08));
    border: 3px solid rgba(255,255,255,0.35);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 60px;
    margin-bottom: 20px;
    box-shadow: 0 15px 50px rgba(0,0,0,0.35);
    animation: float 3s ease-in-out infinite, glow 2s ease-in-out infinite;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
  }}

  @keyframes float {{
    0%, 100% {{ transform: translateY(0px); }}
    50% {{ transform: translateY(-15px); }}
  }}

  @keyframes glow {{
    0%, 100% {{ box-shadow: 0 15px 50px rgba(0,0,0,0.35), 0 0 30px rgba(255,255,255,0.2); }}
    50% {{ box-shadow: 0 15px 50px rgba(0,0,0,0.35), 0 0 60px rgba(255,255,255,0.4); }}
  }}

  /* Título principal */
  h1 {{
    font-family: 'Orbitron', sans-serif;
    font-size: 72px;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    text-shadow: 0 5px 25px rgba(0,0,0,0.5);
    margin-bottom: 8px;
    background: linear-gradient(90deg, #fff 30%, #f0e7ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }}

  .tagline {{
    font-size: 18px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    opacity: 0.85;
    margin-bottom: 40px;
  }}

  /* Container do "terminal" interativo */
  .terminal {{
    width: min(650px, 90vw);
    background: rgba(10, 10, 20, 0.75);
    border-radius: 14px;
    padding: 28px 32px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.12);
    position: relative;
  }}

  .terminal:before {{
    content: "";
    position: absolute;
    top: -2px;
    left: -2px;
    right: -2px;
    bottom: -2px;
    background: linear-gradient(135deg, rgba(102,126,234,0.4), rgba(118,75,162,0.4));
    border-radius: 14px;
    z-index: -1;
    filter: blur(8px);
    opacity: 0.6;
  }}

  .terminal-header {{
    display: flex;
    gap: 8px;
    margin-bottom: 20px;
  }}

  .dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: rgba(255,255,255,0.3);
  }}

  .terminal-body {{
    font-size: 16px;
    line-height: 1.85;
    color: rgba(255,255,255,0.92);
  }}

  .terminal-body .prompt {{
    color: #a78bfa;
    margin-right: 8px;
  }}

  .terminal-body .quote {{
    display: block;
    font-style: italic;
    margin: 18px 0;
    padding-left: 18px;
    border-left: 3px solid rgba(167,139,250,0.5);
    color: rgba(255,255,255,0.75);
  }}

  /* Botões de ação */
  .actions {{
    display: flex;
    gap: 12px;
    margin-top: 24px;
    justify-content: center;
    flex-wrap: wrap;
  }}

  .btn {{
    padding: 14px 28px;
    border: none;
    border-radius: 8px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 14px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 5px 20px rgba(0,0,0,0.25);
  }}

  .btn-primary {{
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
  }}

  .btn-primary:hover {{
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(102,126,234,0.5);
  }}

  .btn-secondary {{
    background: rgba(255,255,255,0.15);
    color: white;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
  }}

  .btn-secondary:hover {{
    background: rgba(255,255,255,0.25);
    transform: translateY(-2px);
  }}

  /* Contador de "estrelas coletadas" */
  .counter {{
    position: fixed;
    top: 20px;
    right: 20px;
    background: rgba(10,10,20,0.8);
    padding: 12px 20px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.05em;
    border: 1px solid rgba(255,255,255,0.2);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    box-shadow: 0 5px 20px rgba(0,0,0,0.3);
    z-index: 100;
  }}

  .counter span {{
    color: #a78bfa;
    font-weight: 700;
  }}

  /* Easter egg: mensagem secreta */
  .secret {{
    display: none;
    position: fixed;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(167,139,250,0.95);
    color: #0a0a14;
    padding: 16px 28px;
    border-radius: 12px;
    font-weight: 600;
    box-shadow: 0 10px 40px rgba(167,139,250,0.5);
    animation: slideUp 0.5s ease;
  }}

  @keyframes slideUp {{
    from {{ opacity: 0; transform: translateX(-50%) translateY(20px); }}
    to {{ opacity: 1; transform: translateX(-50%) translateY(0); }}
  }}

  /* Rodapé */
  .footer {{
    position: fixed;
    bottom: 12px;
    width: 100%;
    text-align: center;
    font-size: 11px;
    letter-spacing: 0.15em;
    opacity: 0.4;
    text-transform: uppercase;
  }}

</style>
</head>
<body>
  <canvas id="constellation"></canvas>

  <div class="counter">
    ✨ Estrelas: <span id="starCount">0</span>
  </div>

  <div class="scene">
    <div class="badge">🎂</div>
    <h1>LIS</h1>
    <div class="tagline">Constelation of Memories</div>

    <div class="terminal">
      <div class="terminal-header">
        <div class="dot" style="background: #ff6057;"></div>
        <div class="dot" style="background: #ffbd2e;"></div>
        <div class="dot" style="background: #28ca42;"></div>
      </div>
      <div class="terminal-body">
        <span class="prompt">system@birthday:~$</span> run celebration.sh<br>
        <span class="prompt">&gt;</span> Iniciando protocolo de aniversário...<br>
        <span class="prompt">&gt;</span> Carregando memórias felizes...<br>
        <span class="prompt">&gt;</span> <strong>Sucesso!</strong> Um novo ciclo foi desbloqueado.<br><br>

        <div class="quote">"{random_quote}"</div>

        <span class="prompt">&gt;</span> <strong>Mensagem:</strong> Lis, que este ano seja repleto de aventuras, 
        descobertas e momentos que façam você sorrir. Você é única, especial e merece toda a felicidade do universo. 🌟
      </div>

      <div class="actions">
        <button class="btn btn-primary" id="launchBtn">🚀 Lançar Fogos</button>
        <button class="btn btn-secondary" id="collectBtn">✨ Coletar Estrela</button>
      </div>
    </div>
  </div>

  <div class="secret" id="secretMsg">
    🎉 Conquista desbloqueada: "Caadora de Estrelas"! Parabéns, Lis!
  </div>

  <div class="footer">Interactive Experience • 2025</div>

<script>
  // ---------- CONSTELACAO INTERATIVA ----------
  const canvas = document.getElementById('constellation');
  const ctx = canvas.getContext('2d');

  let w, h;
  function resize() {{
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
  }}
  window.addEventListener('resize', resize);
  resize();

  // Partículas (estrelas)
  const stars = [];
  const maxStars = 120;

  class Star {{
    constructor() {{
      this.x = Math.random() * w;
      this.y = Math.random() * h;
      this.vx = (Math.random() - 0.5) * 0.2;
      this.vy = (Math.random() - 0.5) * 0.2;
      this.r = Math.random() * 2 + 0.5;
      this.alpha = Math.random() * 0.5 + 0.3;
    }}

    update() {{
      this.x += this.vx;
      this.y += this.vy;
      if(this.x < 0 || this.x > w) this.vx *= -1;
      if(this.y < 0 || this.y > h) this.vy *= -1;
    }}

    draw() {{
      ctx.fillStyle = `rgba(255,255,255,${{this.alpha}})`;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
      ctx.fill();
    }}
  }}

  for(let i=0; i<maxStars; i++) stars.push(new Star());

  // Fogos (explosões)
  const explosions = [];

  class Particle {{
    constructor(x, y) {{
      this.x = x;
      this.y = y;
      const angle = Math.random() * Math.PI * 2;
      const speed = Math.random() * 3 + 1;
      this.vx = Math.cos(angle) * speed;
      this.vy = Math.sin(angle) * speed;
      this.life = Math.random() * 60 + 40;
      this.maxLife = this.life;
      this.hue = Math.random() * 60 + 260; // roxo/azul
    }}

    update() {{
      this.x += this.vx;
      this.y += this.vy;
      this.vy += 0.08; // gravidade
      this.vx *= 0.98;
      this.vy *= 0.98;
      this.life -= 1;
    }}

    draw() {{
      const alpha = this.life / this.maxLife;
      ctx.fillStyle = `hsla(${{this.hue}}, 80%, 60%, ${{alpha}})`;
      ctx.beginPath();
      ctx.arc(this.x, this.y, 2, 0, Math.PI * 2);
      ctx.fill();
    }}
  }}

  function explode(x, y) {{
    for(let i=0; i<80; i++) {{
      explosions.push(new Particle(x, y));
    }}
  }}

  // Loop de animação
  function animate() {{
    ctx.fillStyle = 'rgba(102, 126, 234, 0.15)';
    ctx.fillRect(0, 0, w, h);

    // Estrelas
    stars.forEach(s => {{
      s.update();
      s.draw();
    }});

    // Fogos
    for(let i = explosions.length - 1; i >= 0; i--) {{
      explosions[i].update();
      explosions[i].draw();
      if(explosions[i].life <= 0) explosions.splice(i, 1);
    }}

    requestAnimationFrame(animate);
  }}
  animate();

  // ---------- INTERATIVIDADE ----------
  let starCount = 0;
  const starCountEl = document.getElementById('starCount');
  const secretMsg = document.getElementById('secretMsg');

  // Lançar fogos
  document.getElementById('launchBtn').addEventListener('click', () => {{
    explode(w * 0.5, h * 0.3);
    setTimeout(() => explode(w * 0.3, h * 0.4), 300);
    setTimeout(() => explode(w * 0.7, h * 0.4), 600);
  }});

  // Coletar estrela
  document.getElementById('collectBtn').addEventListener('click', () => {{
    starCount++;
    starCountEl.textContent = starCount;

    // Easter egg: ao coletar 5 estrelas
    if(starCount === 5) {{
      secretMsg.style.display = 'block';
      setTimeout(() => {{
        secretMsg.style.display = 'none';
      }}, 4000);
    }}
  }});

  // Clique na tela = fogos
  canvas.addEventListener('click', (e) => {{
    explode(e.clientX, e.clientY);
  }});

</script>
</body>
</html>
""",
    height=900,
    scrolling=False,
)
