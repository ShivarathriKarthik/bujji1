import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Little Something for You ❤️",
    page_icon="💗",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600&display=swap');
.stApp {
  background: radial-gradient(ellipse at 50% 10%, #38204f 0%, #171326 48%, #090b16 100%);
  color: #fff5ed;
}
header, footer {visibility: hidden;}
.block-container {max-width: 850px; padding-top: 2rem; padding-bottom: 3rem;}
h1,h2,h3,p,div {font-family: 'DM Sans', sans-serif;}
.hero {text-align:center; padding: 1.3rem 0 .5rem;}
.eyebrow {letter-spacing:.28em; text-transform:uppercase; color:#e7b9d6; font-size:.72rem;}
.hero h1 {font-family:'Cormorant Garamond',serif; font-size:clamp(2.5rem,7vw,4.5rem); line-height:1; color:#fff0df; margin:.6rem 0;}
.hero p {color:#d9c8dc; font-size:1rem;}
.message {
  text-align:center; background:linear-gradient(135deg,rgba(255,255,255,.10),rgba(255,255,255,.035));
  border:1px solid rgba(255,220,245,.25); border-radius:22px; padding:1.5rem 1.2rem;
  box-shadow:0 15px 55px rgba(0,0,0,.25); margin:.8rem 0 1rem;
}
.message h2 {font-family:'Cormorant Garamond',serif; font-size:2rem; color:#ffe7f3; margin:.2rem 0 .6rem;}
.message p {color:#f0dce9; font-size:1.05rem; line-height:1.7; margin:0 auto; max-width:620px;}
.small-note {text-align:center;color:#bbaac5;font-size:.8rem;margin-top:.5rem;}
.stButton button {
  display:block; margin:0 auto; border:1px solid #f4c7df; border-radius:999px;
  background:linear-gradient(120deg,#a94e83,#7149a4); color:white; font-weight:600;
  padding:.75rem 2rem; min-height:3rem; transition:transform .2s, box-shadow .2s;
}
.stButton button:hover {border-color:#fff; color:white; transform:translateY(-2px); box-shadow:0 8px 25px #b45c9b55;}
div[data-testid="stMarkdownContainer"] {color:#fff5ed;}
</style>
""", unsafe_allow_html=True)

if "step" not in st.session_state:
    st.session_state.step = 0

messages = [
    ("A little surprise for you…", "Hey, Bujji. I made this little place just for you. Take your time, follow the lights, and let me tell you something from my heart."),
    ("You make ordinary days special", "Even the simplest moments feel beautiful when you are part of them. Your smile has a way of making my whole day better."),
    ("If I could make one wish…", "It would be to keep creating little memories with you — laughing together, holding your hand, and being there through every kind of day."),
    ("You are my favourite person", "Not because every moment is perfect, but because even the imperfect moments mean something when I get to share them with you."),
    ("One last thing…", "This fountain has one final message. And this one is the most important of all."),
    ("I LOVE YOU, BUJJIIII! ❤️", "So much more than these little words can ever explain. You are precious to me. Always remember that. ❤️"),
]

def fountain_svg(step: int) -> str:
    glow = min(step, 5)
    return f"""
    <div style="width:100%;display:flex;justify-content:center;margin:8px auto 20px;">
    <svg viewBox="0 0 640 420" width="100%" style="max-width:650px;filter:drop-shadow(0 0 24px rgba(236,139,203,.22))" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="water" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#b6f5ff" stop-opacity=".9"/><stop offset="1" stop-color="#6b79d9" stop-opacity=".2"/></linearGradient>
        <radialGradient id="halo"><stop stop-color="#ffd7f1" stop-opacity=".55"/><stop offset="1" stop-color="#d36aa8" stop-opacity="0"/></radialGradient>
      </defs>
      <ellipse cx="320" cy="365" rx="245" ry="35" fill="url(#halo)"/>
      <path d="M320 55 C275 95 270 130 320 155 C370 130 365 95 320 55Z" fill="#f3b7dd" opacity=".85" stroke="#fff0f8" stroke-width="5"/>
      <path d="M320 70 L320 145 M286 108 L354 108" stroke="#713d83" stroke-width="4"/>
      <path d="M250 155 Q320 190 390 155 L370 205 Q320 230 270 205Z" fill="#4c8caa" stroke="#e6d4ff" stroke-width="6"/>
      <path d="M270 165 L320 185 L370 165 L355 200 L285 200Z" fill="#77d4df" opacity=".7"/>
      <path d="M320 205 C290 235 290 260 320 280 C350 260 350 235 320 205Z" fill="url(#water)"/>
      <path d="M320 225 C250 250 220 280 190 310 M320 225 C390 250 420 280 450 310" stroke="#9cecff" stroke-width="8" fill="none" stroke-linecap="round" opacity=".85"/>
      <ellipse cx="320" cy="315" rx="175" ry="38" fill="#345f91" stroke="#f3d7f0" stroke-width="7"/>
      <ellipse cx="320" cy="307" rx="145" ry="23" fill="#79cbdc" opacity=".75"/>
      <path d="M175 315 L205 365 L435 365 L465 315" fill="#633e83" stroke="#f3d7f0" stroke-width="7"/>
      <path d="M205 365 L260 365 L245 325 L190 325Z" fill="#e78ab5" stroke="#fff0f8" stroke-width="3"/>
      <path d="M260 365 L320 365 L320 330 L245 325Z" fill="#6bbcc9" stroke="#fff0f8" stroke-width="3"/>
      <path d="M320 365 L380 365 L395 325 L320 330Z" fill="#a68be2" stroke="#fff0f8" stroke-width="3"/>
      <path d="M380 365 L435 365 L450 325 L395 325Z" fill="#e9bd73" stroke="#fff0f8" stroke-width="3"/>
      <g fill="#fff4fd">
        <circle cx="145" cy="205" r="3"/><circle cx="495" cy="180" r="4"/><circle cx="220" cy="90" r="3"/><circle cx="430" cy="75" r="3"/>
      </g>
      <g opacity="{0.25 + glow*0.14}">
        <path d="M320 55 C275 95 270 130 320 155 C370 130 365 95 320 55Z" fill="none" stroke="#fff" stroke-width="11"/>
        <ellipse cx="320" cy="315" rx="185" ry="46" fill="none" stroke="#ffd5f0" stroke-width="9"/>
      </g>
      <text x="320" y="405" text-anchor="middle" fill="#f7d9ed" font-size="13" letter-spacing="4">MADE WITH LOVE</text>
    </svg></div>
    """

st.markdown("""
<div class="hero">
  <div class="eyebrow">A tiny world, made for you</div>
  <h1>For My Bujji</h1>
  <p>Some feelings deserve more than a text message.</p>
</div>
""", unsafe_allow_html=True)


# A little photo gallery, using the four pictures you provided.
st.markdown("""
<div class="hero" style="padding-top:.2rem">
  <div class="eyebrow">Our little memories</div>
  <p>Every picture holds a moment I want to keep close. ❤️</p>
</div>
""", unsafe_allow_html=True)

photo_cols = st.columns(2, gap="medium")
photo_items = [
    ("assets/solo_festive.jpg", "One of my favourite pictures"),
    ("assets/couple_festive.jpg", "A moment together"),
    ("assets/solo_casual.jpg", "My favourite smile"),
    ("assets/couple_casual.jpg", "Us, just being us"),
]
for col, (photo_path, caption) in zip([photo_cols[0], photo_cols[1], photo_cols[0], photo_cols[1]], photo_items):
    with col:
        st.image(photo_path, use_container_width=True)
        st.caption(caption)

components.html(fountain_svg(st.session_state.step), height=430, scrolling=False)

title, body = messages[st.session_state.step]
st.markdown(
    f'<div class="message"><div class="eyebrow">A message from my heart</div>'
    f'<h2>{title}</h2><p>{body}</p></div>',
    unsafe_allow_html=True
)

if st.session_state.step < len(messages) - 1:
    labels = ["Open my little surprise 💗", "Next 💖", "Keep going ✨", "One more thing…", "Show me ❤️"]
    label = labels[min(st.session_state.step, len(labels)-1)]
    if st.button(label, use_container_width=False):
        st.session_state.step += 1
        st.rerun()
else:
    st.markdown('<div class="small-note">🌷 A little fountain. A thousand feelings. All for you. 🌷</div>', unsafe_allow_html=True)
    if st.button("Replay our little moment ↻"):
        st.session_state.step = 0
        st.rerun()

st.markdown('<div class="small-note">You can change every message in the <code>messages</code> list in app.py.</div>', unsafe_allow_html=True)
