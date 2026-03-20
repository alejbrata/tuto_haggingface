from transformers import pipeline
import warnings

# Ignorar advertencias menores que a veces muestra la librería
warnings.filterwarnings('ignore')

print("Descargando/Cargando el pipeline de análisis de sentimiento...")
print("(La primera vez puede tardar un poco mientras descarga el modelo predeterminado)\n")

# 1. Crear el pipeline
# Usamos `model="nlptown/bert-base-multilingual-uncased-sentiment"` porque 
# el modelo por defecto está en inglés. Este modelo entiende español.
clasificador = pipeline(
    "sentiment-analysis", 
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

# 2. Textos a analizar
textos = [
    "¡Me encanta este curso de Inteligencia Artificial! Es increíble.",
    "El servicio al cliente de esta empresa es terrible, no vuelvo a comprar aquí.",
    "Hoy está nublado y la temperatura es de 20 grados."
]

# 3. Analizar e imprimir resultados
for texto in textos:
    # El pipeline nos devuelve una lista con un diccionario
    resultado = clasificador(texto)[0] 
    
    # El modelo que hemos elegido devuelve 'estrellas' (1 star a 5 stars)
    print(f"Texto: '{texto}'")
    print(f"Clasificación: {resultado['label']} con una confianza del {resultado['score']:.2f}")
    print("-" * 50)

print("\n¡Felicidades! Acabas de ejecutar tu primer modelo de NLP (Procesamiento de Lenguaje Natural).")
