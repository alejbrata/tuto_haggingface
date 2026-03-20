# 1.2 Instalación y Configuración del Entorno

Ahora que sabemos qué es Hugging Face y por qué es tan poderoso, necesitamos preparar nuestra "caja de herramientas". 

Vamos a trabajar principalmente en Python. Para usar el ecosistema de Hugging Face de forma local, necesitamos instalar un par de librerías esenciales. En este curso dejaremos un archivo `requirements.txt` pre-configurado para que esto sea muy sencillo.

## Las librerías que vamos a instalar:

1. **`transformers`**: La librería estrella de Hugging Face. Es la API que nos permitirá interactuar con los modelos con muy poco código.
2. **`torch` (PyTorch)**: Los modelos de IA son gigantescas redes neuronales matemáticas. PyTorch es el "motor" que hace todos esos cálculos complejos por debajo. Hugging Face necesita estar sobre un motor (PyTorch es el más popular, seguido de TensorFlow).
3. **`datasets`**: Una librería muy útil de Hugging Face que nos permitirá descargar colecciones enormes de texto o imágenes para probar nuestros modelos.
4. **`accelerate`**: Ayuda a que el código se ejecute de manera eficiente, especialmente si en un futuro tienes una tarjeta gráfica (GPU) para acelerar la IA.

## Próximos pasos prácticos

He automatizado la creación de un entorno virtual para ti y la instalación de estas librerías.

Un entorno virtual es como una carpeta aislada en tu ordenador donde se instalan las herramientas de Python sin afectar a otras cosas que tengas instaladas en tu sistema.

¡Si todo está instalado correctamente, estaremos listos para ir al **Módulo 2** y escribir nuestras primeras 3 líneas de código de IA!
