from transformers import pipeline
import warnings
import os

# Esto ayuda a evitar algunos mensajes de error de paralelismo en Windows/Mac
os.environ["TOKENIZERS_PARALLELISM"] = "false"
warnings.filterwarnings('ignore')

print("Cargando el pipeline de generación de texto...")
print("(Estamos usando DeepSeek/Qwen o un modelo pequeño en español/inglés)\n")

# Aquí usamos "text-generation".
# Para que funcione rápido en tu PC sin GPU, usaremos un modelo muy pequeñito 
# llamado "DeepPavlov/rubert-base-cased" u otro ligero. 
# En este caso usaremos "datificate/gpt2-small-spanish", que es un GPT2 entrenado en español.
generador = pipeline(
    "text-generation", 
    model="datificate/gpt2-small-spanish"
)

prompt = "El futuro de la inteligencia artificial es"

print(f"Texto inicial (Prompt): '{prompt}'")
print("\nGenerando continuación (esto puede tomar unos segundos)...\n")

# Parámetros comunes:
# - max_length: número máximo de tokens (palabras/sílabas) a generar
# - num_return_sequences: cuántas opciones diferentes queremos
# - temperature: "creatividad" del modelo (más alto = más creativo/loco, más bajo = más predecible)
resultados = generador(
    prompt, 
    max_length=50, 
    num_return_sequences=1,
    temperature=0.7,
    truncation=True
)

for resultado in resultados:
    print("--------------------------------------------------")
    print(resultado['generated_text'])
    print("--------------------------------------------------")
