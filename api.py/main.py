from pydantic import BaseModel
from transformers import WhisperForConditionalGeneration, WhisperProcessor, WhisperTokenizer, pipeline, WhisperFeatureExtractor
import base64

feature_extractor = WhisperFeatureExtractor.from_pretrained("Sanyam0605/whisper-large-v2-hi")
model = WhisperForConditionalGeneration.from_pretrained("Sanyam0605/whisper-large-v2-hi")
tokenizer = WhisperTokenizer.from_pretrained("Sanyam0605/whisper-large-v2-hi", language="Hindi", task="transcribe")
pipe = pipeline('automatic-speech-recognition', model=model, tokenizer=tokenizer, feature_extractor=feature_extractor)

class Item(BaseModel):
    audio: str


def predict(item, run_id ,logger):
    item = Item(**item)

    if not item.audio:
        logger.info('User did not send specific parameter in request')
        return {"status_code": 422}  # returns a 422 status code

    decoded_data = base64.b64decode(item.audio)
    text = pipe(decoded_data)["text"]
    return {"transcribed_text": text}
