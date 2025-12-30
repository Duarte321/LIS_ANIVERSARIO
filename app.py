import streamlit as st
import time

# Configuração da Página
st.set_page_config(
    page_title="Parabéns da Roça pra Lis! 🤠",
    page_icon="🌻",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilização CSS Personalizada (Tema Country/Rústico)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Rye&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Courier+Prime&display=swap');

    /* Fundo estilo madeira/rústico */
    .stApp {
        background-color: #f4e1d2;
        background-image: radial-gradient(#d7ccc8 1px, transparent 1px), radial-gradient(#d7ccc8 1px, transparent 1px);
        background-size: 20px 20px;
        background-position: 0 0, 10px 10px;
    }
    
    /* Título Principal */
    .title-text {
        font-family: 'Rye', serif;
        font-size: 50px !important;
        color: #5D4037; /* Marrom café */
        text-align: center;
        text-shadow: 2px 2px 0px #D7CCC8;
        margin-bottom: 20px;
    }
    
    /* Cartão de Mensagem (estilo papel antigo) */
    .message-card {
        background-color: #fff8e1;
        border: 2px dashed #8d6e63;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        text-align: center;
        font-size: 20px;
        color: #4e342e;
        font-family: 'Courier Prime', monospace;
    }

    /* Botão Personalizado (estilo couro/madeira) */
    .stButton>button {
        background-color: #795548;
        color: #fff8e1;
        border: 2px solid #3e2723;
        border-radius: 8px;
        padding: 15px 30px;
        font-family: 'Rye', serif;
        font-size: 22px;
        width: 100%;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        background-color: #5d4037;
        color: white;
        transform: scale(1.02);
        border-color: #fff;
    }
    
    /* Estilo das Abas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #efebe9;
        border-radius: 4px;
        color: #5d4037;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #8d6e63;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown('<p class="title-text">🤠 Feliz Aniversário, Lis! 🌻</p>', unsafe_allow_html=True)

# Imagem de Capa (Tema Country/Festa)
# Dica: Substitua por uma foto dela com chapéu ou na fazenda!
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExam95OHJ0ZGd6ZmF4Z3F6Z3F6Z3F6Z3F6Z3F6Z3F6Z3F6ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LfpjDCLnTeHYA/giphy.gif", caption="Hoje o dia é todo seu, cowgirl!", use_column_width=True)

st.write("") 

# Conteúdo Interativo
tab1, tab2, tab3 = st.tabs(["📝 Prosa Boa", "🎁 Presente", "🎸 Modão Sertanejo"])

with tab1:
    st.write("")
    st.markdown("""
    <div class="message-card">
    <b>Minha querida Lis,</b><br><br>
    Hoje a porteira da felicidade se abriu de par em par pra você! 🌾<br><br>
    Que seu novo ano seja firme igual palanque de aroeira e doce igual compota de vó.
    Que não falte café quente, conversa boa e gente de verdade ao seu lado.<br><br>
    Você tem a força da terra e o brilho do sol. 
    <b>Parabéns por ser essa mulher de fibra!</b><br><br>
    🤠 ❤️ 🐎
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.write("")
    st.markdown("<h3 style='text-align: center; color: #5D4037; font-family: Rye;'>Segura peão, que tem surpresa!</h3>", unsafe_allow_html=True)
    if st.button("💥 SOLTAR OS FOGUETE 💥"):
        st.balloons()
        st.success("🎉 ÊTA LIS! MUITA SAÚDE, PAZ E ALEGRIA! 🎉")
        time.sleep(1)
        st.markdown("""
        <div style='text-align: center; font-size: 24px; color: #4e342e; margin-top: 20px;'>
        🐎 🐄 🚜 🌽 🐓<br>
        <i>A fazenda inteira tá em festa pro cê!</i>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.write("")
    st.info("Aumenta o som que agora é hora do modão apaixonado!")
    # Playlist Sertanejo Raiz/Modão (Link do Spotify)
    st.components.v1.iframe("https://open.spotify.com/embed/playlist/37i9dQZF1DX0f93dbd2b9o?utm_source=generator", height=380)

# Rodapé
st.write("---")
st.markdown("<div style='text-align: center; color: #6d4c41;'>Feito com carinho e Python 🐍🤠</div>", unsafe_allow_html=True)
