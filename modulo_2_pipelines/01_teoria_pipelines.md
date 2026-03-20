# 2.1 La magia de `pipeline`

La herramienta más poderosa y sencilla de la librería `transformers` es la función `pipeline`.

## ¿Qué es un `pipeline`?
Imagina un "pipeline" (tubería) como una caja negra que hace tres cosas por ti automáticamente:
1. **Pre-procesamiento (Tokenizer):** Toma tu texto (ej. "¡Hola mundo!") y lo convierte en números que el modelo matemático puede entender.
2. **El Modelo:** Pasa esos números por el modelo de IA (la red neuronal) para obtener las predicciones.
3. **Post-procesamiento:** Convierte la salida matemática del modelo de vuelta a algo que los humanos podamos entender (ej. "Sentimiento: Positivo").

Si no existiera `pipeline`, tendrías que escribir código separado y bastante complejo para cada uno de estos tres pasos. 

## ¿Para qué sirve?
Hugging Face ha pre-programado pipelines para decenas de tareas. Algunas de las más comunes son:
- **`sentiment-analysis`**: Detectar si un texto es positivo, negativo o neutral.
- **`text-generation`**: Completar un texto (como lo hace ChatGPT).
- **`translation`**: Traducir de un idioma a otro.
- **`summarization`**: Resumir un texto largo.
- **`image-classification`**: Decir qué hay en una imagen.
- **`automatic-speech-recognition`**: Transcribir audio a texto (Whisper).

¡La sintaxis siempre es la misma! Solo cambias el nombre de la tarea.

```python
from transformers import pipeline

# 1. Creas el pipeline diciendo qué tarea quieres
clasificador = pipeline("sentiment-analysis")

# 2. Le pasas tu texto
resultado = clasificador("¡Estoy aprendiendo mucho hoy!")
print(resultado)
```

En los siguientes scripts de Python, vamos a ejecutar este código real en tu máquina. Ve al archivo `02_analisis_sentimiento.py` para tu primera prueba.
