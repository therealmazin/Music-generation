## README

# Music, Instrumental, and Lyrics Generator

This project is a web application for generating music, instrumentals, and rap lyrics. It uses various APIs and models to create content based on user input. 

## Features

- **Music Generation**: Generate music based on a text prompt describing the desired beat and lyrics.
- **Instrumental Generation**: Create instrumentals based on a specified style.
- **Lyrics Generation**: Generate rap lyrics and a rap name based on the user's city of birth.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/theralmazin/Music-generator.git
   cd Music-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

### Music Generation

1. Select "Music" from the sidebar.
2. Enter a prompt describing the type of beat and lyrics you want.
   Example: `"A classic 90's hip hop track with heavy 808 and snares. The lyrics reflect on urban life and social issues, delivered with a gangster flow by a black male MC."`
3. Click "Generate Music".
4. Wait for the music to be generated. This process can take 3-4 minutes.
5. The generated audio URLs will be displayed once the process is complete.
![alt text][<img width="1512" alt="Screenshot 2024-07-27 at 9 23 24 PM" src="https://github.com/user-attachments/assets/1c458c01-0012-4684-a071-a80cd12bb187">
]

### Instrumental Generation

1. Select "Instrumental" from the sidebar.
2. Enter a prompt describing the style of beat you want.
   Example: `"West Coast style hip hop beat with heavy 808 and drums"`
3. Click "Generate Instrumental".
4. Wait for the instrumental to be generated. This process can take 3-4 minutes.
5. The generated instrumental will be available for playback in the app.

### Lyrics Generation

1. Select "Lyrics" from the sidebar.
2. Enter the city you were born in.
3. Click "Generate Lyrics".
4. The generated rap name and lyrics will be displayed.

## File Structure

- `app.py`: Main application file containing the Streamlit app.
- `requirements.txt`: List of dependencies required to run the app.

## Dependencies

- Streamlit
- time
- langchain_temp (custom module)
- beat (custom module)
- rap (custom module)

