import streamlit as st

st.set_page_config(page_title="Music & Story AI Studio", page_icon="🎬", layout="wide")

# Сол жақ панель (Меню)
st.sidebar.title("📌 Бөлімді таңдаңыз")
mode = st.sidebar.radio("Қай сервисті қолданғыңыз келеді?", ["🎵 Музыка Студиясы", "📖 Рассказ Генераторы"])

# ==========================================
# 1-БӨЛІМ: МУЗЫКА СТУДИЯСЫ
# ==========================================
if mode == "🎵 Музыка Студиясы":
    st.title("🎵 Музыкалық Автоматизация Софты")
    st.write("Сілтеме немесе трек аты бойынша 3 түрлі нұсқада Suno AI промпты, ән мәтіні, YouTube метадеректері және Превью (Thumbnail) идеяларын дайындау.")
    st.divider()

    song_input = st.text_input("🔗 Әннің сілтемесін (YouTube/Spotify) немесе атын жазыңыз:")
    language = st.selectbox("🌐 Мәлімет қай тілде дайындалсын?", ["Қазақша", "Русский", "English"], key="lang_music")

    if st.button("✨ Музыка, SEO және Превью дайындау"):
        if song_input.strip() == "":
            st.warning("Өтініш, ән атын немесе сілтемесін енгізіңіз!")
        else:
            st.success(f"'{song_input}' бойынша {language} тілінде 3 нұсқа дайындалды!")
            
            if language == "Русский":
                lyrics_1 = "[Verse 1]\nНочной ритм, глубокое чувство как шторм...\n\n[Chorus]\nВремя уходит, нам не подчиняясь..."
                lyrics_2 = "[Verse 1]\nТихий вечер, звезды горят в тишине...\n\n[Chorus]\nТы мой свет, ты моя мечта..."
                lyrics_3 = "[Verse 1]\nВспышки света, ритм биения сердца...\n\n[Chorus]\nТанцуй со мной до самого утра..."
                
                yt_title_1 = f"Новинка музыки | {song_input} (Deep House Remix)"
                yt_desc = "Слушайте лучший трек в новом звучании! Подписывайтесь на канал.\n\n#deepHouse #музыка #новинка"
                yt_tags = "музыка, deep house, новинка, ремикс, трек"
                thumb_idea = f"Яркий контрастный фон, силуэт человека в наушниках под неоновым светом, крупная надпись: '{song_input}'"
                thumb_prompt = f"YouTube thumbnail style, vibrant neon glow, deep house music concept, cinematic lighting, 8k --ar 16:9"
                
            elif language == "English":
                lyrics_1 = "[Verse 1]\nNight rhythm, deep feeling like a storm...\n\n[Chorus]\nTime goes by, running out of control..."
                lyrics_2 = "[Verse 2]\nQuiet evening, stars shining in the dark...\n\n[Chorus]\nYou are my light, you are my dream..."
                lyrics_3 = "[Verse 1]\nFlashing lights, heart beating to the rhythm...\n\n[Chorus]\nDance with me until the morning comes..."
                
                yt_title_1 = f"New Music Hit | {song_input} (Remix Version)"
                yt_desc = "Listen to the best track in a new style! Subscribe for more.\n\n#newMusic #deepHouse #remix"
                yt_tags = "music, deep house, new track, remix, hit"
                thumb_idea = f"Dark moody background with glowing audio equalizer lines, bold text: 'NEW HIT'"
                thumb_prompt = f"YouTube thumbnail design, modern music vibe, dark aesthetic with bright accents, 8k --ar 16:9"
                
            else: # Қазақша
                lyrics_1 = "[Verse 1]\nТүнгі ырғақ, терең сезім дауылдай...\n\n[Chorus]\nӨтіп жатыр уақыт бізге бағынбай..."
                lyrics_2 = "[Verse 1]\nТүнгі қала, жұлдыздар жанады сырлы...\n\n[Chorus]\nСен менің арманым, сезімнің нұры..."
                lyrics_3 = "[Verse 1]\nЖарық сәуле, жүректің соғысы қатты...\n\n[Chorus]\nБиле өзіммен таң атырғанша татты..."
                
                yt_title_1 = f"Жаңа ән | {song_input} (Тәтті ремикс)"
                yt_desc = "Ең керемет әннің жаңа нұсқасы! Арнаға жазылыңыздар.\n\n#жаңаән #deepHouse #қазақша"
                yt_tags = "қазақша әндер, жаңа ән, ремикс, deep house, трек"
                thumb_idea = f"Қараңғы фондағы әсерлі атмосфера, қазақша үлкен әріппен жазу: '{song_input}'"
                thumb_prompt = f"YouTube thumbnail concept, atmospheric emotional music background, high contrast, 8k --ar 16:9"

            tab1, tab2, tab3 = st.tabs(["🔥 1-нұсқа (Organic Deep House)", "💖 2-нұсқа (Romantic Pop)", "⚡ 3-нұсқа (Club Dance)"])

            with tab1:
                st.subheader("📝 Suno AI Промпт:")
                prompt1 = "Organic Deep House, atmospheric pads, catchy bass, emotional male vocals, 120 BPM"
                st.code(prompt1)
                
                st.subheader(f"📜 Ән мәтіні ({language}):")
                st.text_area("1-нұсқа мәтіні:", lyrics_1, height=130, key="l1")
                
                st.subheader("🖼️ YouTube Превью (Thumbnail) идеясы мен Промпты:")
                st.write(f"**💡 Дизайн идеясы:** {thumb_idea}")
                st.code(thumb_prompt)

                st.subheader("📺 YouTube SEO & Метадеректер:")
                st.text_input("YouTube Название:", yt_title_1, key="yt1")
                st.text_area("YouTube Описание:", yt_desc, height=90, key="yd1")
                st.text_input("YouTube Тегтер:", yt_tags, key="ytag1")
                
                txt_data1 = f"PROMPT:\n{prompt1}\n\nLYRICS:\n{lyrics_1}\n\nTHUMBNAIL IDEA:\n{thumb_idea}\n\nTHUMBNAIL PROMPT:\n{thumb_prompt}\n\nYOUTUBE TITLE:\n{yt_title_1}\n\nDESC:\n{yt_desc}\n\nTAGS:\n{yt_tags}"
                st.download_button("💾 1-нұсқа пакетін TXT етіп жүктеп алу", txt_data1, file_name=f"music_v1_{language}.txt", key="d1")

            with tab2:
                st.subheader("📝 Suno AI Промпт:")
                prompt2 = "Romantic Pop, acoustic guitar, soft piano, warm male vocals, emotional beat, 95 BPM"
                st.code(prompt2)
                
                st.subheader(f"📜 Ән мәтіні ({language}):")
                st.text_area("2-нұсқа мәтіні:", lyrics_2, height=130, key="l2")
                
                st.subheader("🖼️ YouTube Превью (Thumbnail) идеясы мен Промпты:")
                st.write(f"**💡 Дизайн идеясы:** Романтикалық стиль, жұмсақ түстер, жүрек немесе аспан көрінісі.")
                st.code(thumb_prompt)

                st.subheader("📺 YouTube SEO & Метадеректер:")
                st.text_input("YouTube Название:", f"Romantic Version | {song_input}", key="yt2")
                st.text_area("YouTube Описание:", yt_desc, height=90, key="yd2")
                st.text_input("YouTube Тегтер:", yt_tags, key="ytag2")
                
                txt_data2 = f"PROMPT:\n{prompt2}\n\nLYRICS:\n{lyrics_2}\n\nYOUTUBE TITLE:\nRomantic Version | {song_input}\n\nDESC:\n{yt_desc}\n\nTAGS:\n{yt_tags}"
                st.download_button("💾 2-нұсқа пакетін TXT етіп жүктеп алу", txt_data2, file_name=f"music_v2_{language}.txt", key="d2")

            with tab3:
                st.subheader("📝 Suno AI Промпт:")
                prompt3 = "Energetic Dance Pop, synthwave bass, modern electropop vocals, upbeat drive, 128 BPM"
                st.code(prompt3)
                
                st.subheader(f"📜 Ән мәтіні ({language}):")
                st.text_area("3-нұсқа мәтіні:", lyrics_3, height=130, key="l3")
                
                st.subheader("🖼️ YouTube Превью (Thumbnail) идеясы мен Промпты:")
                st.write(f"**💡 Дизайн идеясы:** Клубтық жарқын түстер, динамикалық эффектілер.")
                st.code(thumb_prompt)

                st.subheader("📺 YouTube SEO & Метадеректер:")
                st.text_input("YouTube Название:", f"Club Mix | {song_input}", key="yt3")
                st.text_area("YouTube Описание:", yt_desc, height=90, key="yd3")
                st.text_input("YouTube Тегтер:", yt_tags, key="ytag3")
                
                txt_data3 = f"PROMPT:\n{prompt3}\n\nLYRICS:\n{lyrics_3}\n\nYOUTUBE TITLE:\nClub Mix | {song_input}\n\nDESC:\n{yt_desc}\n\nTAGS:\n{yt_tags}"
                st.download_button("💾 3-нұсқа пакетін TXT етіп жүктеп алу", txt_data3, file_name=f"music_v3_{language}.txt", key="d3")

# ==========================================
# 2-БӨЛІМ: РАССКАЗ ГЕНЕРАТОРЫ
# ==========================================
elif mode == "📖 Рассказ Генераторы":
    st.title("📖 Рассказ & Сюжет Генераторы")
    st.write("YouTube арналарына арналған қызықты әсерлі әңгімелер, сюжеттер және визуалды промпттар дайындау.")
    st.divider()

    story_topic = st.text_input("✍️ Рассказ тақырыбы немесе негізгі идеясы:")
    story_lang = st.selectbox("🌐 Рассказ қай тілде жасалсын?", ["Қазақша", "Русский", "English"], key="lang_story")
    story_genre = st.selectbox("🎭 Жанры:", ["Детектив / Мистика", "Драма / Өмірлік оқиға", "Романтика", "Қорқынышты әңгімелер"])

    if st.button("✨ Рассказ бен Сюжетті жасау"):
        if story_topic.strip() == "":
            st.warning("Өтініш, рассказ тақырыбын енгізіңіз!")
        else:
            st.success(f"'{story_topic}' тақырыбы бойынша {story_lang} тілінде сюжет дайындалды!")

            if story_lang == "Русский":
                story_text = f"Однажды в тихом и уютном городе произошло то, чего никто не ожидал... Тема: {story_topic}. Это была история, которая изменила всё."
                img_prompt = f"Cinematic dark moody illustration for story about {story_topic}, highly detailed, 8k"
                s_title = f"Тайна истории: {story_topic}"
                s_desc = "Удивительная и захватывающая история. Подписывайтесь на канал!\n\n#истории #рассказы #жизнь"
                s_tags = "истории из жизни, рассказы, мистика, драма"
            elif story_lang == "English":
                story_text = f"Once upon a time in a quiet city, something unexpected happened regarding {story_topic}..."
                img_prompt = f"Cinematic atmospheric illustration for story about {story_topic}, highly detailed, 8k"
                s_title = f"The Mystery of {story_topic}"
                s_desc = "An incredible story you must listen to. Subscribe for more!\n\n#stories #mystery #drama"
                s_tags = "stories, life stories, mystery, drama, storytelling"
            else: # Қазақша
                story_text = f"Бұл оқиға өмірдің тосын сыйлары мен күтпеген сәттеріне толы еді... Тақырып: {story_topic}. Бәрі бір сәтте өзгереді деп ешкім ойламаған еді."
                img_prompt = f"Cinematic emotional illustration for story about {story_topic}, highly detailed, 8k"
                s_title = f"Танымдық оқиға: {story_topic}"
                s_desc = "Жүрегіңізге әсер ететін шынайы өмірлік оқиға. Арнаға жазылыңыз!\n\n#қазақшаәңгімелер #өмірлікоқиға #әсерлі"
                s_tags = "қазақша әңгімелер, өмірлік оқиға, сыр-сұхбат, әсерлі әңгіме"

            st.subheader("📜 Дайын Рассказ / Сценарий:")
            st.text_area("Мәтін:", story_text, height=180, key="st_text")

            st.subheader("🖼️ Сурет жасауға арналған AI Промпт (Midjourney/DALL-E):")
            st.code(img_prompt)

            st.subheader("📺 YouTube SEO & Метадеректер:")
            st.text_input("YouTube Название:", s_title, key="st_t")
            st.text_area("YouTube Описание:", s_desc, height=90, key="st_d")
            st.text_input("YouTube Тегтер:", s_tags, key="st_tag")

            story_package = f"STORY:\n{story_text}\n\nIMAGE PROMPT:\n{img_prompt}\n\nYOUTUBE TITLE:\n{s_title}\n\nYOUTUBE DESC:\n{s_desc}\n\nTAGS:\n{s_tags}"
            st.download_button("💾 Рассказ пакетін TXT етіп жүктеп алу", story_package, file_name=f"story_package_{story_lang}.txt", key="dl_story")






