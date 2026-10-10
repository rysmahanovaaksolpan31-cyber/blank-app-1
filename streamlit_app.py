import streamlit as st

st.set_page_config(page_title="Music & Story AI Studio", page_icon="🚀", layout="wide")

# Навигациялық Меню
st.sidebar.title("📌 Бөлімді таңдаңыз")
mode = st.sidebar.radio("Қай сервисті қолданасыз?", ["🎵 Музыка Студиясы", "📖 Рассказ & Story Generator"])

# ==========================================
# 1-БӨЛІМ: МУЗЫКА СТУДИЯСЫ
# ==========================================
if mode == "🎵 Музыка Студиясы":
    st.title("🎵 Музыкалық Автоматизация Софты")
    st.write("Сілтеме немесе трек аты бойынша 3 түрлі нұсқада Suno AI промпты мен ән мәтінін дайындау.")
    st.divider()

    track_input = st.text_input(
        "🔗 Әннің сілтемесін (YouTube/Spotify) немесе атын жазыңыз:",
        placeholder="Мысалы: https://youtu.be/... немесе 'Sadraddin - Tatti ertegim'"
    )

    language = st.selectbox(
        "🌐 Ән мәтіні қай тілде дайындалсын?",
        ["Қазақша", "Русский", "English", "العربية (Арабша)"]
    )

    if st.button("✨ 3 түрлі нұсқада музыка дайындау"):
        if track_input:
            st.success(f"'{track_input}' негізінде {language} тілінде 3 нұсқа дайындалды!")
            
            tab1, tab2, tab3 = st.tabs(["🔥 1-нұсқа (Organic Deep House)", "💖 2-нұсқа (Romantic Pop)", "⚡ 3-нұсқа (Club / Dance Remix)"])
            
            with tab1:
                st.subheader("📝 Suno AI Промпт:")
                prompt1 = "Organic Deep House, atmospheric pads, catchy melody, 120 bpm, high quality vocal"
                st.code(prompt1, language="text")
                st.subheader(f"📜 Ән мәтіні ({language}):")
                lyrics1 = f"[Verse 1]\nТүнгі ырғақ, терең сезім дауылдай ({language})...\n\n[Chorus]\nӨтіп жатыр уақыт бізге бағынбай..."
                st.text_area("1-нұсқа мәтіні:", lyrics1, height=150, key="l1")
                
                full_text_1 = f"PROMPT:\n{prompt1}\n\nLYRICS:\n{lyrics1}"
                st.download_button("📥 1-нұсқаны TXT файлы етіп жүктеп алу", data=full_text_1, file_name="music_option_1.txt", mime="text/plain", key="d1")

            with tab2:
                st.subheader("📝 Suno AI Промпт:")
                prompt2 = "Melodic Acoustic Pop, soft emotional piano, warm vocal, romantic ballad, 95 bpm"
                st.code(prompt2, language="text")
                st.subheader(f"📜 Ән мәтіні ({language}):")
                lyrics2 = f"[Verse 1]\nСезімге толы көздеріңе қараймын ({language})...\n\n[Chorus]\nҰмытпа мені, есіңе алғайсың..."
                st.text_area("2-нұсқа мәтіні:", lyrics2, height=150, key="l2")
                
                full_text_2 = f"PROMPT:\n{prompt2}\n\nLYRICS:\n{lyrics2}"
                st.download_button("📥 2-нұсқаны TXT файлы етіп жүктеп алу", data=full_text_2, file_name="music_option_2.txt", mime="text/plain", key="d2")

            with tab3:
                st.subheader("📝 Suno AI Промпт:")
                prompt3 = "High energy Dance Remix, driving synth bass, festival EDM lead, powerful vocal, 128 bpm"
                st.code(prompt3, language="text")
                st.subheader(f"📜 Ән мәтіні ({language}):")
                lyrics3 = f"[Verse 1]\nТүн ортасы, клубте жарық жанады ({language})...\n\n[Chorus]\nБиле тоқтамай, қуатты сезін..."
                st.text_area("3-нұсқа мәтіні:", lyrics3, height=150, key="l3")
                
                full_text_3 = f"PROMPT:\n{prompt3}\n\nLYRICS:\n{lyrics3}"
                st.download_button("📥 3-нұсқаны TXT файлы етіп жүктеп алу", data=full_text_3, file_name="music_option_3.txt", mime="text/plain", key="d3")
        else:
            st.warning("Өтініш, әнге сілтеме немесе атын енгізіңіз!")

# ==========================================
# 2-БӨЛІМ: РАССКАЗ ЖӘНЕ СТОРИ ГЕНЕРАТОР
# ==========================================
else:
    st.title("📖 Рассказ & YouTube Story Generator")
    st.write("30-60 минуттық видеоларға арналған орысша және ағылшынша сюжеттер мен ИИ-сценарий дайындау.")
    st.divider()

    story_title = st.text_input(
        "💡 Рассказ тақырыбын немесе негізгі идеяны жазыңыз:",
        placeholder="Мысалы: 'Тайна заброшенного замка' немесе 'A lonely detective in London'"
    )

    col1, col2 = st.columns(2)
    with col1:
        story_lang = st.selectbox("🌐 Рассказ тілі:", ["Русский", "English"])
    with col2:
        story_genre = st.selectbox("🎭 Жанры:", ["Детектив / Мистика", "Драма / История из жизни", "Фантастика / Ужасы", "Романтика"])

    if st.button("🚀 Сценарий мен ИИ-Промпттарды генерациялау"):
        if story_title:
            st.success(f"'{story_title}' тақырыбы бойынша {story_lang} тілінде дайын материалдар:")

            st.subheader("📜 1. Видеоға арналған толық Сценарий (Текст для озвучки):")
            if story_lang == "Русский":
                story_text = f"--- ВВЕДЕНИЕ ---\nЭто была холодная осенняя ночь. {story_title} — история, которую никто не должен был узнать...\n\n--- ГЛАВА 1: НАЧАЛО ---\nВсе началось с одного странного письма, полученного в полночь...\n\n(Далее следует продолжение истории для 30-60 минутного видео...)"
            else:
                story_text = f"--- INTRODUCTION ---\nIt was a dark and cold night. The story of {story_title} was forgotten for years...\n\n--- CHAPTER 1: THE BEGINNING ---\nIt all started with a mysterious letter received at midnight...\n\n(Full long story prompt for 30-60 min voiceover...)"
            
            st.text_area("Дайын текст:", story_text, height=220, key="story_area")

            img_prompt = f"Cinematic realistic illustration, {story_genre} vibe, {story_title}, dark moody lighting, highly detailed 8k, 16:9 aspect ratio"
            st.subheader("🖼️ 2. Суреттер жасауға арналған промпттар (Midjourney / DALL-E):")
            st.code(img_prompt, language="text")

            st.subheader("🏷️ 3. SEO Тагтар мен Идеялар:")
            seo_info = f"YouTube Название: {story_title} | Полная история ({story_lang})\nТеги: #историинаночь #рассказы #{story_genre.lower().replace(' ', '')} #аудиокнига #storytelling"
            st.write(f"**YouTube Название:** {story_title} | Полная история ({story_lang})")
            st.write(f"**Теги:** #историинаночь #рассказы #{story_genre.lower().replace(' ', '')} #аудиокнига #storytelling")

            full_story_package = f"=== SCRIPT ===\n{story_text}\n\n=== IMAGE PROMPTS ===\n{img_prompt}\n\n=== SEO & TAGS ===\n{seo_info}"
            st.download_button("📥 Рассказ сценарийін TXT файлы етіп жүктеп алу", data=full_story_package, file_name="story_script.txt", mime="text/plain", key="d_story")
        else:
            st.warning("Өтініш, рассказ тақырыбын енгізіңіз!")



