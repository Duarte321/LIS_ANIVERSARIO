import streamlit as st
import time

# Configuração da Página
st.set_page_config(
    page_title="Parabéns Lis! 🤠",
    page_icon="🌽",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS para Efeitos 3D e Cores Vibrantes (Sem Rosa!)
st.markdown("""
<style>
    /* Fundo vibrante (Verde Roça Tech) */
    .stApp {
        background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%);
        color: white;
    }
    
    /* Título 3D */
    .title-3d {
        font-family: 'Arial Black', sans-serif;
        font-size: 60px;
        color: #FFC107; /* Amarelo Ouro */
        text-align: center;
        text-transform: uppercase;
        transform: perspective(500px) rotateX(10deg);
        text-shadow: 
            0 1px 0 #c69c06,
            0 2px 0 #b68f05,
            0 3px 0 #a58204,
            0 4px 0 #947503,
            0 5px 0 #836702,
            0 6px 1px rgba(0,0,0,.1),
            0 0 5px rgba(0,0,0,.1),
            0 1px 3px rgba(0,0,0,.3),
            0 3px 5px rgba(0,0,0,.2),
            0 5px 10px rgba(0,0,0,.25),
            0 10px 10px rgba(0,0,0,.2),
            0 20px 20px rgba(0,0,0,.15);
        animation: float 3s ease-in-out infinite;
    }

    /* Animação de Flutuar */
    @keyframes float {
        0% { transform: perspective(500px) rotateX(10deg) translateY(0px); }
        50% { transform: perspective(500px) rotateX(10deg) translateY(-15px); }
        100% { transform: perspective(500px) rotateX(10deg) translateY(0px); }
    }

    /* Cubo 3D (CSS Puro) */
    .scene {
        width: 200px;
        height: 200px;
        perspective: 600px;
        margin: 50px auto;
    }
    .cube {
        width: 100%;
        height: 100%;
        position: relative;
        transform-style: preserve-3d;
        animation: spin 5s infinite linear;
    }
    .cube-face {
        position: absolute;
        width: 200px;
        height: 200px;
        border: 2px solid black;
        line-height: 200px;
        font-size: 80px;
        font-weight: bold;
        color: white;
        text-align: center;
        opacity: 0.9;
    }
    .front  { background: hsla(  0, 100%, 50%, 0.7); transform: rotateY(  0deg) translateZ(100px); }
    .right  { background: hsla( 60, 100%, 50%, 0.7); transform: rotateY( 90deg) translateZ(100px); }
    .back   { background: hsla(120, 100%, 50%, 0.7); transform: rotateY(180deg) translateZ(100px); }
    .left   { background: hsla(180, 100%, 50%, 0.7); transform: rotateY(-90deg) translateZ(100px); }
    .top    { background: hsla(240, 100%, 50%, 0.7); transform: rotateX( 90deg) translateZ(100px); }
    .bottom { background: hsla(300, 100%, 50%, 0.7); transform: rotateX(-90deg) translateZ(100px); }

    @keyframes spin {
        0% { transform: rotateX(0deg) rotateY(0deg); }
        100% { transform: rotateX(360deg) rotateY(360deg); }
    }

    /* Cartão da Mensagem */
    .funny-card {
        background-color: #FFF3E0; /* Laranja clarinho */
        color: #E65100;
        border-radius: 15px;
        padding: 20px;
        border: 4px solid #FF9800;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        box-shadow: 10px 10px 0px #3E2723; /* Sombra dura estilo cartoon */
        transform: rotate(-1deg);
        transition: transform 0.3s;
    }
    .funny-card:hover {
        transform: rotate(1deg) scale(1.02);
    }

    /* Botãozão */
    .stButton>button {
        background-color: #FF5722;
        color: white;
        font-size: 24px;
        font-weight: bold;
        border-radius: 10px;
        border: 4px solid #BF360C;
        box-shadow: 0 9px #999;
    }
    .stButton>button:active {
        box-shadow: 0 5px #666;
        transform: translateY(4px);
    }
</style>
""", unsafe_allow_html=True)

# Título 3D Flutuante
st.markdown('<div class="title-3d">FELIZ NIVER<br>LIS! 🚜</div>', unsafe_allow_html=True)

# Cubo 3D Giratório
st.markdown("""
<div class="scene">
  <div class="cube">
    <div class="cube-face front">🤠</div>
    <div class="cube-face back">🌽</div>
    <div class="cube-face right">🎉</div>
    <div class="cube-face left">🎂</div>
    <div class="cube-face top">🐮</div>
    <div class="cube-face bottom">🔥</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.write("")

# Abas simplificadas (Sem playlist, sem vídeo)
tab1, tab2 = st.tabs(["😂 A Realidade", "🎁 O Presente"])

with tab1:
    st.write("")
    st.markdown("""
    <div class="funny-card">
    Ô Lis, parabéns!!! 👏👏<br><br>
    Fiquei sabendo que você não tá ficando velha...<br>
    Você só tá virando um clássico sertanejo! Quanto mais o tempo passa, mais o povo gosta! 📻<br><br>
    Dizem que a sabedoria vem com a idade...<br>
    Pelo jeito, esse ano você já ganha o prêmio Nobel da Roça!<br><br>
    Aproveita que hoje pode tudo: comer bolo, pão de queijo e até culpar a idade se esquecer de pagar alguma conta.<br><br>
    <b>Tudo de bão pro cê!</b> 
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.write("")
    st.markdown("<h3 style='text-align: center; color: #FFC107;'>CUIDADO: Efeitos de alta tecnologia da roça abaixo</h3>", unsafe_allow_html=True)
    
    if st.button("NÃO CLIQUE AQUI 🚫"):
        # Efeito Caótico Divertido
        st.balloons()
        time.sleep(0.5)
        st.error("EU FALEI PRA NÃO CLICAR! AGORA TOMA ESSE PARABÉNS!")
        time.sleep(1)
        st.success("BRINCADEIRA! 🤣 FELICIDADES MIL!")
        st.markdown("""
        <h1 style='text-align: center; font-size: 80px;'>🐄💨</h1>
        <p style='text-align: center;'>A vaca foi pro brejo... de alegria!</p>
        """, unsafe_allow_html=True)

# Rodapé
st.write("---")
st.markdown("<div style='text-align: center; font-size: 12px;'>Tecnologia Agro-Espacial 🚀🌽</div>", unsafe_allow_html=True)
