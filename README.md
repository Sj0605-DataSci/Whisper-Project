# Whisper-Project
Finetuned  with 200 epochs and other training params, finetune Large V2 OpenAI Whisper for Google Fleurs on Hindi subset with colab pro and finally deploying it for inference on hugging face, for cpu

You can checkout the HuggingFace repository [here](https://huggingface.co/Sanyam0605/whisper-large-v2-hi). ( for cpu - use inference end point of hf )

[Api.py](https://github.com/Sj0605-DataSci/Whisper-Synth-DL_Intern/tree/main/api.py) defines the endpoint and deployment code. 
( for gpu - use inference end point of Cerebrium )

For deployment purposes and to get an A10 gpu, i used cerebrium's cortex service, Mike founder of Cerebrium, helped me in setting it up via discord

[audiotest](https://github.com/Sj0605-DataSci/Whisper-Synth-DL_Intern/tree/main/audiotest) contains some sample testing code. You can use that to get inference result from the model. (Make sure to change the path to audio file!)
