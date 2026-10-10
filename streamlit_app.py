import streamlit as st

st.set_page_config(page_title="Music Studio AI", page_icon="🎵")

st.title("🎵 Музыкалық Автоматизация Софты")
st.write("Музыка тректерін талдау, текст генерациялау, сурет және SEO жасау құралы.")

st.divider()

track_title = st.text_input("Трек аты немесе стилі:", placeholder="Мысалы: Organic Deep House remix")

if st.button("✨ Текст және Промпт дайындау"):
    if track_title:
        st.success(f"'{track_title}' трегі үшін деректер дайындалды!")
        st.subheader("📝 Suno AI үшін промпт:")
        st.code("Arabic Organic Deep House, deep atmospheric pads, catchy melody, 120 bpm, high quality", language="text")
        
        st.subheader("📜 Ән мәтіні (Lyrics):")
        st.text_area("Генерацияланған текст:", "Жұлдызды түн, тыныш дала...\nЖүректегі сырлы әуен...", height=150)
    else:
        st.warning("Өтініш, трек атын енгізіңіз!")

st.divider()

st.subheader("🖼️ Обложка және SEO тагтар")
if st.button("🎨 Идеялар шығару"):
    st.write("**YouTube Тагтар:** #music #deephouse #remix #layalimusic")
    st.write("**Промпт DALL-E үшін:** A artistic music album cover, deep house vibe, sunset desert, high resolution 8k")


