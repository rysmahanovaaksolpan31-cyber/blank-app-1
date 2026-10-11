import streamlit as st
from google import genai

st.set_page_config(page_title="Content Factory AI Studio", page_icon="🎬", layout="wide")

# API кілтіңізді осында тікелей жазыңыз
api_key = "AQ.Ab8RN6LIVzn81CeBEKU0i2RrA8cIOJmYHSFEI1pPWs2ZZgkOsQ"
client = genai.Client(api_key=api_key) if api_key and "КІЛТ" not in api_key else None

st.sidebar.title("📌 Бөлімді таңдаңыз")
mode = st.sidebar.radio("Қай сервисті қолданғыңыз келеді?", ["🎵 Музыка Студиясы", "📖 Рассказ Генераторы"])

if not client:
    st.warning("⚠️ Өтініш, кодтың басындағы `api_key` айнымалысына өз Gemini API кілтіңізді жазыңыз.")

# ==========================================
# 1-БӨЛІМ: МУЗЫКА СТУДИЯСЫ
# ==========================================
if mode == "🎵 Музыка Студиясы":
    st.title("🎵 Профессионал Музыкалық Автоматизация (Gemini AI)")
    st.write("Ән немесе жинақ сілтемесін/атын енгізіңіз. Gemini AI сол стилді талдап, Suno AI промптарын, толық ән мәтінін және YouTube SEO пакетін дайындайды.")
    st.divider()

    song_input = st.text_input("🔗 Әннің сілтемесін немесе атын жазыңыз (Мысалы: 'Сadraddin - Тәтті ертегім' немесе YouTube URL):")
    language = st.selectbox("🌐 Мәтін мен Метадеректер қай тілде дайындалсын?", ["Қазақша", "Русский", "English"], key="lang_music")

    if st.button("✨ Толық Кәсіби Пакетті Дайындау"):
        if song_input.strip() == "":
            st.warning("Өтініш, ән атын немесе сілтемесін енгізіңіз!")
        elif not client:
            st.error("Алдымен кодқа Gemini API кілтіңізді енгізіңіз!")
        else:
            with st.spinner("Gemini AI стильді талдап, 2 түрлі кәсіби нұсқаны дайындауда..."):
                prompt_for_ai = f"""
                You are a professional music producer and songwriter.
                Analyze the track or link: '{song_input}'.
                Create TWO complete professional music packages in language: {language}.
                Package 1: Modern/Electronic/Deep House style with ethnic elements.
                Package 2: Romantic/Pop/Acoustic style.

                CRITICAL INSTRUCTION: Return plain text ONLY. Do NOT use markdown code blocks (like ```).

                Use these exact tags for separation:

                [V1_PROMPT]
                [V1_LYRICS] ([Intro], [Verse 1], [Chorus], [Verse 2], [Bridge], [Chorus], [Outro])
                [V1_THUMB_IDEA]
                [V1_THUMB_PROMPT]
                [V1_YT_TITLE]
                [V1_YT_DESC]
                [V1_YT_TAGS]

                [V2_PROMPT]
                [V2_LYRICS] ([Intro], [Verse 1], [Chorus], [Verse 2], [Bridge], [Chorus], [Outro])
                [V2_THUMB_IDEA]
                [V2_THUMB_PROMPT]
                [V2_YT_TITLE]
                [V2_YT_DESC]
                [V2_YT_TAGS]
                """

                try:
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt_for_ai,
                    )
                    content = response.text.replace("```", "")

                    def get_part(text, start, end):
                        try:
                            p = text.split(start)[1]
                            if end in p:
                                p = p.split(end)[0]
                            return p.strip()
                        except:
                            return ""

                    # 1-нұсқа
                    p1 = get_part(content, "[V1_PROMPT]", "[V1_LYRICS]") or "Organic Deep House, 120 BPM"
                    l1 = get_part(content, "[V1_LYRICS]", "[V1_THUMB_IDEA]") or "Мәтін дайындалды."
                    ti1 = get_part(content, "[V1_THUMB_IDEA]", "[V1_THUMB_PROMPT]") or "Неоновый стиль"
                    tp1 = get_part(content, "[V1_THUMB_PROMPT]", "[V1_YT_TITLE]") or "Thumbnail 8k --ar 16:9"
                    yt1 = get_part(content, "[V1_YT_TITLE]", "[V1_YT_DESC]") or "Премьера трека"
                    yd1 = get_part(content, "[V1_YT_DESC]", "[V1_YT_TAGS]") or "Описание..."
                    ytag1 = get_part(content, "[V1_YT_TAGS]", "[V2_PROMPT]") or "музыка"

                    # 2-нұсқа
                    p2 = get_part(content, "[V2_PROMPT]", "[V2_LYRICS]") or "Romantic Pop, 95 BPM"
                    l2 = get_part(content, "[V2_LYRICS]", "[V2_THUMB_IDEA]") or "Мәтін дайындалды."
                    ti2 = get_part(content, "[V2_THUMB_IDEA]", "[V2_THUMB_PROMPT]") or "Романтический стиль"
                    tp2 = get_part(content, "[V2_THUMB_PROMPT]", "[V2_YT_TITLE]") or "Thumbnail 8k --ar 16:9"
                    yt2 = get_part(content, "[V2_YT_TITLE]", "[V2_YT_DESC]") or "Кавер версия"
                    yd2 = get_part(content, "[V2_YT_DESC]", "[V2_YT_TAGS]") or "Описание..."
                    ytag2 = get_part(content, "[V2_YT_TAGS]", "END") or "поп"

                    st.success("✨ Екі кәсіби нұсқа толығымен дайын!")

                    tab1, tab2 = st.tabs(["🔥 1-нұсқа (Deep House / Этно)", "💖 2-нұсқа (Romantic / Pop)"])

                    with tab1:
                        st.subheader("📝 Suno AI Промпт:")
                        st.code(p1)
                        st.subheader(f"📜 Толық Ән Мәтіні ({language}):")
                        st.text_area("Құрылымы:", l1, height=280, key="l1_k")
                        st.subheader("🖼️ YouTube Превью Идеясы мен Промпты:")
                        st.write(f"**💡 Идея:** {ti1}")
                        st.code(tp1)
                        st.subheader("📺 YouTube SEO:")
                        st.text_input("Название:", yt1, key="yt1_k")
                        st.text_area("Описание:", yd1, height=140, key="yd1_k")
                        st.text_input("Тегтер:", ytag1, key="ytag1_k")

                        txt_data1 = f"PROMPT:\n{p1}\n\nLYRICS:\n{l1}\n\nTITLE:\n{yt1}\n\nDESC:\n{yd1}"
                        st.download_button("💾 1-нұсқаны TXT етіп жүктеп алу", txt_data1, file_name=f"music_v1_{language}.txt", key="dl_v1")

                    with tab2:
                        st.subheader("📝 Suno AI Промпт:")
                        st.code(p2)
                        st.subheader(f"📜 Толық Ән Мәтіні ({language}):")
                        st.text_area("Құрылымы:", l2, height=280, key="l2_k")
                        st.subheader("🖼️ YouTube Превью Идеясы мен Промпты:")
                        st.write(f"**💡 Идея:** {ti2}")
                        st.code(tp2)
                        st.subheader("📺 YouTube SEO:")
                        st.text_input("Название:", yt2, key="yt2_k")
                        st.text_area("Описание:", yd2, height=140, key="yd2_k")
                        st.text_input("Тегтер:", ytag2, key="ytag2_k")

                        txt_data2 = f"PROMPT:\n{p2}\n\nLYRICS:\n{l2}\n\nTITLE:\n{yt2}\n\nDESC:\n{yd2}"
                        st.download_button("💾 2-нұсқаны TXT етіп жүктеп алу", txt_data2, file_name=f"music_v2_{language}.txt", key="dl_v2")

                except Exception as e:
                    st.error(f"Генерация қатесі: {e}")

# ==========================================
# 2-БӨЛІМ: РАССКАЗ ГЕНЕРАТОРЫ
# ==========================================
elif mode == "📖 Рассказ Генераторы":
    st.title("📖 Рассказ & Сюжет Генераторы (Gemini AI)")
    st.write("YouTube арналарына арналған толық сценарий, сурет промпты мен метадеректер дайындау.")
    st.divider()

    story_topic = st.text_input("✍️ Рассказ тақырыбы немесе негізгі идеясы:")
    story_lang = st.selectbox("🌐 Тіл:", ["Қазақша", "Русский", "English"], key="s_lang")
    story_genre = st.selectbox("🎭 Жанры:", ["Детектив / Мистика", "Драма / Өмірлік оқиға", "Романтика", "Қорқынышты әңгімелер"])

    if st.button("✨ Сюжет пен Сценарийді Жасау"):
        if story_topic.strip() == "":
            st.warning("Өтініш, тақырыпты енгізіңіз!")
        elif not client:
            st.error("Алдымен API кілтін енгізіңіз!")
        else:
            with st.spinner("Сценарий мен сюжет дайындалуда..."):
                s_prompt_ai = f"""
                Write an engaging story and YouTube script about '{story_topic}' in genre '{story_genre}' in language {story_lang}.
                Return plain text ONLY. No markdown code blocks.
                Include:
                [STORY_TEXT] (Full structured story with intro, main part, conclusion)
                [IMAGE_PROMPT] (Midjourney image prompt in English with --ar 16:9)
                [YT_TITLE] (Catchy YouTube title)
                [YT_DESC] (YouTube description with hashtags)
                [YT_TAGS] (SEO tags)
                """
                try:
                    res = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=s_prompt_ai,
                    )
                    sc_content = res.text.replace("```", "")

                    def get_s_part(text, start, end):
                        try:
                            p = text.split(start)[1]
                            if end in p:
                                p = p.split(end)[0]
                            return p.strip()
                        except:
                            return ""

                    s_text = get_s_part(sc_content, "[STORY_TEXT]", "[IMAGE_PROMPT]") or "Сценарий жасалды."
                    s_img = get_s_part(sc_content, "[IMAGE_PROMPT]", "[YT_TITLE]") or "Story thumbnail 8k --ar 16:9"
                    s_yt_t = get_s_part(sc_content, "[YT_TITLE]", "[YT_DESC]") or "Әсерлі оқиға"
                    s_yt_d = get_s_part(sc_content, "[YT_DESC]", "[YT_TAGS]") or "Сипаттама..."
                    s_yt_tag = get_s_part(sc_content, "[YT_TAGS]", "END") or "оқиға"

                    st.success("✨ Сюжет пен сценарий сәтті дайын!")

                    st.subheader("📜 Толық Рассказ / Сценарий:")
                    st.text_area("Дайын текст:", s_text, height=300, key="st_res")

                    st.subheader("🖼️ Сурет жасауға арналған AI Промпт:")
                    st.code(s_img)

                    st.subheader("📺 YouTube SEO & Метадеректер:")
                    st.text_input("YouTube Название:", s_yt_t, key="st_t_res")
                    st.text_area("YouTube Описание:", s_yt_d, height=140, key="st_d_res")
                    st.text_input("YouTube Тегтер:", s_yt_tag, key="st_tag_res")

                    story_pkg = f"STORY:\n{s_text}\n\nIMAGE PROMPT:\n{s_img}\n\nTITLE:\n{s_yt_t}\n\nDESC:\n{s_yt_d}"
                    st.download_button("💾 Сценарийді TXT файлы етіп жүктеп алу", story_pkg, file_name=f"story_{story_lang}.txt", key="dl_story_res")

                except Exception as e:
                    st.error(f"Қате: {e}")








