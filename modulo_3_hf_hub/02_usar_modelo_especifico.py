from transformers import pipeline
import warnings
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"
warnings.filterwarnings('ignore')

print("Descargando un modelo específico desde el Hub...")
print("Vamos a usar un modelo entrenado específicamente para detectar noticias falsas (Fake News) en español.\n")

# Supongamos que fuiste a huggingface.co/models
# Filtras por Tarea: "Text Classification" y Lenguaje: "Spanish"
# Encontraste un modelo creado por la organización "PlanTL-GOB-ES" o "Verificada" 
# (Aquí usaremos un clasificador multilingüe genérico como ejemplo práctico de zero-shot o un modelo de emociones)
#
# Para este ejemplo utilicemos un modelo que detecta una EMOCIÓN específica.
# ID del modelo en el Hub: "pysentimiento/robertuito-emotion-analysis" (entrenado en tuits en español)

modelo_hub_id = "pysentimiento/robertuito-emotion-analysis"

clasificador_emociones = pipeline(
    "text-classification", 
    model=modelo_hub_id
)

textos = [
    "¡Gané la lotería! No me lo puedo creer, estoy saltando de alegría.",
    "Perdí a mi perro hoy. No dejo de llorar, qué dolor tan grande.",
    "Si vuelves a tocar mi computadora, te las verás conmigo."
]

for texto in textos:
    resultado = clasificador_emociones(texto)[0]
    print(f"Texto: '{texto}'")
    # Este modelo devuelve etiquetas como 'joy' (alegría), 'sadness' (tristeza), 'anger' (ira), etc.
    print(f"Emoción predominante: {resultado['label']} (Confianza: {resultado['score']:.2f})")
    print("-" * 50)
    print(resultado)
