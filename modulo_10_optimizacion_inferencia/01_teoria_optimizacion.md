# 10.0 Optimización de Inferencia: Haciendo que los gigantes quepan en tu PC

Una vez que has elegido o entrenado un modelo excelente, te enfrentarás al mayor problema del despliegue en producción: **Los Modelos de Lenguaje (LLMs) son monstruosamente pesados.**

Si quieres usar un modelo LlaMA-3 de 8 billones de parámetros, por defecto ocupará unos **16 GB de RAM de Video (VRAM)**. Una tarjeta gráfica con esa capacidad es muy cara.

¿Cómo resolvemos esto y aceleramos el modelo? Usando **Técnicas de Optimización de Inferencia**.

## 1. Precisión Reducida (Half-Precision / fp16)
Por defecto, las matemáticas de los modelos se calculan usando números de alta precisión (`float32`).
Si "recortamos" los decimales de esos cálculos y los convertimos a `float16`, **recortamos el peso del modelo a la MITAD (50%)**, y en la práctica, la IA no se vuelve más boba ni pierde calidad apenas.
- En Hugging Face, se hace pasando el argumento `torch_dtype=torch.float16` al cargar el modelo.

## 2. Cuantización (BitsAndBytes / QLoRA)
Esta es la revolución que permitió a la gente correr ChatGPTs caseros en sus teléfonos.
La cuantización "comprime" los parámetros matemáticos del modelo. En lugar de usar `float16`, los comprime a un formato de **8 bits** o incluso **4 bits**.
- **Resultado:** ¡Un modelo que pesaba 16 GB ahora pesa solo 4 GB!
- **Librería Clave:** HF usa la librería externa `bitsandbytes`.

## 3. Flash Attention
Es un algoritmo matemático optimizado a nivel de hardware. Simplemente "encendiéndolo" en Hugging Face (requiere librerías y GPUs modernas), el modelo lee textos largos mucho más rápido y usando menos memoria.

---
En nuestro último script, `02_ejemplo_cuantizacion.py`, veremos cómo cargar un modelo pidiéndole a Hugging Face que lo comprima automáticamente durante la descarga.
