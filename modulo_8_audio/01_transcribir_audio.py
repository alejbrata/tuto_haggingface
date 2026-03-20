from transformers import pipeline
from datasets import load_dataset
import warnings
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"
warnings.filterwarnings('ignore')

print("¡Vamos a transcribir voz humana (Audios) usando Whisper!\n")

# Para probar este código necesitamos un audio real.
# En lugar de obligarte a descargar un archivo wav/mp3 tú mismo manualmene,
# vamos usar un mini-dataset de HF que ya contiene audios precargados de demostración.
print("Descargando un archivo de audio corto desde Hugging Face Datasets...")
ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")

# Obtenemos el primer audio del dataset
archivo_de_audio = ds[0]["audio"]["array"]
frecuencia_muestreo = ds[0]["audio"]["sampling_rate"]

print("\nCargando modelo Whisper de OpenAI...")
# Usamos el modelo "tiny" que es rapídisimo y sirve como demostración
# Whisper es brutal para transcribir audios, traducir podcasts enteros y poner subtítulos
transcriptor = pipeline(
    "automatic-speech-recognition", 
    model="openai/whisper-tiny"
)

print("\nTranscribiendo...")

# Whisper recibe el audio convertido en números y detecta automáticamente el idioma y las palabras
resultado = transcriptor(
    {"sampling_rate": frecuencia_muestreo, "raw": archivo_de_audio}
)

print("-" * 50)
print("Texto Transcrito por la Inteligencia Artificial:")
print(f"'{resultado['text']}'")
print("-" * 50)
