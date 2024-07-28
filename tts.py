from transformers import AutoProcessor, BarkModel
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
processor = AutoProcessor.from_pretrained("suno/bark")

model = BarkModel.from_pretrained("suno/bark").to(device)
model = model.to_bettertransformer()
model.enable_cpu_offload()

txt = "Sim, você provavelmente está se referindo ao personagem Sonic the Hedgehog da série de jogos de vídeo game com o mesmo nome. Embora Sonic não seja exatamente descrito como um \"furry\" no sentido tradicional da subcultura furry, ele é um personagem antropomórfico azul que assemelha-se a um ouriço e coleta anéis dourados ao longo dos níveis nos jogos."
voice_preset = "v2/pt_speaker_5"

inputs = processor(txt, voice_preset=voice_preset)
inputs = inputs.to(device)

audio_array = model.generate(**inputs)
audio_array = audio_array.cpu().numpy().squeeze()

# from IPython.display import Audio

# sample_rate = model.generation_config.sample_rate
# Audio(audio_array, rate=sample_rate)

import scipy

sample_rate = model.generation_config.sample_rate
scipy.io.wavfile.write("output.wav", rate=sample_rate, data=audio_array)
