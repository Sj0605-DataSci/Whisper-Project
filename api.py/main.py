from pydantic import BaseModel
from transformers import WhisperForConditionalGeneration, WhisperProcessor, WhisperTokenizer, pipeline, WhisperFeatureExtractor
import base64

feature_extractor = WhisperFeatureExtractor.from_pretrained("Sanyam0605/whisper-large-v2-hi")
model = WhisperForConditionalGeneration.from_pretrained("Sanyam0605/whisper-large-v2-hi")
tokenizer = WhisperTokenizer.from_pretrained("Sanyam0605/whisper-large-v2-hi", language="Hindi", task="transcribe")
# processor = WhisperProcessor.from_pretrained("Sanyam0605/whisper-large-v2-hi")
pipe = pipeline('automatic-speech-recognition', model=model, tokenizer=tokenizer, feature_extractor=feature_extractor)

DOWNLOAD_ROOT = './audio_files'
class Item(BaseModel):
    audio: str


def predict(item, run_id ,logger):
    item = Item(**item)

    if not item.audio:
        logger.info('User did not send specific parameter in request')
        return {"status_code": 422}  # returns a 422 status code

    decoded_data = base64.b64decode(item.audio)

    # filename = f"{DOWNLOAD_ROOT}/tmp.mp3"
    #
    # with open(filename, "wb") as file:
    #     file.write(decoded_data)
    #
    # logger.info("Decoding base64 to file was successful")
    text = pipe(decoded_data)["text"]

    # Do something with parameters from item

    return {"transcribed_text": text}
