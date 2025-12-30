import streamlit as st
import time

# Configuração da Página
st.set_page_config(
    page_title="Para Lis ♡",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS TEMA VINTAGE BOTANICAL ---
st.markdown("""
<style>
    /* Importando Fontes */
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Playfair+Display:wght@400;600;700&family=Crimson+Text:wght@400;600&display=swap');

    /* Ocultar elementos Streamlit */
    .stAppHeader, .stToolbar, #MainMenu, footer {
        visibility: hidden;
    }

    /* Fundo Papel Antigo */
    .stApp {
        background-color: #f5f1e8;
        background-image: 
            repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,.02) 2px, rgba(0,0,0,.02) 4px),
            repeating-linear-gradient(90deg, transparent, transparent 2px, rgba(0,0,0,.02) 2px, rgba(0,0,0,.02) 4px);
    }

    .block-container {
        padding: 3rem 1rem;
        max-width: 750px;
    }

    /* Container Principal (Cartão Postal) */
    .postcard-container {
        background: linear-gradient(135deg, #fdfbf7 0%, #f5f1e8 100%);
        border: 12px solid #8b9d83;
        border-radius: 3px;
        padding: 60px 50px;
        box-shadow: 
            0 10px 30px rgba(0,0,0,0.15),
            inset 0 0 100px rgba(139, 157, 131, 0.05);
        position: relative;
        margin: 40px auto;
    }

    /* Selo Vintage (Canto Superior Direito) */
    .stamp {
        position: absolute;
        top: 20px;
        right: 20px;
        width: 80px;
        height: 100px;
        background: linear-gradient(135deg, #d4a5a5 0%, #b88b8b 100%);
        border: 3px dashed #5d4e37;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 40px;
        transform: rotate(15deg);
        opacity: 0.9;
    }

    /* Lacre de Cera */
    .wax-seal {
        position: absolute;
        bottom: -30px;
        right: 50px;
        width: 70px;
        height: 70px;
        background: radial-gradient(circle, #a52a2a 0%, #8b1a1a 100%);
        border-radius: 50%;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        animation: sealPulse 2s ease-in-out infinite;
    }

    @keyframes sealPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }

    /* Bordas Florais */
    .floral-corner {
        position: absolute;
        font-size: 50px;
        opacity: 0.6;
        color: #8b9d83;
    }
    .corner-tl { top: 10px; left: 10px; }
    .corner-tr { top: 10px; right: 10px; transform: scaleX(-1); }
    .corner-bl { bottom: 10px; left: 10px; transform: scaleY(-1); }
    .corner-br { bottom: 10px; right: 10px; transform: scale(-1); }

    /* Título Manuscrito */
    .handwritten-title {
        font-family: 'Dancing Script', cursive;
        font-size: 65px;
        color: #5d4e37;
        text-align: center;
        margin-bottom: 10px;
        font-weight: 700;
        text-shadow: 2px 2px 0px rgba(139, 157, 131, 0.2);
    }

    /* Subtítulo */
    .subtitle {
        font-family: 'Crimson Text', serif;
        font-size: 20px;
        color: #8b9d83;
        text-align: center;
        font-style: italic;
        margin-bottom: 40px;
        letter-spacing: 2px;
    }

    /* Texto da Carta */
    .letter-text {
        font-family: 'Crimson Text', serif;
        font-size: 19px;
        line-height: 1.9;
        color: #3d3d3d;
        text-align: justify;
        margin-bottom: 30px;
        text-indent: 40px;
    }

    .letter-text strong {
        color: #a52a2a;
        font-weight: 600;
    }

    /* Assinatura */
    .signature {
        font-family: 'Dancing Script', cursive;
        font-size: 32px;
        color: #5d4e37;
        text-align: right;
        margin-top: 40px;
        font-weight: 400;
    }

    /* Envelope (Para Interação) */
    .envelope-container {
        text-align: center;
        margin: 50px 0;
    }

    .envelope {
        display: inline-block;
        width: 200px;
        height: 130px;
        background: #e8dcc4;
        border: 2px solid #8b9d83;
        position: relative;
        box-shadow: 0 5px 20px rgba(0,0,0,0.2);
    }

    .envelope:before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 0;
        height: 0;
        border-left: 100px solid transparent;
        border-right: 100px solid transparent;
        border-top: 65px solid #d4a5a5;
    }

    /* Botão Vintage */
    .stButton>button {
        background-color: #8b9d83;
        color: #fdfbf7;
        border: 2px solid #5d4e37;
        border-radius: 3px;
        padding: 15px 40px;
        font-family: 'Playfair Display', serif;
        font-size: 18px;
        font-weight: 600;
        letter-spacing: 1px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #5d4e37;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }

    /* Divider Floral */
    .floral-divider {
        text-align: center;
        font-size: 30px;
        color: #8b9d83;
        margin: 30px 0;
        opacity: 0.5;
    }

</style>
""", unsafe_allow_html=True)

# --- CONTEÚDO ---

# Envelope (Intro)
envelope_opened = False

st.markdown('<div class="envelope-container">', unsafe_allow_html=True)
st.markdown('<div class="envelope"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.write("")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("💌 Abrir Envelope"):
        envelope_opened = True
        st.balloons()

if envelope_opened:
    time.sleep(0.5)
    
    # Cartão Postal
    st.markdown("""
    <div class="postcard-container">
        <!-- Selo -->
        <div class="stamp">🌺</div>
        
        <!-- Lacre de Cera -->
        <div class="wax-seal">♡</div>
        
        <!-- Cantos Florais -->
        <div class="floral-corner corner-tl">🌿</div>
        <div class="floral-corner corner-tr">🌿</div>
        <div class="floral-corner corner-bl">🌿</div>
        <div class="floral-corner corner-br">🌿</div>
        
        <!-- Conteúdo -->
        <div class="handwritten-title">Querida Lis,</div>
        <div class="subtitle">Em um dia tão especial</div>
        
        <div class="floral-divider">❀ ❀ ❀</div>
        
        <p class="letter-text">
        Escrevo estas palavras com o coração cheio de gratidão por ter você em minha vida. 
        Seu aniversário é um lembrete de que <strong>pessoas especiais merecem celebrações igualmente especiais</strong>.
        </p>
        
        <p class="letter-text">
        Que este novo ciclo lhe traga a serenidade de um jardim em flor, a força das raízes profundas 
        e a beleza das pétalas que se abrem ao sol. Que cada dia seja repleto de pequenos milagres 
        e grandes razões para sorrir.
        </p>
        
        <p class="letter-text">
        Você ilumina o mundo ao seu redor com sua presença única. 
        Continue sendo essa <strong>pessoa extraordinária</strong> que tanto admiramos.
        </p>
        
        <div class="floral-divider">✿</div>
        
        <div class="signature">Com carinho e os melhores votos,<br>Seu admirador secretário ♡</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    # Botão Final
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🌸 Guardar no Coração"):
            st.success("✨ Mensagem guardada com carinho! Feliz Aniversário, Lis!")
            st.markdown('<div style="text-align: center; font-size: 50px; margin-top: 20px;">🌻🌺🌹</div>', unsafe_allow_html=True)

else:
    st.markdown('<div style="text-align: center; color: #5d4e37; font-family: \'Crimson Text\', serif; font-size: 20px; margin-top: 20px;">Há uma mensagem especial esperando por você...</div>', unsafe_allow_html=True)

# Rodapé
st.write("")
st.write("")
st.markdown("""
<div style="text-align: center; margin-top: 60px; color: rgba(93, 78, 55, 0.4); font-family: 'Crimson Text', serif; font-size: 12px;">
    Handcrafted with love • 2025
</div>
""", unsafe_allow_html=True)
