# 4.1 La anatomía de un modelo de IA: Tokenizers y AutoModel

Hasta ahora hemos usado `pipeline`, que nos ocultaba toda la complejidad técnica. Pero si quieres crear aplicaciones reales e integrarlas en tus sistemas, necesitas entender qué ocurre "debajo del capó".

Hay dos protagonistas principales en cualquier interacción con un modelo de NLP (Lenguaje Natural):
1. **El Tokenizer**
2. **El Modelo**

## El Tokenizer: El traductor al idioma de las máquinas
Los modelos matemáticos (las redes neuronales) no entienden texto (ni letras, ni palabras). ¡Solo entienden números (tensores/vectores)!

La función del Tokenizer es **dividir tu texto en trocitos pequeños (tokens)** y luego convertir esos fragmentos en números.

*Ejemplo:*
- Texto: "Hugging Face es la mejor herramienta!"
- Tokens (trozos): ["Hugging", " Face", " es", " la", " me", "jor", " herramienta", "!"]
- IDs (números): [1234, 560, 4, 8, 90, 12, 599, 9]

> **Regla de Oro:** Cada modelo fue entrenado con un tokenizer en particular. SIEMPRE debes usar el tokenizer exacto asociado al modelo que quieres utilizar. Si no lo haces, los números no coincidirán con las palabras y el modelo dará respuestas sin sentido.

## El Modelo (AutoModel)
Una vez el Tokenizer convierte las palabras en números, se los pasamos al modelo. El modelo hace millones de cálculos matriciales y nos devuelve otro conjunto de números (que representan probabilidades o predicciones). 

## Hugging Face al rescate: Las clases `Auto*`
Para facilitarnos la vida sin usar `pipeline`, Hugging Face ofrece las clases "Auto" (`AutoTokenizer` y `AutoModel`).
Tú solo le pasas el ID del modelo del Hub, y estas clases detectan automáticamente qué arquitectura de red descargar y qué diccionario de palabras usar.

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

id_modelo = "nlptown/bert-base-multilingual-uncased-sentiment"

# Descarga el Tokenizer correcto
tokenizer = AutoTokenizer.from_pretrained(id_modelo)

# Descarga el Modelo con la "cabeza" de clasificación (para decirnos estrellas/sentimiento)
modelo = AutoModelForSequenceClassification.from_pretrained(id_modelo)
```

En el siguiente script (4.2), replicaremos lo que hacía el pipeline de análisis de sentimiento, pero **escribiendo nosotros mismos el proceso manual**. Esto te dará todo el control sobre cómo procesar lotes grandes de datos o manejar salidas personalizadas.
