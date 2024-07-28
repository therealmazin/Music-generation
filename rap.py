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
