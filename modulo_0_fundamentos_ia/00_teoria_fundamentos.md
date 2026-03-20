# 0.0 Los Fundamentos: Antes de Programar, Entender

Es imposible disfrutar construyendo la casa por el tejado. Si vas a usar tecnología punta de Hugging Face en los siguientes módulos, primero debes entender la jerga de la industria y la historia de cómo llegamos hasta aquí.

¡Empecemos desde el principio!

## 1. ¿Qué demonios es el NLP?
**NLP** significa *Natural Language Processing* (Procesamiento de Lenguaje Natural).
- Durante décadas, los ordenadores solo entendían matemáticas y comandos (`if a > b:`).
- El NLP es el campo científico de la Inteligencia Artificial que se dedica a intentar **que las máquinas entiendan y hablen los idiomas humanos** (español, inglés, chino...) igual que nosotros.

## 2. El Antes y el Después: El nacimiento del "Transformer"
En el año 2017 casi todo el NLP fallaba olímpicamente si escribías frases raras. 
Pero ese año, Google publicó un *paper* (un documento científico) revolucionario llamado *"Attention is All You Need"* (La atención es todo lo que necesitas).

En este documento, inventaron una arquitectura cerebral nueva para la IA llamada **Transformer**.
A diferencia de los modelos antiguos, que leían palabra por palabra aburriéndose de lo que leyeron al principio, el Transformer usa el **"Mecanismo de Atención"**. Puede mirar todas las palabras de tu frase al mismo tiempo y descubrir qué palabra importa más. Por ejemplo, en *"El banco del parque es verde y el banco de dinero está cerrado"*, sabe que ambos "bancos" son cosas radicalmente distintas.

## 3. Las dos mitades del cerebro: Encoders y Decoders
La arquitectura Transformer original se compone de dos piezas: un **Encoder** y un **Decoder**.

- **El Encoder (El que lee y entiende):**
  - Su trabajo es tragar texto y deducir profundamente de qué habla. Mira hacia atrás y hacia adelante en la frase.
  - *Modelo famoso de tipo Encoder:* **BERT** de Google (2018).
  - *Uso:* Excelente para Análisis de Sentimientos o Clasificar textos.

- **El Decoder (El que habla e inventa):**
  - Su trabajo es tomar contexto y adivinar "cuál es la siguiente palabra".
  - *Modelo famoso de tipo Decoder:* **GPT** de OpenAI (Generative Pre-trained Transformer).
  - *Uso:* Excelente para escribir artículos, chatear y mantener conversaciones de forma creativa.

A partir del nacimiento del Transformer en 2017, la empresa Hugging Face se fundó para empaquetar en Python estas arquitecturas y que no tuvieras que ser un doctor en Matemáticas para usarlas.

## 4. El monstruo final: ¿Qué es un LLM?
Un **LLM** (*Large Language Model* o Modelo de Lenguaje Grande) no es magia negra. 
Es simplemente una arquitectura Transformer (generalmente un **Decoder** como la familia de *GPT*, *Llama* o *Qwen*) que se ha entrenado con **literalmente todo internet entero**.

Tienen "Grandes" en el título porque, en lugar de pesar unos pocos megabytes y tener un millón de parámetros (neuronas), están compuestos por **miles de billones de parámetros** y se entrenaron gastando millones de dólares en electricidad usando el hardware más avanzado del mundo.

---
Con esta jerga clara (*NLP*, *Transformers*, *Encoder/Decoder*, *LLM*), ahora estás plenamente preparado para ir al **Módulo 1** y empezar a invocar y a conectarte con estos cerebros artificiales en tu ordenador usando Python.
