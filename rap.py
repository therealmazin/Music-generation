import requests

base_url = 'https://suno-api-flax.vercel.app'

def generate_audio_by_prompt(payload):
    url = f"{base_url}/api/generate"
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    print(response.text, response.status_code)
    try:
        return response.json()
    except ValueError:
        print("Non-JSON response received:", response.text)
        return None
    
def get_audio_information(audio_ids):
    url = f"{base_url}/api/get?ids={audio_ids}"
    response = requests.get(url)
    try:
        return response.json()
    except ValueError:
        print(f"Non-JSON response received for audio information: {response.text}")
        return None

# def convert_to_wav(audio_id):
#     url = f"{base_url}/api/gen/{audio_id}/convert_wav/"
#     response = requests.post(url)
#     try:
#         return response.json()
#     except ValueError:
#         print(f"Non-JSON response received for convert to wav: {response.text}")
#         return None

# def get_wav_file_url(audio_id):
#     url = f"{base_url}/api/gen/{audio_id}/wav_file/"
#     response = requests.get(url)
#     try:
#         return response.json()
#     except ValueError:
#         print(f"Non-JSON response received for wav file url: {response.text}")
#         return None

# def download_audio(url, file_name):
#     response = requests.get(url)
#     with open(file_name, 'wb') as f:
#         f.write(response.content)

# def process_audio_generation(payload):
#     data = generate_audio_by_prompt(payload)
    
#     if not data:
#         return "Failed to generate audio from prompt", None
    
#     ids = f"{data[0]['id']},{data[1]['id']}"
#     print(f"ids: {ids}")