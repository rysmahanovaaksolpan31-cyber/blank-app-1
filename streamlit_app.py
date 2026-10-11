import streamlit as st

st.set_page_config(page_title="Music & Story AI Studio", page_icon="🎵")

st.title("🎵 Music & Story AI Studio")
st.write("Сілтеме немесе трек аты бойынша 3 түрлі нұсқада Suno AI промпты мен ән мәтінін дайындау.")

# 1. Енгізу өрісі
song_input = st.text_input("🔗 Әннің сілтемесін (YouTube/Spotify) немесе атын жазыңыз:")

# 2. Тілді таңдау
language = st.selectbox("🌐 Ән мәтіні қай тілде дайындалсын?", ["Қазақша", "Русский", "English"])

# 3. Батырма
if st.button("✨ 3 түрлі нұсқада музыка дайындау"):
    if song_input.strip() == "":
        st.warning("Өтініш, ән атын немесе сілтемесін енгізіңіз!")
    else:
        st.success(f"'{song_input}' бойынша {language} тілінде 3 нұсқа дайындалды!")
        
        # Тілге байланысты дайын шаблон мәтіндерді құрастыру логикасы
        if language == "Русский":
            lyrics_1 = "[Verse 1]\nНочной ритм, глубокое чувство как шторм...\n\n[Chorus]\nВремя уходит, нам не подчиняясь..."
            lyrics_2 = "[Verse 1]\nТихий вечер, звезды горят в тишине...\n\n[Chorus]\nТы мой свет, ты моя мечта..."
            lyrics_3 = "[Verse 1]\nВспышки света, ритм биения сердца...\n\n[Chorus]\nТанцуй со мной до самого утра..."
        elif language == "English":
            lyrics_1 = "[Verse 1]\nNight rhythm, deep feeling like a storm...\n\n[Chorus]\nTime goes by, running out of control..."
            lyrics_2 = "[Verse 2]\nQuiet evening, stars shining in the dark...\n\n[Chorus]\nYou are my light, you are my dream..."
            lyrics_3 = "[Verse 1]\nFlashing lights, heart beating to the rhythm...\n\n[Chorus]\nDance with me until the morning comes..."
        else: # Қазақша
            lyrics_1 = "[Verse 1]\nТүнгі ырғақ, терең сезім дауылдай...\n\n[Chorus]\nӨтіп жатыр уақыт бізге бағынбай..."
            lyrics_2 = "[Verse 1]\nТүнгі қала, жұлдыздар жанады сырлы...\n\n[Chorus]\nСен менің арманым, сезімнің нұры..."
            lyrics_3 = "[Verse 1]\nЖарық сәуле, жүректің соғысы қатты...\n\n[Chorus]\nБиле өзіммен таң атырғанша татты..."

        # Табтар (Нұсқалар)
        tab1, tab2, tab3 = st.tabs(["🔥 1-нұсқа (Organic Deep House)", "💖 2-нұсқа (Romantic Pop)", "⚡ 3-нұсқа (Club Dance)"])

        with tab1:
            st.subheader("📝 Suno AI Промпт:")
            prompt1 = "Organic Deep House, atmospheric pads, catchy bass, emotional male vocals, 120 BPM"
            st.code(prompt1)
            
            st.subheader(f"📜 Ән мәтіні ({language}):")
            st.text_area("1-нұсқа мәтіні:", lyrics_1, height=180)
            
            txt_data1 = f"PROMPT:\n{prompt1}\n\nLYRICS:\n{lyrics_1}"
            st.download_button("💾 1-нұсқаны TXT файлы етіп жүктеп алу", txt_data1, file_name=f"music_version_1_{language}.txt")

        with tab2:
            st.subheader("📝 Suno AI Промпт:")
            prompt2 = "Romantic Pop, acoustic guitar, soft piano, warm male vocals, emotional beat, 95 BPM"
            st.code(prompt2)
            
            st.subheader(f"📜 Ән мәтіні ({language}):")
            st.text_area("2-нұсқа мәтіні:", lyrics_2, height=180)
            
            txt_data2 = f"PROMPT:\n{prompt2}\n\nLYRICS:\n{lyrics_2}"
            st.download_button("💾 2-нұсқаны TXT файлы етіп жүктеп алу", txt_data2, file_name=f"music_version_2_{language}.txt")

        with tab3:
            st.subheader("📝 Suno AI Промпт:")
            prompt3 = "Energetic Dance Pop, synthwave bass, modern electropop vocals, upbeat drive, 128 BPM"
            st.code(prompt3)
            
            st.subheader(f"📜 Ән мәтіні ({language}):")
            st.text_area("3-нұсқа мәтіні:", lyrics_3, height=180)
            
            txt_data3 = f"PROMPT:\n{prompt3}\n\nLYRICS:\n{lyrics_3}"
            st.download_button("💾 3-нұсқаны TXT файлы етіп жүктеп алу", txt_data3, file_name=f"music_version_3_{language}.txt")




