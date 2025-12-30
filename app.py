import streamlit as st
import time

st.set_page_config(
    page_title="Lis • Art Déco Card",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Estado
if "opened" not in st.session_state:
    st.session_state.opened = False

# Tema Art Déco (Premium, sem vídeo)
st.markdown(
    """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500&display=swap');

  /* Limpa elementos */
  .stAppHeader, .stToolbar, #MainMenu, footer { visibility: hidden; }

  /* Fundo Art Déco (padrão geométrico animado) */
  .stApp {
    background:
      radial-gradient(1200px circle at 20% 10%, rgba(212,175,55,0.14), transparent 55%),
      radial-gradient(900px circle at 80% 30%, rgba(212,175,55,0.10), transparent 50%),
      linear-gradient(180deg, #07070a 0%, #0c0c12 100%);
    color: #f4f4f6;
  }

  .deco-grid {
    position: fixed;
    inset: 0;
    pointer-events: none;
    background:
      linear-gradient(90deg, rgba(212,175,55,0.06) 1px, transparent 1px),
      linear-gradient(0deg, rgba(212,175,55,0.06) 1px, transparent 1px);
    background-size: 64px 64px;
    mask-image: radial-gradient(600px circle at 50% 35%, rgba(0,0,0,1), rgba(0,0,0,0));
    animation: gridFloat 10s ease-in-out infinite;
    opacity: 0.65;
  }

  @keyframes gridFloat {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
  }

  /* Moldura Art Déco */
  .frame {
    border: 1px solid rgba(212,175,55,0.35);
    border-radius: 18px;
    padding: 26px;
    background: rgba(16,16,22,0.65);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 18px 60px rgba(0,0,0,0.55);
    position: relative;
    overflow: hidden;
  }

  .frame:before {
    content: "";
    position: absolute;
    inset: -2px;
    background: conic-gradient(from 180deg, transparent, rgba(212,175,55,0.45), transparent);
    filter: blur(18px);
    opacity: 0.35;
    animation: halo 6s linear infinite;
  }

  @keyframes halo {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  .frame > * { position: relative; z-index: 1; }

  .kicker {
    font-family: 'Inter', sans-serif;
    letter-spacing: 0.28em;
    text-transform: uppercase;
    color: rgba(212,175,55,0.95);
    font-size: 12px;
    text-align: center;
    margin-bottom: 14px;
  }

  .title {
    font-family: 'Playfair Display', serif;
    font-size: 52px;
    text-align: center;
    margin: 0;
    line-height: 1.05;
  }

  .subtitle {
    font-family: 'Inter', sans-serif;
    text-align: center;
    color: rgba(244,244,246,0.80);
    margin-top: 10px;
    font-size: 16px;
  }

  .divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(212,175,55,0.6), transparent);
    margin: 22px 0;
  }

  .body {
    font-family: 'Inter', sans-serif;
    font-size: 17px;
    line-height: 1.85;
    color: rgba(244,244,246,0.86);
  }

  .sig {
    margin-top: 18px;
    font-family: 'Playfair Display', serif;
    font-size: 18px;
    color: rgba(212,175,55,0.95);
    text-align: right;
  }

  /* Botões */
  .stButton>button {
    width: 100%;
    background: transparent;
    color: rgba(212,175,55,0.98);
    border: 1px solid rgba(212,175,55,0.65);
    border-radius: 999px;
    padding: 14px 18px;
    font-family: 'Inter', sans-serif;
    letter-spacing: 0.10em;
    text-transform: uppercase;
    transition: all .25s ease;
  }
  .stButton>button:hover {
    background: rgba(212,175,55,0.10);
    border-color: rgba(212,175,55,0.95);
    box-shadow: 0 0 26px rgba(212,175,55,0.18);
    transform: translateY(-1px);
  }

  /* Selo "Premium" */
  .seal {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 78px;
    height: 78px;
    border-radius: 50%;
    margin: 14px auto 0;
    border: 1px solid rgba(212,175,55,0.75);
    color: rgba(212,175,55,0.95);
    font-family: 'Inter', sans-serif;
    letter-spacing: 0.18em;
    font-size: 11px;
    text-transform: uppercase;
    background: radial-gradient(circle at 30% 30%, rgba(212,175,55,0.18), rgba(0,0,0,0));
    box-shadow: inset 0 0 18px rgba(212,175,55,0.18);
  }

  .sealWrap { text-align:center; }

  /* Confete elegante (CSS) */
  .spark {
    position: fixed;
    inset: 0;
    pointer-events: none;
    overflow: hidden;
    z-index: 0;
  }

  .spark i {
    position: absolute;
    top: -10vh;
    width: 2px;
    height: 12vh;
    background: linear-gradient(180deg, rgba(212,175,55,0), rgba(212,175,55,0.55), rgba(212,175,55,0));
    opacity: 0.35;
    animation: fall linear infinite;
  }

  @keyframes fall {
    to { transform: translateY(120vh); }
  }
</style>

<div class="deco-grid"></div>

<div class="spark">
  <i style="left: 10%; animation-duration: 3.8s; animation-delay: 0.2s;"></i>
  <i style="left: 22%; animation-duration: 4.6s; animation-delay: 1.1s;"></i>
  <i style="left: 35%; animation-duration: 5.2s; animation-delay: 0.6s;"></i>
  <i style="left: 48%; animation-duration: 4.1s; animation-delay: 1.7s;"></i>
  <i style="left: 60%; animation-duration: 5.8s; animation-delay: 0.9s;"></i>
  <i style="left: 73%; animation-duration: 4.9s; animation-delay: 1.4s;"></i>
  <i style="left: 86%; animation-duration: 6.2s; animation-delay: 0.3s;"></i>
</div>
""",
    unsafe_allow_html=True,
)

# Conteúdo
st.markdown('<div class="kicker">Edição Comemorativa</div>', unsafe_allow_html=True)

st.markdown(
    """
<div class="frame">
  <h1 class="title">Lis</h1>
  <div class="subtitle">Uma celebração à altura de um novo ciclo.</div>
  <div class="divider"></div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    if not st.session_state.opened:
        if st.button("✨ Abrir Cartão"):
            st.session_state.opened = True
            st.toast("Cartão aberto.", icon="✨")

if st.session_state.opened:
    time.sleep(0.2)
    st.markdown(
        """
<div class="frame">
  <div class="kicker">Mensagem</div>
  <div class="body">
    Prezada Lis,<nobr></nobr><br><br>
    Receba esta homenagem como um gesto de estima e reconhecimento. Que este aniversário marque o início de um período
    de serenidade, realização e progresso consistente — daqueles que se constroem com propósito e constância.<br><br>
    Que cada novo dia traga boas oportunidades, clareza nas decisões e a tranquilidade de quem sabe valorizar o que realmente importa.
    <br><br>
    Com respeito e sinceros votos de felicidades.
  </div>

  <div class="sealWrap"><div class="seal">Premium</div></div>
  <div class="sig">— Felicitações</div>
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")
    cc1, cc2, cc3 = st.columns([1, 2, 1])
    with cc2:
        if st.button("🥂 Celebrar"):
            st.toast("Brinde a um novo ciclo.", icon="🥂")
            st.balloons()
            st.success("Feliz aniversário, Lis.")
else:
    st.markdown(
        """
<div style="text-align:center; font-family: Inter, sans-serif; color: rgba(244,244,246,0.70); margin-top: 10px;">
  Um cartão elegante aguarda o próximo clique.
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown(
    """
<div style="text-align:center; margin-top: 40px; font-family: Inter, sans-serif; font-size: 11px; letter-spacing: 0.18em; color: rgba(244,244,246,0.35);">
  ART DÉCO EDITION • 2025
</div>
""",
    unsafe_allow_html=True,
)
