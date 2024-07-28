import streamlit as st
import time
import langchain_temp
from beat import instrumental_generation
from rap import generate_audio_by_prompt, get_audio_information




music = st.sidebar.selectbox("Music & Instrumental Generation",("Music","Instrumental","Lyrics"))

if music == "Music":
    st.title("Music Generator")
    prompt = st.text_input("Please write down on what type of beat you want, along with what song are you going for ", "A classic 90's hip hop track with heavy 808 and snares. The lyrics reflect on urban life and social issues, delivered with a gangster flow by a black male MC.")
        
    
    if st.button("Generate Music"):
        with st.spinner("Generating Music. Please kindly wait for 3-4 minutes"):
            payload = {
                "prompt": prompt,
                "make_instrumental": False,
                "wait_audio": False
            }
            data = generate_audio_by_prompt(payload)

            if not data:
                st.error("Failed to generate audio from prompt")
            else:
                ids = f"{data[0]['id']},{data[1]['id']}"
                st.write(f"Generated IDs: {ids}")

                # Polling to get the audio streaming URLs
                for _ in range(60):
                    data = get_audio_information(ids)
                    if data and data[0]["status"] == 'streaming':
                        audio_url_1 = data[0]['audio_url']
                        audio_url_2 = data[1]['audio_url']
                        st.write(f"Audio URL 1: {audio_url_1}")
                        st.write(f"Audio URL 2: {audio_url_2}")
                        break
                    time.sleep(5)


            st.success("Music generated successfully")




elif music == "Instrumental":
    st.title("Instrumental Generation")

    prompt = st.text_input("Enter the style of beat u want","West Coast style hip hop beat with heavy 808 and drums")

    if st.button("Generate Instrumental"):
        with st.spinner("Generating instrumental. Please kindly wait for 3-4 minutes"):
            output_file= instrumental_generation(prompt)
            st.success("Instrumental generated successfully")
            st.audio(output_file,format="audio/wav")

else:
    st.title("Lyrics Generation")
    st.write("This model here generates a rap name based on your city along with lyrics")
    city= st.text_input("Type which city you were born in","Bangalore,India")
    if st.button("Generate Lyrics"):
        response= langchain_temp.gen_rap_name_and_lyrics(city)
        st.success("Generate Lyrics")
        st.header(response["rap_name"].strip())
        rap_lyrics = response['lyrics'].strip().split("\n")
        st.write("Lyrics by",response["rap_name"])
        for lyric in rap_lyrics:
            st.write(lyric)






            
