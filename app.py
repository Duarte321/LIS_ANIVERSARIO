import streamlit as st
import streamlit.components.v1 as components
import time

# Configuração da Página
st.set_page_config(
    page_title="Parabéns Lis! 🎂",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS para Efeitos 3D, Bolo Animado e Título com Efeitos
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%);
        color: white;
    }
    
    /* Título Animado com Múltiplos Efeitos */
    .title-animated {
        font-family: 'Arial Black', sans-serif;
        font-size: 60px;
        text-align: center;
        text-transform: uppercase;
        background: linear-gradient(45deg, #FFC107, #FF5722, #FFC107);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientShift 3s ease infinite, bounce 2s ease-in-out infinite;
        text-shadow: 0 0 20px rgba(255,193,7,0.5);
        filter: drop-shadow(0 0 10px #FFC107);
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }

    /* Container do Bolo */
    .cake-container {
        position: relative;
        width: 300px;
        height: 350px;
        margin: 50px auto;
        cursor: pointer;
    }

    /* Camadas do Bolo (Animadas) */
    .cake-layer {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        border-radius: 10px;
        animation: buildCake 1s ease-out forwards;
        opacity: 0;
    }

    .layer-1 {
        bottom: 0;
        width: 250px;
        height: 80px;
        background: linear-gradient(180deg, #8D6E63 0%, #6D4C41 100%);
        animation-delay: 0s;
    }

    .layer-2 {
        bottom: 80px;
        width: 200px;
        height: 70px;
        background: linear-gradient(180deg, #A1887F 0%, #8D6E63 100%);
        animation-delay: 0.3s;
    }

    .layer-3 {
        bottom: 150px;
        width: 150px;
        height: 60px;
        background: linear-gradient(180deg, #BCAAA4 0%, #A1887F 100%);
        animation-delay: 0.6s;
    }

    @keyframes buildCake {
        from {
            opacity: 0;
            transform: translateX(-50%) translateY(50px) scale(0.5);
        }
        to {
            opacity: 1;
            transform: translateX(-50%) translateY(0) scale(1);
        }
    }

    /* Velas */
    .candle {
        position: absolute;
        width: 10px;
        height: 50px;
        background: linear-gradient(180deg, #FF6B6B 0%, #EE5A6F 100%);
        border-radius: 5px;
        bottom: 210px;
        opacity: 0;
        transition: opacity 0.3s;
    }

    .candle.active {
        opacity: 1;
        animation: candleWiggle 0.5s ease-out;
    }

    @keyframes candleWiggle {
        0%, 100% { transform: translateX(-50%) rotate(0deg); }
        25% { transform: translateX(-50%) rotate(-5deg); }
        75% { transform: translateX(-50%) rotate(5deg); }
    }

    .candle-1 { left: 35%; }
    .candle-2 { left: 45%; }
    .candle-3 { left: 55%; }
    .candle-4 { left: 65%; }

    /* Chamas */
    .flame {
        position: absolute;
        top: -20px;
        left: 50%;
        transform: translateX(-50%);
        width: 15px;
        height: 25px;
        background: radial-gradient(circle, #FFF59D 0%, #FFD54F 40%, #FF6F00 100%);
        border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
        animation: flicker 0.3s infinite alternate;
    }

    .flame.blown {
        animation: blowOut 0.5s forwards;
    }

    @keyframes flicker {
        0% { transform: translateX(-50%) scale(1) translateY(0); }
        100% { transform: translateX(-50%) scale(1.1) translateY(-3px); }
    }

    @keyframes blowOut {
        to {
            opacity: 0;
            transform: translateX(-50%) scale(0.3) translateY(-30px);
        }
    }

    .funny-card {
        background-color: #FFF3E0;
        color: #E65100;
        border-radius: 15px;
        padding: 20px;
        border: 4px solid #FF9800;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        box-shadow: 10px 10px 0px #3E2723;
    }
</style>
""", unsafe_allow_html=True)

# Título com Efeitos
st.markdown('<div class="title-animated">PARABÉNS<br>LIS! 🎉</div>', unsafe_allow_html=True)

st.write("")
st.markdown("<h3 style='text-align: center; color: #FFC107;'>☝️ Clique no bolo pra colocar as velas!</h3>", unsafe_allow_html=True)

# Bolo Interativo com Velas
components.html("""
<div class="cake-container" id="cakeArea">
    <div class="cake-layer layer-1"></div>
    <div class="cake-layer layer-2"></div>
    <div class="cake-layer layer-3"></div>
    
    <div class="candle candle-1" id="candle1">
        <div class="flame" id="flame1"></div>
    </div>
    <div class="candle candle-2" id="candle2">
        <div class="flame" id="flame2"></div>
    </div>
    <div class="candle candle-3" id="candle3">
        <div class="flame" id="flame3"></div>
    </div>
    <div class="candle candle-4" id="candle4">
        <div class="flame" id="flame4"></div>
    </div>
</div>

<div id="blowMessage" style="text-align: center; color: #FFC107; font-size: 24px; margin-top: 20px;"></div>

<script>
    // Adicionar velas ao clicar
    const cakeArea = document.getElementById('cakeArea');
    const candles = [1, 2, 3, 4];
    let candlesLit = false;

    cakeArea.addEventListener('click', function() {
        if (!candlesLit) {
            candles.forEach(num => {
                document.getElementById('candle' + num).classList.add('active');
            });
            candlesLit = true;
            document.getElementById('blowMessage').innerHTML = '💨 Agora sopre o microfone (clique no botão abaixo)!';
        }
    });

    // Função para apagar velas (chamada pelo botão)
    window.blowCandles = function() {
        if (candlesLit) {
            candles.forEach(num => {
                const flame = document.getElementById('flame' + num);
                flame.classList.add('blown');
            });
            setTimeout(() => {
                document.getElementById('blowMessage').innerHTML = '🎉🎉 PARABÉNS, LIS!!! 🎉🎉';
            }, 500);
        } else {
            document.getElementById('blowMessage').innerHTML = '⚠️ Primeiro clique no bolo pra acender as velas!';
        }
    };
</script>

<style>
    .stApp {
        background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%);
    }
    .cake-container {
        position: relative;
        width: 300px;
        height: 350px;
        margin: 50px auto;
        cursor: pointer;
    }
    .cake-layer {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        border-radius: 10px;
        animation: buildCake 1s ease-out forwards;
        opacity: 0;
    }
    .layer-1 {
        bottom: 0;
        width: 250px;
        height: 80px;
        background: linear-gradient(180deg, #8D6E63 0%, #6D4C41 100%);
        animation-delay: 0s;
    }
    .layer-2 {
        bottom: 80px;
        width: 200px;
        height: 70px;
        background: linear-gradient(180deg, #A1887F 0%, #8D6E63 100%);
        animation-delay: 0.3s;
    }
    .layer-3 {
        bottom: 150px;
        width: 150px;
        height: 60px;
        background: linear-gradient(180deg, #BCAAA4 0%, #A1887F 100%);
        animation-delay: 0.6s;
    }
    @keyframes buildCake {
        from {
            opacity: 0;
            transform: translateX(-50%) translateY(50px) scale(0.5);
        }
        to {
            opacity: 1;
            transform: translateX(-50%) translateY(0) scale(1);
        }
    }
    .candle {
        position: absolute;
        width: 10px;
        height: 50px;
        background: linear-gradient(180deg, #FF6B6B 0%, #EE5A6F 100%);
        border-radius: 5px;
        bottom: 210px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    .candle.active {
        opacity: 1;
        animation: candleWiggle 0.5s ease-out;
    }
    @keyframes candleWiggle {
        0%, 100% { transform: translateX(-50%) rotate(0deg); }
        25% { transform: translateX(-50%) rotate(-5deg); }
        75% { transform: translateX(-50%) rotate(5deg); }
    }
    .candle-1 { left: 35%; }
    .candle-2 { left: 45%; }
    .candle-3 { left: 55%; }
    .candle-4 { left: 65%; }
    .flame {
        position: absolute;
        top: -20px;
        left: 50%;
        transform: translateX(-50%);
        width: 15px;
        height: 25px;
        background: radial-gradient(circle, #FFF59D 0%, #FFD54F 40%, #FF6F00 100%);
        border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
        animation: flicker 0.3s infinite alternate;
    }
    .flame.blown {
        animation: blowOut 0.5s forwards;
    }
    @keyframes flicker {
        0% { transform: translateX(-50%) scale(1) translateY(0); }
        100% { transform: translateX(-50%) scale(1.1) translateY(-3px); }
    }
    @keyframes blowOut {
        to {
            opacity: 0;
            transform: translateX(-50%) scale(0.3) translateY(-30px);
        }
    }
</style>
""", height=500)

st.write("")

# Botão para "Soprar"
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("💨 SOPRAR AS VELAS 💨", use_container_width=True):
        st.balloons()
        components.html("""
        <script>
            if (window.parent.blowCandles) {
                window.parent.blowCandles();
            }
        </script>
        """, height=0)
        st.success("🎉 PARABÉNS, LIS! QUE TODOS OS SEUS SONHOS SE REALIZEM! 🎉")
        time.sleep(1)
        st.markdown("""
        <div style='text-align: center; font-size: 60px;'>
        🎂🎈🎁
        </div>
        """, unsafe_allow_html=True)

st.write("")

# Mensagem Engraçada
with st.expander("😂 Mensagem Especial (Clique aqui)"):
    st.markdown("""
    <div class="funny-card">
    Ô Lis, parabéns!!! 👏<br><br>
    Fiquei sabendo que você não tá ficando velha...<br>
    Você só tá virando um clássico sertanejo! Quanto mais o tempo passa, mais o povo gosta! 📻<br><br>
    Aproveita que hoje pode tudo: comer bolo, pão de queijo e até culpar a idade se esquecer de pagar alguma conta!<br><br>
    <b>Felicidades e muita saúde, Cowgirl! 🤠</b>
    </div>
    """, unsafe_allow_html=True)

# Rodapé
st.write("---")
st.markdown("<div style='text-align: center; font-size: 12px; color: #FFC107;'>Feito com carinho e Python 🐍✨</div>", unsafe_allow_html=True)
