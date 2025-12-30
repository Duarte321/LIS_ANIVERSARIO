import streamlit as st
import time

# Configuração da Página (Modo Wide para Cinema)
st.set_page_config(
    page_title="Celebration for Lis",
    page_icon="🥂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS & HTML PARA O TEMA PREMIUM ---
st.markdown("""
<style>
    /* Importando Fontes de Luxo */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Lato:wght@300;400&display=swap');

    /* Remover padding padrão do Streamlit para o vídeo cobrir tudo */
    .stAppHeader, .stToolbar {
        visibility: hidden;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Vídeo de Fundo */
    #myVideo {
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%; 
        min-height: 100%;
        z-index: -1;
        filter: brightness(0.4); /* Escurecer para o texto brilhar */
    }

    /* Títulos */
    h1, h2, h3 {
        font-family: 'Cinzel', serif !important;
        color: #F8F8FF;
        text-shadow: 0 0 10px rgba(0,0,0,0.8);
    }

    /* Cartão de Vidro (Glassmorphism) */
    .glass-card {
        background: rgba(20, 20, 20, 0.65);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(212, 175, 55, 0.3); /* Borda Dourada Sutil */
        border-radius: 15px;
        padding: 60px 40px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        max-width: 800px;
        margin: 0 auto;
    }

    /* Texto da Mensagem */
    .message-text {
        font-family: 'Lato', sans-serif;
        font-size: 22px;
        color: #E0E0E0;
        line-height: 1.8;
        font-weight: 300;
        margin-top: 30px;
        margin-bottom: 40px;
    }

    /* Destaque Dourado */
    .gold-text {
        color: #D4AF37; /* Dourado Metálico */
        font-weight: 700;
    }

    /* Botão Premium */
    .stButton>button {
        background: transparent;
        color: #D4AF37;
        border: 2px solid #D4AF37;
        border-radius: 2px;
        padding: 15px 40px;
        font-family: 'Cinzel', serif;
        font-size: 18px;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.4s ease;
    }
    .stButton>button:hover {
        background-color: #D4AF37;
        color: #000;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.6);
        border-color: #D4AF37;
    }

</style>

<!-- Vídeo de Fundo (Loop) -->
<video autoplay muted loop id="myVideo">
    <source src="https://player.vimeo.com/external/475960643.sd.mp4?s=e780517700687707e777f980164c8c4c74070222&profile_id=165&oauth2_token_id=57447761" type="video/mp4">
    Seu navegador não suporta HTML5 video.
</video>
""", unsafe_allow_html=True)

# --- CONTEÚDO DA PÁGINA ---

st.write("")
st.write("")

# Container Centralizado
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    # Cartão Principal
    st.markdown("""
    <div class="glass-card">
        <h1 style="font-size: 55px; margin-bottom: 10px;">LIS</h1>
        <h3 style="font-size: 18px; letter-spacing: 4px; color: #D4AF37; text-transform: uppercase;">Celebrando a Excelência</h3>
        
        <div class="message-text">
            Prezada Lis,<br><br>
            Aniversários são marcos que celebram não apenas a passagem do tempo, 
            mas a consolidação de uma história única. <br><br>
            Sua trajetória é definida pela <span class="gold-text">competência</span> e pela força serena de sua presença. 
            Que este novo ciclo lhe traga a clareza para alcançar novos horizontes 
            e a certeza de que suas conquistas são apenas o reflexo do seu mérito.<br><br>
            Com respeito e admiração,
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    # Área de Interação (O Brinde)
    # Centralizando o botão com colunas
    b1, b2, b3 = st.columns([1,2,1])
    with b2:
        if st.button("🥂 REALIZAR UM BRINDE"):
            time.sleep(0.5)
            # Toast (Notificação Elegante)
            st.toast("Um brinde à sua saúde e sucesso!", icon="🥂")
            
            # Chuva de Dourado (Substituto elegante para balões)
            st.markdown("""
            <script>
            // Aqui poderíamos injetar JS para partículas, 
            // mas usaremos o efeito nativo do Streamlit de forma sutil
            </script>
            """, unsafe_allow_html=True)
            st.balloons() # O Streamlit só tem balloons ou snow, balões brancos/amarelos combinam
            
            # Mensagem Final
            st.markdown("""
            <div style="text-align: center; margin-top: 20px; animation: fadeIn 2s;">
                <h2 style="color: #D4AF37; font-size: 30px;">Felicidades.</h2>
            </div>
            """, unsafe_allow_html=True)

# Rodapé Discreto
st.markdown("""
<div style="position: fixed; bottom: 10px; width: 100%; text-align: center; color: rgba(255,255,255,0.3); font-family: 'Lato', sans-serif; font-size: 10px;">
    PRIVATE CELEBRATION CARD • MMXXV
</div>
""", unsafe_allow_html=True)
