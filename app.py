import streamlit as st
import time

# Configuração da Página
st.set_page_config(
    page_title="Cosmic Journey - Lis",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS PARA O TEMA ESPACIAL ---
st.markdown("""
<style>
    /* Importando Fontes Futuristas */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Raleway:wght@300;400;600&display=swap');

    /* Remover elementos padrão do Streamlit */
    .stAppHeader, .stToolbar, #MainMenu, footer {
        visibility: hidden;
    }
    .block-container {
        padding-top: 0;
        padding-bottom: 0;
        max-width: 100%;
    }

    /* Fundo Cósmico */
    .stApp {
        background: linear-gradient(to bottom, #0a0e27 0%, #1a1147 50%, #2d1b69 100%);
        overflow-x: hidden;
    }

    /* Camada de Estrelas (3 camadas para efeito parallax) */
    .stars, .stars2, .stars3 {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
    }

    .stars {
        background: transparent url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAAEklEQVQIW2P4//+/AwMDwz8AGZYC/Wl5sLkAAAAASUVORK5CYII=') repeat;
        animation: animateStars 50s linear infinite;
        opacity: 0.5;
    }

    .stars2 {
        background: transparent url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAADCAYAAABWKLW/AAAAEklEQVQIW2P4//+/AwMDwz8AGgQC/+3iqJ4AAAAASUVORK5CYII=') repeat;
        animation: animateStars 100s linear infinite;
        opacity: 0.3;
    }

    .stars3 {
        background: transparent url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIW2P4////fwAJ+wP9BUNFygAAAABJRU5ErkJggg==') repeat;
        animation: animateStars 150s linear infinite;
        opacity: 0.7;
    }

    @keyframes animateStars {
        from { transform: translateY(0px); }
        to { transform: translateY(-2000px); }
    }

    /* Container Principal */
    .cosmic-container {
        position: relative;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 40px 20px;
        z-index: 10;
    }

    /* Título Principal com Brilho */
    .cosmic-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 80px;
        font-weight: 900;
        color: #ffffff;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 8px;
        text-shadow: 
            0 0 10px #00d9ff,
            0 0 20px #00d9ff,
            0 0 40px #00d9ff,
            0 0 80px #00d9ff;
        animation: pulse 2s ease-in-out infinite;
        margin-bottom: 20px;
    }

    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }

    /* Subtítulo */
    .cosmic-subtitle {
        font-family: 'Raleway', sans-serif;
        font-size: 24px;
        color: #00d9ff;
        text-align: center;
        letter-spacing: 4px;
        margin-bottom: 60px;
        animation: fadeIn 3s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* Cartões de Estação Espacial */
    .space-card {
        background: rgba(26, 17, 71, 0.7);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(0, 217, 255, 0.3);
        border-radius: 20px;
        padding: 50px 40px;
        margin: 40px auto;
        max-width: 700px;
        text-align: center;
        box-shadow: 0 0 30px rgba(0, 217, 255, 0.2);
        animation: slideIn 1s ease-out;
    }

    @keyframes slideIn {
        from { 
            opacity: 0; 
            transform: translateY(50px); 
        }
        to { 
            opacity: 1; 
            transform: translateY(0); 
        }
    }

    .space-card h3 {
        font-family: 'Orbitron', sans-serif;
        font-size: 32px;
        color: #00d9ff;
        margin-bottom: 25px;
        text-transform: uppercase;
        letter-spacing: 3px;
    }

    .space-card p {
        font-family: 'Raleway', sans-serif;
        font-size: 18px;
        line-height: 1.8;
        color: #e0e0e0;
        font-weight: 300;
    }

    /* Foguete Animado */
    .rocket {
        position: fixed;
        bottom: 100px;
        right: 50px;
        width: 60px;
        height: 60px;
        font-size: 60px;
        animation: float 3s ease-in-out infinite, rotate 10s linear infinite;
        z-index: 100;
        filter: drop-shadow(0 0 10px #00d9ff);
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(10deg); }
    }

    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    /* Botão Futurista */
    .stButton>button {
        background: linear-gradient(135deg, #00d9ff 0%, #5b2c6f 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 18px 50px;
        font-family: 'Orbitron', sans-serif;
        font-size: 18px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.5);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        box-shadow: 0 0 40px rgba(0, 217, 255, 0.8);
        transform: scale(1.05);
    }

    /* Planetas decorativos */
    .planet {
        position: fixed;
        border-radius: 50%;
        opacity: 0.6;
        animation: orbit 20s linear infinite;
    }

    .planet1 {
        width: 100px;
        height: 100px;
        background: radial-gradient(circle at 30% 30%, #ff6b9d, #c44569);
        top: 15%;
        right: 10%;
    }

    .planet2 {
        width: 150px;
        height: 150px;
        background: radial-gradient(circle at 30% 30%, #00d9ff, #5b2c6f);
        bottom: 20%;
        left: 8%;
        animation-duration: 30s;
    }

    @keyframes orbit {
        0% { transform: rotate(0deg) translateX(20px) rotate(0deg); }
        100% { transform: rotate(360deg) translateX(20px) rotate(-360deg); }
    }

</style>

<!-- Camadas de Estrelas -->
<div class="stars"></div>
<div class="stars2"></div>
<div class="stars3"></div>

<!-- Planetas Decorativos -->
<div class="planet planet1"></div>
<div class="planet planet2"></div>

<!-- Foguete Flutuante -->
<div class="rocket">🚀</div>

""", unsafe_allow_html=True)

# --- CONTEÚDO PRINCIPAL ---

st.markdown('<div class="cosmic-container">', unsafe_allow_html=True)

# Título Principal
st.markdown('<div class="cosmic-title">LIS</div>', unsafe_allow_html=True)
st.markdown('<div class="cosmic-subtitle">Uma Jornada Cósmica de Celebração</div>', unsafe_allow_html=True)

st.write("")

# Botão de Iniciar Jornada
col1, col2, col3 = st.columns([1,2,1])
with col2:
    start_journey = st.button("🚀 INICIAR JORNADA")

if start_journey:
    st.balloons()
    time.sleep(0.5)

st.write("")
st.write("")

# Estação 1: O Início
st.markdown("""
<div class="space-card">
    <h3>🌌 Estação 1: Origem</h3>
    <p>
    Cada jornada começa com um ponto de partida. Hoje celebramos não apenas mais um ano, 
    mas a continuída expansão do seu universo pessoal. Você é a arquiteta da sua própria galáxia.
    </p>
</div>
""", unsafe_allow_html=True)

# Estação 2: A Jornada
st.markdown("""
<div class="space-card">
    <h3>✨ Estação 2: Crescimento</h3>
    <p>
    Como estrelas que nascem de poeira cósmica, você se transforma constantemente. 
    Cada desafio superado é uma nova constelação no céu da sua história. 
    Sua luz brilha mais forte a cada ciclo.
    </p>
</div>
""", unsafe_allow_html=True)

# Estação 3: O Futuro
st.markdown("""
<div class="space-card">
    <h3>🌠 Estação 3: Infinito</h3>
    <p>
    O futuro é vasto como o cosmos. Que este novo ano lhe traga descobertas extraordinárias, 
    paz interior e a certeza de que você é capaz de alcançar qualquer horizonte. 
    <strong>Feliz Aniversário, Lis.</strong>
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# Mensagem Final Interativa
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("✨ CELEBRAR MOMENTO"):
        st.snow()
        st.success("🎉 Que a força do universo esteja sempre com você!")
        st.markdown("""
        <div style="text-align: center; font-size: 50px; margin-top: 20px; animation: fadeIn 2s;">
        🌌🚀✨🌠
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Rodapé
st.markdown("""
<div style="text-align: center; margin-top: 100px; padding: 20px; color: rgba(255,255,255,0.3); font-family: 'Raleway', sans-serif; font-size: 12px;">
    COSMIC CELEBRATION CARD • 2025 • POWERED BY IMAGINATION
</div>
""", unsafe_allow_html=True)
