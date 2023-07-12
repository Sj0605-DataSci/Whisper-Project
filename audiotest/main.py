import requests
import json
import base64


endpoint = "https://run.cerebrium.ai/v2/p-efe0c57a/synth/predict"

audio_path = r"<PATH/TO/AUDIO/FILE>" # Tested with .mp3 files

data = base64.b64encode(open(audio_path, 'rb').read())
data_str = data.decode('utf-8')
payload = json.dumps({"audio": data_str})

headers = {
    'Authorization': 'public-3d51ef810fee14d89fe3',
    'Content-Type': 'application/json'
}

response = requests.request("POST", endpoint, headers=headers, data=payload)

print(response.text)
