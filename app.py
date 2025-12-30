import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Lis • Premium Spin",
    page_icon="🎰",
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
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { height: 100%; overflow: hidden; }
  body {
    font-family: 'Inter', sans-serif;
    background: radial-gradient(circle at 30% 20%, rgba(138,43,226,0.15), transparent 60%),
                radial-gradient(circle at 75% 40%, rgba(255,215,0,0.12), transparent 55%),
                linear-gradient(180deg, #0a0a0f 0%, #151520 100%);
    color: #f4f4f6;
    position: relative;
  }

  /* Partículas de luxo flutuando */
  .particles {
    position: fixed;
    inset: 0;
    pointer-events: none;
    overflow: hidden;
  }

  .particle {
    position: absolute;
    width: 4px;
    height: 4px;
    background: radial-gradient(circle, rgba(255,215,0,0.8), transparent);
    border-radius: 50%;
    opacity: 0;
    animation: floatUp linear infinite;
  }

  @keyframes floatUp {
    0% { transform: translateY(100vh) scale(0); opacity: 0; }
    10% { opacity: 0.6; }
    90% { opacity: 0.3; }
    100% { transform: translateY(-100px) scale(1.2); opacity: 0; }
  }

  /* Wrapper principal */
  .wrapper {
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    position: relative;
    z-index: 10;
  }

  /* Título premium */
  .title {
    font-family: 'Playfair Display', serif;
    font-size: 64px;
    font-weight: 900;
    text-align: center;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
    background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #FFD700 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 0 40px rgba(255,215,0,0.3);
    cursor: pointer;
    user-select: none;
  }

  .subtitle {
    text-align: center;
    font-size: 14px;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: rgba(255,215,0,0.75);
    margin-bottom: 50px;
  }

  /* Container da roleta */
  .wheel-container {
    position: relative;
    width: 420px;
    height: 420px;
    margin: 0 auto 40px;
  }

  #wheelCanvas {
    display: block;
    filter: drop-shadow(0 20px 60px rgba(0,0,0,0.6));
  }

  /* Indicador (seta) */
  .pointer {
    position: absolute;
    top: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 0;
    height: 0;
    border-left: 18px solid transparent;
    border-right: 18px solid transparent;
    border-top: 35px solid #FFD700;
    filter: drop-shadow(0 5px 15px rgba(255,215,0,0.6));
    z-index: 20;
  }

  /* Botão GIRAR */
  .spin-btn {
    display: block;
    margin: 0 auto;
    padding: 18px 45px;
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: #0a0a0f;
    background: linear-gradient(135deg, #FFD700, #FFA500);
    border: none;
    border-radius: 50px;
    cursor: pointer;
    box-shadow: 0 10px 40px rgba(255,215,0,0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
  }

  .spin-btn:before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255,255,255,0.3);
    transform: translate(-50%, -50%);
    transition: width 0.6s, height 0.6s;
  }

  .spin-btn:hover:before {
    width: 300px;
    height: 300px;
  }

  .spin-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 50px rgba(255,215,0,0.6);
  }

  .spin-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  /* Modal de resultado */
  .result-modal {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.85);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    z-index: 1000;
    align-items: center;
    justify-content: center;
    animation: fadeIn 0.4s ease;
  }

  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  .result-card {
    background: linear-gradient(135deg, rgba(20,20,30,0.95), rgba(30,30,45,0.95));
    border: 2px solid rgba(255,215,0,0.4);
    border-radius: 20px;
    padding: 50px 60px;
    text-align: center;
    max-width: 500px;
    box-shadow: 0 30px 80px rgba(0,0,0,0.7);
    animation: scaleIn 0.5s cubic-bezier(0.68, -0.55, 0.27, 1.55);
  }

  @keyframes scaleIn {
    from { transform: scale(0.5); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
  }

  .result-emoji {
    font-size: 80px;
    margin-bottom: 20px;
    animation: bounce 0.6s ease;
  }

  @keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
  }

  .result-text {
    font-family: 'Playfair Display', serif;
    font-size: 26px;
    font-weight: 700;
    color: #FFD700;
    margin-bottom: 15px;
  }

  .result-desc {
    font-size: 16px;
    color: rgba(244,244,246,0.8);
    line-height: 1.6;
  }

  .close-btn {
    margin-top: 30px;
    padding: 12px 35px;
    background: transparent;
    border: 2px solid rgba(255,215,0,0.5);
    color: #FFD700;
    border-radius: 30px;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
  }

  .close-btn:hover {
    background: rgba(255,215,0,0.15);
    border-color: #FFD700;
  }

  /* Modo trapaça */
  .cheat-indicator {
    display: none;
    position: fixed;
    top: 20px;
    right: 20px;
    background: rgba(138,43,226,0.9);
    padding: 10px 20px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    box-shadow: 0 5px 20px rgba(138,43,226,0.5);
    animation: pulse 1.5s ease-in-out infinite;
  }

  @keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
  }

  .footer {
    position: fixed;
    bottom: 15px;
    width: 100%;
    text-align: center;
    font-size: 11px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: rgba(244,244,246,0.3);
  }

</style>
</head>
<body>
  <!-- Partículas -->
  <div class="particles" id="particles"></div>

  <!-- Indicador modo trapaça -->
  <div class="cheat-indicator" id="cheatMode">🍀 Modo Sorte Grande</div>

  <div class="wrapper">
    <h1 class="title" id="titleClick">LIS</h1>
    <div class="subtitle">Premium Celebration Wheel</div>

    <div class="wheel-container">
      <div class="pointer"></div>
      <canvas id="wheelCanvas" width="420" height="420"></canvas>
    </div>

    <button class="spin-btn" id="spinBtn">🎰 Girar Roleta</button>
  </div>

  <!-- Modal resultado -->
  <div class="result-modal" id="resultModal">
    <div class="result-card">
      <div class="result-emoji" id="resultEmoji">🎉</div>
      <div class="result-text" id="resultText">Parabéns!</div>
      <div class="result-desc" id="resultDesc">Você ganhou algo especial!</div>
      <button class="close-btn" id="closeBtn">Continuar</button>
    </div>
  </div>

  <div class="footer">Luxe Experience • 2025</div>

<script>
  // Prêmios
  const prizes = [
    { text: 'Vale 1 Bolo', emoji: '🎂', desc: 'Sem julgamentos, só felicidade!' },
    { text: 'Cochilo VIP', emoji: '😴', desc: 'Passaporte premium para aquela soneca merecida.' },
    { text: 'Dia de Rainha', emoji: '👑', desc: 'Hoje você manda em tudo (literalmente).' },
    { text: 'Café Infinito', emoji: '☕', desc: 'Energia ilimitada para conquistar o mundo.' },
    { text: 'Zero Culpa', emoji: '🍰', desc: 'Coma o que quiser. Calorias não contam hoje.' },
    { text: 'Desculpa Mágica', emoji: '✨', desc: 'Vale para qualquer coisa que você esquecer.' },
    { text: 'Parabéns Duplo', emoji: '🎉', desc: 'Você é tão especial que merece 2x mais festa!' },
    { text: 'Momento Zen', emoji: '🧘', desc: 'Permissão oficial para não fazer absolutamente nada.' },
  ];

  // Canvas
  const canvas = document.getElementById('wheelCanvas');
  const ctx = canvas.getContext('2d');
  const centerX = 210;
  const centerY = 210;
  const radius = 200;

  let currentRotation = 0;
  let isSpinning = false;
  let cheatMode = false;
  let clickCount = 0;

  // Cores elegantes
  const colors = ['#8A2BE2', '#FFD700', '#FF6B6B', '#4ECDC4', '#FFA500', '#9B59B6', '#1ABC9C', '#E74C3C'];

  function drawWheel() {
    const sliceAngle = (Math.PI * 2) / prizes.length;

    prizes.forEach((prize, i) => {
      const startAngle = currentRotation + i * sliceAngle;
      const endAngle = startAngle + sliceAngle;

      // Fatia
      ctx.beginPath();
      ctx.arc(centerX, centerY, radius, startAngle, endAngle);
      ctx.lineTo(centerX, centerY);
      ctx.fillStyle = colors[i % colors.length];
      ctx.fill();

      // Borda elegante
      ctx.strokeStyle = 'rgba(255,255,255,0.3)';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Texto
      ctx.save();
      ctx.translate(centerX, centerY);
      ctx.rotate(startAngle + sliceAngle / 2);
      ctx.textAlign = 'center';
      ctx.fillStyle = '#fff';
      ctx.font = 'bold 16px Inter';
      ctx.fillText(prize.text, radius * 0.65, 5);
      ctx.restore();
    });

    // Centro decorativo (círculo dourado)
    ctx.beginPath();
    ctx.arc(centerX, centerY, 35, 0, Math.PI * 2);
    const grad = ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, 35);
    grad.addColorStop(0, '#FFD700');
    grad.addColorStop(1, '#FFA500');
    ctx.fillStyle = grad;
    ctx.fill();
    ctx.strokeStyle = 'rgba(255,255,255,0.6)';
    ctx.lineWidth = 3;
    ctx.stroke();
  }

  drawWheel();

  // Girar roleta
  document.getElementById('spinBtn').addEventListener('click', () => {
    if (isSpinning) return;
    isSpinning = true;
    document.getElementById('spinBtn').disabled = true;

    // Criar partículas
    createParticles();

    const spins = Math.random() * 3 + 5; // 5-8 voltas
    const extraDegrees = Math.random() * 360;
    const totalRotation = spins * 360 + extraDegrees;
    const duration = 4000; // 4s
    const startTime = Date.now();
    const startRotation = currentRotation;

    function animate() {
      const elapsed = Date.now() - startTime;
      const progress = Math.min(elapsed / duration, 1);

      // Easing suave (ease-out cubic)
      const eased = 1 - Math.pow(1 - progress, 3);
      currentRotation = startRotation + totalRotation * eased * (Math.PI / 180);

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      drawWheel();

      if (progress < 1) {
        requestAnimationFrame(animate);
      } else {
        isSpinning = false;
        document.getElementById('spinBtn').disabled = false;
        showResult();
      }
    }
    animate();
  });

  // Resultado
  function showResult() {
    const sliceAngle = (Math.PI * 2) / prizes.length;
    const normalized = ((currentRotation % (Math.PI * 2)) + Math.PI * 2) % (Math.PI * 2);
    const pointerAngle = (Math.PI * 2) - normalized + (Math.PI / 2);
    let index = Math.floor(pointerAngle / sliceAngle) % prizes.length;

    // Modo trapaça: sempre prêmios bons
    if (cheatMode) {
      const goodPrizes = [0, 2, 4, 6]; // Índices dos melhores
      index = goodPrizes[Math.floor(Math.random() * goodPrizes.length)];
    }

    const prize = prizes[index];

    document.getElementById('resultEmoji').textContent = prize.emoji;
    document.getElementById('resultText').textContent = prize.text;
    document.getElementById('resultDesc').textContent = prize.desc;
    document.getElementById('resultModal').style.display = 'flex';

    // Fogos de artifício (visual extra)
    setTimeout(() => {
      createExplosion(window.innerWidth / 2, window.innerHeight / 2);
    }, 300);
  }

  // Fechar modal
  document.getElementById('closeBtn').addEventListener('click', () => {
    document.getElementById('resultModal').style.display = 'none';
  });

  // Easter egg: clicar 5x no título
  document.getElementById('titleClick').addEventListener('click', () => {
    clickCount++;
    if (clickCount === 5) {
      cheatMode = true;
      document.getElementById('cheatMode').style.display = 'block';
    }
  });

  // Partículas flutuantes
  function createParticles() {
    const container = document.getElementById('particles');
    for (let i = 0; i < 30; i++) {
      const p = document.createElement('div');
      p.className = 'particle';
      p.style.left = Math.random() * 100 + '%';
      p.style.animationDuration = (Math.random() * 3 + 2) + 's';
      p.style.animationDelay = Math.random() * 2 + 's';
      container.appendChild(p);
      setTimeout(() => p.remove(), 6000);
    }
  }

  // Explosão visual (confete)
  function createExplosion(x, y) {
    // Simulação simples de confete caindo
    const colors = ['#FFD700', '#FF6B6B', '#4ECDC4', '#8A2BE2'];
    for (let i = 0; i < 40; i++) {
      const confetti = document.createElement('div');
      confetti.style.position = 'fixed';
      confetti.style.left = x + 'px';
      confetti.style.top = y + 'px';
      confetti.style.width = '8px';
      confetti.style.height = '8px';
      confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
      confetti.style.borderRadius = '50%';
      confetti.style.pointerEvents = 'none';
      confetti.style.zIndex = '999';
      document.body.appendChild(confetti);

      const angle = Math.random() * Math.PI * 2;
      const velocity = Math.random() * 5 + 3;
      const vx = Math.cos(angle) * velocity;
      const vy = Math.sin(angle) * velocity - 5;

      let posX = x;
      let posY = y;
      let velX = vx;
      let velY = vy;

      const interval = setInterval(() => {
        posX += velX;
        posY += velY;
        velY += 0.2; // gravidade
        confetti.style.left = posX + 'px';
        confetti.style.top = posY + 'px';

        if (posY > window.innerHeight) {
          clearInterval(interval);
          confetti.remove();
        }
      }, 16);
    }
  }

</script>
</body>
</html>
""",
    height=900,
    scrolling=False,
)
