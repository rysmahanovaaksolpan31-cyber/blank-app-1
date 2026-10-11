import streamlit as st

st.set_page_config(page_title="Content Factory AI Studio", page_icon="🎬", layout="wide")

st.sidebar.title("📌 Бөлімді таңдаңыз")
mode = st.sidebar.radio("Қай сервисті қолданғыңыз келеді?", ["🎵 Музыка Студиясы", "📖 Рассказ Генераторы"])

# Атауды сілтемелерден тазалау функциясы
def clean_input_title(raw_input):
    if "http" in raw_input or "youtu" in raw_input:
        parts = raw_input.split("/")[-1].replace("watch?v=", "").split("?")[0]
        return parts.replace("_", " ").replace("-", " ").capitalize() if parts else "Арнайы Трек"
    return raw_input.strip()

# ==========================================
# 1-БӨЛІМ: МУЗЫКА СТУДИЯСЫ
# ==========================================
if mode == "🎵 Музыка Студиясы":
    st.title("🎵 Профессионал Музыкалық Автоматизация")
    st.write("Сілтеме немесе трек/жинақ атын енгізіп, Suno AI промптын, толық ән мәтінін, YouTube SEO және Превью идеяларын алыңыз.")
    st.divider()

    song_input = st.text_input("🔗 Әннің/Жинақтың атын немесе сілтемесін жазыңыз (Мысалы: 'Есіңе мені алғайсың' немесе YouTube URL):")
    language = st.selectbox("🌐 Мәтін мен Метадеректер қай тілде дайындалсын?", ["Қазақша", "Русский", "English"], key="lang_music")

    if st.button("✨ Толық Кәсіби Пакетті Дайындау"):
        if song_input.strip() == "":
            st.warning("Өтініш, ән атын немесе сілтемесін енгізіңіз!")
        else:
            title = clean_input_title(song_input)
            st.success(f"'{title}' бойынша {language} тілінде толыққанды 3 кәсіби нұсқа дайындалды!")

            if language == "Русский":
                # 1-нұсқа: Deep House
                lyrics_1 = (
                    f"[Intro - Deep synth pads, subtle ethnic flutes, slow sub-bass build-up]\n\n"
                    f"[Verse 1]\n"
                    f"Тени прошлых воспоминаний о треке '{title}' растворились в ночной тишине,\n"
                    f"Каждый шепот ветра напоминает мне о забытом огне.\n"
                    f"Этот город засыпает под ритмы холодного дождя,\n"
                    f"Я ищу твои следы, но вокруг лишь глубокая темнота...\n\n"
                    f"[Chorus - Emotional high energy beat, deep punchy bass drop]\n"
                    f"Забирай мою память, забирай мою боль и страх,\n"
                    f"История '{title}' останется навечно в наших сердцах.\n"
                    f"В океане иллюзий, где нет берегов и спасения,\n"
                    f"Мы растворяемся в звуке нового притяжения...\n\n"
                    f"[Verse 2]\n"
                    f"Каждый шаг как по лезвию, каждый вдох наполнен огнем,\n"
                    f"Мы пытались сбежать от прошлого, но опять мы вдвоем.\n"
                    f"Разлетаются искры от сгоревших мостов и надежд,\n"
                    f"Среди тысяч чужих взглядов и бессмысленных одежд...\n\n"
                    f"[Bridge - Atmospheric breakdown, piano solo with soft male vocal]\n"
                    f"И если вспыхнет яркий свет в полной ночной тьме...\n"
                    f"Вспомню ли я снова о нашей общей мечте?..\n\n"
                    f"[Chorus - Explosive drop with heavy sub-bass and ethnic drive]\n"
                    f"Забирай мою память, забирай мою боль и страх,\n"
                    f"История '{title}' останется навечно в наших сердцах.\n"
                    f"В океане иллюзий, где нет берегов и спасения,\n"
                    f"Мы растворяемся в звуке нового притяжения...\n\n"
                    f"[Outro - Fade out with piano and ethnic duduk chords]\n"
                    f"Только эхо в ночи... Только '{title}'... Бесконечность."
                )
                prompt_1 = f"Organic Deep House remix of {title}, hypnotic deep sub-bass, atmospheric ethnic duduk, emotional deep vocal, punchy kick drum, 122 BPM, high-end studio mix, immersive audio"
                yt_title_1 = f"{title} - Organic Deep House Remix (2026) | Премьера Трека"
                yt_desc_1 = (
                    f"🔥 Погрузитесь в атмосферу глубокого звука и незабываемых эмоций!\n\n"
                    f"Представляем вам эксклюзивную ремикс-версию на тему '{title}'. "
                    f"Специальный саунд-дизайн, объединяющий этнические мотивы и мощный deep house бит.\n\n"
                    f"🎧 Слушайте в наушниках для полного погружения!\n"
                    f"💬 Напишите в комментариях, как вам этот вайб?\n"
                    f"👍 Ставьте лайк и подписывайтесь на канал Layali Music!\n\n"
                    f"#DeepHouse #{title.replace(' ', '')} #Музыка2026 #Премьера #Remix"
                )
                yt_tags_1 = f"{title}, deep house remix, музыка 2026, ремикс, слушать музыку, премьера песни, новинки музыки, organic house"
                thumb_idea_1 = f"Крупный неоновый текст '{title}', фиолетово-синие тона, силуэт музыканта в тумане с сильным световым контрастом."
                thumb_prompt_1 = f"YouTube thumbnail design, dramatic atmospheric lighting, glowing neon typography '{title}', deep house music vibe, 8k --ar 16:9"

                # 2-нұсқа: Romantic Pop
                lyrics_2 = (
                    f"[Intro - Soft acoustic guitar, gentle piano melodies]\n\n"
                    f"[Verse 1]\n"
                    f"Тихий вечер опускается на улицу, звезды горят в полной тишине,\n"
                    f"Все мысли о '{title}' снова возвращают меня к тебе.\n"
                    f"Твой нежный голос звучит сквозь расстояние и года,\n"
                    f"Я верю, что эта светлая любовь останется навсегда...\n\n"
                    f"[Chorus - Warm emotional pop beat, lush vocal harmonies]\n"
                    f"Ты мой свет в темноте, ты моя долгожданная мечта,\n"
                    f"Пусть звучит мелодия '{title}', наполняя сердца.\n"
                    f"Сквозь дожди и метели я к тебе одному лечу,\n"
                    f"Обнять тебя крепко и любить тебя сильно хочу...\n\n"
                    f"[Verse 2]\n"
                    f"Касание рук, искренний взгляд — в этом весь наш мир,\n"
                    f"Ты мой главный ориентир в жизни и мой единственный кумир.\n"
                    f"Мы напишем свою главу без грусти и без лишних слез,\n"
                    f"В мире, где сбываются сотни самых прекрасных грёз...\n\n"
                    f"[Bridge - Soft string quartet, high emotional vocal pitch]\n"
                    f"И когда опустится ночь на наш уютный дом,\n"
                    f"Мы будем тихими словами говорить о золотом...\n\n"
                    f"[Chorus - Warm emotional pop beat, maximum harmony]\n"
                    f"Ты мой свет в темноте, ты моя долгожданная мечта,\n"
                    f"Пусть звучит мелодия '{title}', наполняя сердца.\n"
                    f"Сквозь дожди и метели я к тебе одному лечу,\n"
                    f"Обнять тебя крепко и любить тебя сильно хочу...\n\n"
                    f"[Outro - Piano solo fade out]\n"
                    f"Навечно вместе... Мелодия '{title}'."
                )
                prompt_2 = f"Romantic Pop arrangement, acoustic guitar, soft piano, warm emotional male vocal, gentle beat, 95 BPM, crystalline mastering"
                yt_title_2 = f"{title} (Romantic Cover Version) | Трогательная Музыка"
                yt_desc_2 = f"💖 Душевная и романтическая версия '{title}'. Идеально для вечернего прослушивания.\n\n#Романтика #{title.replace(' ', '')} #ПопМузыка"
                yt_tags_2 = f"{title}, романтическая музыка, душевная песня, кавер, поп музыка"
                thumb_idea_2 = f"Теплые золотистые и закатные тона, силуэт пары, мягкий романтический фон с элегантным текстом '{title}'."
                thumb_prompt_2 = f"Aesthetic romance YouTube thumbnail, golden hour cinematic lighting, soft focus background, elegant text '{title}', 8k --ar 16:9"

            elif language == "English":
                lyrics_1 = (
                    f"[Intro - Ambient soundscape, soft electric guitar, low bass rumble]\n\n"
                    f"[Verse 1]\n"
                    f"Fading shadows under the city lights, thinking of '{title}',\n"
                    f"Chasing distant memories through endless rainy nights.\n"
                    f"Whispers in the dark calling out your forgotten name,\n"
                    f"Nothing feels the same in this endless twisted game...\n\n"
                    f"[Chorus - Dynamic punchy drop, deep organic house groove]\n"
                    f"Take my heart, take my soul, set my spirit free,\n"
                    f"The rhythm of '{title}' is pulling you and me.\n"
                    f"When the storm goes quiet and the sky turns bright,\n"
                    f"We will burn together like a spark in the night...\n\n"
                    f"[Verse 2]\n"
                    f"Every step I take leads me right back to your door,\n"
                    f"Searching for the answers that I never found before.\n"
                    f"Broken promises scattered all over the floor,\n"
                    f"I don't wanna run away from this love anymore...\n\n"
                    f"[Bridge - Emotional piano vocal breakdown]\n"
                    f"Will we find the light before we fade into the dark?\n"
                    f"Reignite the fire from this tiny little spark...\n\n"
                    f"[Chorus - Climax drop with high energy bassline]\n"
                    f"Take my heart, take my soul, set my spirit free,\n"
                    f"The rhythm of '{title}' is pulling you and me.\n"
                    f"When the storm goes quiet and the sky turns bright,\n"
                    f"We will burn together like a spark in the night...\n\n"
                    f"[Outro - Fading ambient pads]\n"
                    f"Lost in the sound of '{title}'... Set me free."
                )
                prompt_1 = f"Melodic Organic House track based on {title}, driving warm bassline, ethereal synth pads, expressive male vocals, crisp percussion, 120 BPM"
                yt_title_1 = f"{title} (Official Melodic Deep House Remix)"
                yt_desc_1 = f"✨ Experience the ultimate musical vibe with '{title}'. Subscribe for more releases!\n\n#DeepHouse #{title.replace(' ', '')} #Remix"
                yt_tags_1 = f"{title}, deep house mix, melodic house, chill music, new track 2026, remix"
                thumb_idea_1 = f"Futuristic aesthetic, soundwaves background, bold text: '{title}'"
                thumb_prompt_1 = f"High aesthetic music cover thumbnail, cinematic deep focus, glowing lines, modern electronic music design, 8k --ar 16:9"

                lyrics_2 = lyrics_1
                prompt_2 = prompt_1
                yt_title_2 = f"{title} - Chillout Version"
                yt_desc_2 = yt_desc_1
                yt_tags_2 = yt_tags_1
                thumb_idea_2 = thumb_idea_1
                thumb_prompt_2 = thumb_prompt_1

            else: # Қазақша
                lyrics_1 = (
                    f"[Intro - Қобыз бен сыбызғы үні, терең атмосфералық басс]\n\n"
                    f"[Verse 1]\n"
                    f"Түнгі қала, шамдары сөнген мұңды көшелер,\n"
                    f"'{title}' әуені жүректегі сырды тербетер.\n"
                    f"Өткен күннің елесі қайтадан оралып ойға,\n"
                    f"Тағы да жалғыз қалдым мынау бисіз тойда...\n\n"
                    f"[Chorus - Терең басс, ырғақты кач, этно-электроника]\n"
                    f"Жоғалтқым келмейді сезімді қайтадан,\n"
                    f"'{title}' әуені тарайды кең байтақ даладан.\n"
                    f"Сезімнің дауылы басылмай келеді жүректе,\n"
                    f"Тек сені, тек сені іздеймін бұл түнде...\n\n"
                    f"[Verse 2]\n"
                    f"Көздеріңде тұнғандай жұмбақ сырлы әлем,\n"
                    f"Қолдарыңнан ұстауға батпайды батыл кәлем.\n"
                    f"Уақыт емші десе де емдей алмады жараны,\n"
                    f"Сені ойлаумен тағы да атты арайлы таңым...\n\n"
                    f"[Bridge - Пианино мен сыбызғының эмоциялық дуэті]\n"
                    f"Жұлдыздар аққанда бір тілек тіледім іштей,\n"
                    f"Өтер ме екен бұл өмір өзіңді мүлде көрмей?..\n\n"
                    f"[Chorus - Максималды энергия, жарылғыш басс дроп]\n"
                    f"Жоғалтқым келмейді сезімді қайтадан,\n"
                    f"'{title}' әуені тарайды кең байтақ даладан.\n"
                    f"Сезімнің дауылы басылмай келеді жүректе,\n"
                    f"Тек сені, тек сені іздеймін бұл түнде...\n\n"
                    f"[Outro - Баяу өшу, қобыздың соңғы пернесі]\n"
                    f"Тек сені... '{title}'... Мәңгілікке."
                )
                prompt_1 = f"Kazakh Ethnic Organic Deep House, remix of {title}, deep driving bass, atmospheric kobyz and sybyzgy pads, passionate emotional vocal, 120 BPM, professional mix"
                yt_title_1 = f"{title} - Жаңа Нұсқа (Organic Deep House Remix) | 2026"
                yt_desc_1 = (
                    f"🔥 Жүректі тербейтін ерекше туынды! '{title}' әнінің жаңа заманауи ремикс нұсқасы.\n\n"
                    f"Терең басс ырғақтары мен қазақтың ұлттық аспаптарының сиқырлы үні үйлесім тапқан бірегей трек. "
                    f"Көлікте, құлаққаппен тыңдауға өте ыңғайлы!\n\n"
                    f"💬 Ән ұнады ма? Өз ойыңызды пікірге жазып кетіңіз!\n"
                    f"🔔 Арнамызға жазылып, лайк басуды ұмытпаңыздар!\n\n"
                    f"#ҚазақшаӘндер #{title.replace(' ', '')} #DeepHouse #ЖаңаӘн #Ремикс2026"
                )
                yt_tags_1 = f"{title}, қазақша әндер, жаңа ән 2026, deep house казакша, ремикс, хит әндер, казакша ремикс"
                thumb_idea_1 = f"Қараңғы стильді фон, ортада алтын түстес қазақы орнамент пен неоны бар үлкен жазу: '{title}'"
                thumb_prompt_1 = f"YouTube thumbnail design, cinematic dark aesthetic with golden glowing kazakh ornament accents, dramatic lighting, high contrast text '{title}', 8k --ar 16:9"

                # 2-нұсқа: Поп Эстрада
                lyrics_2 = (
                    f"[Intro - Акустикалық гитара, жағымды ырғақ]\n\n"
                    f"[Verse 1]\n"
                    f"Жазғы кеш, мамыражай тыныш дала,\n"
                    f"'{title}' әуені естіледі шалғайдан ғана.\n"
                    f"Екеуміз жүрген сол бір жағалауда,\n"
                    f"Сезім лаулап жанады қайтадан қайта...\n\n"
                    f"[Chorus - Жұмсақ поп ырғақ, лирикалық вокал]\n"
                    f"Сен менің арманым, сезімнің нұрысың,\n"
                    f"Жүректің соғуы, өмірдің тынысысың.\n"
                    f"Үзбеші үмітті, қашықтама менен,\n"
                    f"Мәңгілікке бірге боламын сенімен...\n\n"
                    f"[Verse 2]\n"
                    f"Қол ұстасып жүрейік жұлдыздар астында,\n"
                    f"Бақыттың кілті тұрғандай біздің уыста.\n"
                    f"Ешкімге бермеймін өзіңдей асылымды,\n"
                    f"Сақтаймын іштегі пәк сұлу сырымды...\n\n"
                    f"[Bridge - Пианино соло]\n"
                    f"Уақыт тоқтасын біз үшін осы сәтте...\n\n"
                    f"[Chorus - Жұмсақ поп ырғақ, толық хор]\n"
                    f"Сен менің арманым, сезімнің нұрысың,\n"
                    f"Жүректің соғуы, өмірдің тынысысың.\n"
                    f"Үзбеші үмітті, қашықтама менен,\n"
                    f"Мәңгілікке бірге боламын сенімен...\n\n"
                    f"[Outro - Гитара пернелері өшеді]\n"
                    f"Бірге боламын сенімен..."
                )
                prompt_2 = f"Kazakh Romantic Pop arrangement of {title}, acoustic guitar, soft synth, warm male vocal, emotional beat, 95 BPM"
                yt_title_2 = f"{title} (Pop Cover Version) | Сүйікті Әндер"
                yt_desc_2 = f"💖 Жүрекке жылы тиетін орындау: '{title}'.\n\n#ҚазақшаЭстрада #{title.replace(' ', '')}"
                yt_tags_2 = f"{title}, қазақша эстрада, лирикалық ән, романтика"
                thumb_idea_2 = f"Жұмсақ романтикалық фон, әдемі қазақша жазу: '{title}'"
                thumb_prompt_2 = f"Romantic music cover art, soft warm colors, bokeh effect, text '{title}', 8k --ar 16:9"

            tab1, tab2 = st.tabs(["🔥 1-нұсқа (Organic Deep House)", "💖 2-нұсқа (Romantic / Pop)"])

            with tab1:
                st.subheader("📝 Кәсіби Suno AI Промпт:")
                st.code(prompt_1)

                st.subheader(f"📜 Толық Ән Мәтіні ({language}):")
                st.text_area("Ән құрылымы:", lyrics_1, height=280, key="l1_main")

                st.subheader("🖼️ YouTube Превью (Thumbnail) Концепті:")
                st.write(f"**💡 Дизайн идеясы:** {thumb_idea_1}")
                st.code(thumb_prompt_1)

                st.subheader("📺 Вирустық YouTube SEO & Метадеректер:")
                st.text_input("YouTube Название:", yt_title_1, key="yt1_m")
                st.text_area("YouTube Хук-Описание:", yt_desc_1, height=160, key="yd1_m")
                st.text_input("YouTube Тегтер:", yt_tags_1, key="ytag1_m")

                txt_data1 = f"PROMPT:\n{prompt_1}\n\nLYRICS:\n{lyrics_1}\n\nTHUMBNAIL IDEA:\n{thumb_idea_1}\n\nTHUMBNAIL PROMPT:\n{thumb_prompt_1}\n\nYOUTUBE TITLE:\n{yt_title_1}\n\nDESC:\n{yt_desc_1}\n\nTAGS:\n{yt_tags_1}"
                st.download_button("💾 1-нұсқа пакетін TXT етіп жүктеп алу", txt_data1, file_name=f"music_v1_{title}_{language}.txt", key="dl1_m")

            with tab2:
                st.subheader("📝 Кәсіби Suno AI Промпт:")
                st.code(prompt_2)

                st.subheader(f"📜 Толық Ән Мәтіні ({language}):")
                st.text_area("Ән құрылымы:", lyrics_2, height=280, key="l2_main")

                st.subheader("🖼️ YouTube Превью (Thumbnail) Концепті:")
                st.write(f"**💡 Дизайн идеясы:** {thumb_idea_2}")
                st.code(thumb_prompt_2)

                st.subheader("📺 Вирустық YouTube SEO & Метадеректер:")
                st.text_input("YouTube Название:", yt_title_2, key="yt2_m")
                st.text_area("YouTube Хук-Описание:", yt_desc_2, height=160, key="yd2_m")
                st.text_input("YouTube Тегтер:", yt_tags_2, key="ytag2_m")

                txt_data2 = f"PROMPT:\n{prompt_2}\n\nLYRICS:\n{lyrics_2}\n\nTHUMBNAIL IDEA:\n{thumb_idea_2}\n\nTHUMBNAIL PROMPT:\n{thumb_prompt_2}\n\nYOUTUBE TITLE:\n{yt_title_2}\n\nDESC:\n{yt_desc_2}\n\nTAGS:\n{yt_tags_2}"
                st.download_button("💾 2-нұсқа пакетін TXT етіп жүктеп алу", txt_data2, file_name=f"music_v2_{title}_{language}.txt", key="dl2_m")

# ==========================================
# 2-БӨЛІМ: РАССКАЗ ГЕНЕРАТОРЫ
# ==========================================
elif mode == "📖 Рассказ Генераторы":
    st.title("📖 Рассказ & Сюжет Генераторы")
    st.write("YouTube арналарына арналған толыққанды сценарий, AI сурет промпты мен метадеректер дайындау.")
    st.divider()

    story_topic = st.text_input("✍️ Рассказ тақырыбы немесе негізгі идеясы:")
    story_lang = st.selectbox("🌐 Рассказ қай тілде жасалсын?", ["Қазақша", "Русский", "English"], key="lang_story")
    story_genre = st.selectbox("🎭 Жанры:", ["Детектив / Мистика", "Драма / Өмірлік оқиға", "Романтика", "Қорқынышты әңгімелер"])

    if st.button("✨ Рассказ бен Сюжетті жасау"):
        if story_topic.strip() == "":
            st.warning("Өтініш, рассказ тақырыбын енгізіңіз!")
        else:
            s_title_clean = clean_input_title(story_topic)
            st.success(f"'{s_title_clean}' тақырыбы бойынша {story_lang} тілінде толық сюжет дайындалды!")

            if story_lang == "Русский":
                s_text = (
                    f"--- ВВЕДЕНИЕ ---\n"
                    f"Это была холодная осенняя ночь, когда история вокруг '{s_title_clean}' только начиналась. "
                    f"В маленьком городке, скрытом за туманом, никто не подозревал о предстоящих событиях...\n\n"
                    f"--- ОСНОВНАЯ ЧАСТЬ ---\n"
                    f"Главный герой шагнул в неизвестность. Жанр {story_genre} раскрывал свои самые тайные стороны. "
                    f"Каждый шаг давался с трудом, а загадка '{s_title_clean}' становилась всё запутаннее. "
                    f"Неожиданный поворот судьбы заставил переосмыслить всё прошлое...\n\n"
                    f"--- КУЛЬМИНАЦИЯ И ФИНАЛ ---\n"
                    f"Когда правда наконец всплыла на поверхность, никто не мог поверить в увиденное. "
                    f"Эта история о {s_title_clean} навсегда изменила жизни всех участников."
                )
                s_prompt = f"Cinematic realistic illustration for story '{s_title_clean}', {story_genre} atmosphere, highly detailed, dramatic lighting, 8k --ar 16:9"
                s_yt_title = f"ТАЙНА {s_title_clean.upper()} | Захватывающая история ({story_genre})"
                s_yt_desc = f"😱 Невероятная история, которая держит в напряжении до последней секунды!\n\nСмотрите до конца, чтобы узнать развязку '{s_title_clean}'.\n\n#истории #рассказы #{story_genre.split()[0]}"
                s_yt_tags = f"{s_title_clean}, истории из жизни, рассказы на ночь, мистика, драма, аудиорассказы"

            elif story_lang == "English":
                s_text = (
                    f"--- INTRODUCTION ---\n"
                    f"It was a dark and cold evening when the story of '{s_title_clean}' began to unfold...\n\n"
                    f"--- MAIN STORY ---\n"
                    f"Stepping into the mystery of {story_genre}, the main character faced unpredictable challenges. "
                    f"The secret behind '{s_title_clean}' was deeper than anyone could ever imagine...\n\n"
                    f"--- CONCLUSION ---\n"
                    f"In the end, the truth revealed everything. A story that will never be forgotten."
                )
                s_prompt = f"Cinematic atmospheric concept art for '{s_title_clean}', {story_genre} movie scene, 8k resolution --ar 16:9"
                s_yt_title = f"The Mystery of {s_title_clean} | Full Story"
                s_yt_desc = f"✨ An unforgettable story about {s_title_clean}. Subscribe for more captivating stories!\n\n#stories #mystery"
                s_yt_tags = f"{s_title_clean}, audio story, storytelling, drama, mystery"

            else: # Қазақша
                s_text = (
                    f"--- КІРІСПЕ ---\n"
                    f"Бұл оқиға '{s_title_clean}' тақырыбы төңірегінде өрбиді. Күздің салқын түнінде орын алған бұл жағдай ешкімнің түсіне кірмеген еді...\n\n"
                    f"--- НЕГІЗГІ БӨЛІМ ---\n"
                    f"Бас кейіпкер үлкен сынаққа тап болды. {story_genre} жанрындағы бұл оқиға адым сайын сыр мен жұмбаққа толы болды. "
                    f"'{s_title_clean}' жұмбағы шешілмеген сайын, үрей мен қызығушылық қатар өсті...\n\n"
                    f"--- ШЫҢЫ МЕН СОҢЫ ---\n"
                    f"Шындық ашылған сәтте бәрі таңғалды. Бұл оқиға өмірдің қаншалықты тосын сыйларға толы екенін тағы бір мәрте дәлелдеді."
                )
                s_prompt = f"Cinematic emotional kazakh storytelling art for '{s_title_clean}', {story_genre} vibe, ultra detailed, 8k --ar 16:9"
                s_yt_title = f"{s_title_clean.upper()} | Өмірлік Әсерлі Оқиға ({story_genre})"
                s_yt_desc = f"🔥 Жүрегіңізді тербейтін шынайы әрі әсерлі оқиға!\n\nСоңына дейін тыңдап, өз ойыңызды пікірге жазып кетіңіз.\n\n#қазақшаәңгімелер #өмірлікоқиға #әңгіме"
                s_yt_tags = f"{s_title_clean}, қазақша әңгімелер, өмірлік оқиға, сыр-сұхбат, әсерлі әңгіме, аудио әңгіме"

            st.subheader("📜 Толық Рассказ / Сценарий:")
            st.text_area("Дайын текст:", s_text, height=280, key="st_text_main")

            st.subheader("🖼️ Сурет жасауға арналған AI Промпт (Midjourney/DALL-E):")
            st.code(s_prompt)

            st.subheader("📺 YouTube SEO & Метадеректер:")
            st.text_input("YouTube Название:", s_yt_title, key="st_t_m")
            st.text_area("YouTube Описание:", s_yt_desc, height=140, key="st_d_m")
            st.text_input("YouTube Тегтер:", s_yt_tags, key="st_tag_m")

            story_package = f"STORY:\n{s_text}\n\nIMAGE PROMPT:\n{s_prompt}\n\nYOUTUBE TITLE:\n{s_yt_title}\n\nYOUTUBE DESC:\n{s_yt_desc}\n\nTAGS:\n{s_yt_tags}"
            st.download_button("💾 Рассказ сценарийін TXT файлы етіп жүктеп алу", story_package, file_name=f"story_{s_title_clean}_{story_lang}.txt", key="dl_story_m")







