import streamlit as st
import time
from datetime import date

# Configuração da Página
st.set_page_config(
    page_title="Parabéns, Lis!",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilização CSS Personalizada
st.markdown("""
<style>
    /* Fundo festivo */
    .stApp {
        background-image: linear-gradient(to right top, #fce4ec, #f8bbd0, #f48fb1);
    }
    
    /* Título Principal */
    .title-text {
        font-size: 60px !important;
        color: #880E4F;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-weight: 900;
        text-shadow: 2px 2px 4px #ce93d8;
        animation: glow 1s ease-in-out infinite alternate;
    }
    
    /* Animação do Texto */
    @keyframes glow {
        from {
            text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #e60073;
        }
        to {
            text-shadow: 0 0 20px #fff, 0 0 30px #ff4da6, 0 0 40px #ff4da6;
        }
    }

    /* Cartão de Mensagem */
    .message-card {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        font-size: 22px;
        color: #4A148C;
        margin-bottom: 20px;
    }

    /* Botão Personalizado */
    .stButton>button {
        background-color: #AD1457;
        color: white;
        border-radius: 50px;
        padding: 15px 30px;
        font-size: 20px;
        border: none;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #880E4F;
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# Função para efeito de digitação
def typing_effect(text, speed=0.05):
    placeholder = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(f'<div class="message-card">{displayed_text}▌</div>', unsafe_allow_html=True)
        time.sleep(speed)
    placeholder.markdown(f'<div class="message-card">{displayed_text}</div>', unsafe_allow_html=True)

# Cabeçalho
st.markdown('<p class="title-text">🎉 Feliz Aniversário, Lis! 🎉</p>', unsafe_allow_html=True)

# Imagem de Capa (Placeholder - Substituir por foto real depois)
# Dica: Substitua o link abaixo por uma foto dela no GitHub
st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbm90eHhidjF6Ym14Y3Z5eW94YzF6Ym14Y3Z5eW94YzF6Ym14YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LfpjDCLnTeHYA/giphy.gif", caption="Um dia brilhante para uma pessoa brilhante!", use_column_width=True)

st.write("") # Espaçamento

# Conteúdo Interativo
tab1, tab2, tab3 = st.tabs(["💌 Mensagem", "🎁 Surpresa", "🎶 Playlist"])

with tab1:
    st.write("")
    st.markdown("""
    <div class="message-card">
    Hoje o dia amanheceu mais bonito porque é o seu dia! 🌟<br><br>
    Que este novo ciclo seja repleto de conquistas, sorrisos fáceis, 
    viagens inesquecíveis e momentos que aquecem o coração.<br><br>
    Você merece toda a felicidade do mundo!
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.write("")
    st.markdown("<h3 style='text-align: center; color: #880E4F;'>Tem um presente especial esperando...</h3>", unsafe_allow_html=True)
    if st.button("🎂 ASSOPRAR AS VELAS 🎂"):
        st.balloons()
        st.snow()
        st.success("🎈✨ PARABÉNS!!! QUE SEUS DESEJOS SE REALIZEM! ✨🎈")
        # Aqui viria um áudio se o Streamlit suportasse autoplay nativo fácil, 
        # mas visualmente os balões já dão o impacto!
        time.sleep(1)
        st.markdown("""
        <div style='text-align: center; font-size: 50px;'>
        👏👏👏👏👏👏👏👏
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.write("")
    st.info("Dê o play na trilha sonora do seu dia! (Exemplo do Spotify)")
    # Embed do Spotify (Substituir pelo link da playlist dela)
    st.components.v1.iframe("https://open.spotify.com/embed/playlist/37i9dQZF1DX1Nw33e9d7dO?utm_source=generator", height=380)

# Rodapé
st.write("---")
st.markdown("<div style='text-align: center; color: gray;'>Feito com ❤️ e Python</div>", unsafe_allow_html=True)
