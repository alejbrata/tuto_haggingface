import gradio as gr
from transformers import pipeline
import warnings

warnings.filterwarnings('ignore')

print("Arrancando tu primera aplicación web en Gradio...")
print("Se abrirá un enlace local al final de la carga para que lo uses en tu navegador.\n")

# Cargamos el pipeline clásico de análisis de sentimiento
clasificador = pipeline(
    "sentiment-analysis", 
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

# Definimos una función simple de Python que Gradio utilizará
def predecir_sentimiento(texto):
    resultado = clasificador(texto)[0]
    etiqueta = resultado['label']
    confianza = round(resultado['score'] * 100, 2)
    return f"Resultado: {etiqueta} (Seguridad del modelo: {confianza}%)"

# Aquí empieza la magia de Gradio: 
# Crear una interfaz de usuario para tu función en UNA SOLA LÍNEA de código importante
interfaz = gr.Interface(
    fn=predecir_sentimiento,               # Función de Python 
    inputs=gr.Textbox(lines=4, placeholder="Escribe tu reseña o pensamiento aquí..."), # Caja de entrada
    outputs=gr.Text(label="Análisis del Modelo Hugging Face"),                        # Caja de salida
    title="Analizador de Sentimientos con Inteligencia Artificial 🤖",
    description="Escribe cualquier texto en español. El modelo predecirá de 1 a 5 estrellas cuán positivo o negativo es."
)

# Lanzamos el servidor web
# Nota: Si quisieras compartir esta web con amigos de otro país, solo añades `share=True` dentro del `launch()` 
# y Hugging Face te regalará una URL pública temporal válida por 72 horas.
interfaz.launch(share=False)
