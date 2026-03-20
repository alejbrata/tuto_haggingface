# 7.0 La Revolución del Text-to-Image (Diffusers)

Hasta este módulo del curso nos habíamos centrado en entender y generar **textos**. Sin embargo, la revolución más visual de la IA llegó con la democratización de la generación de imágenes a raíz de "DALL-E", "Midjourney" y "Stable Diffusion".

Para lidiar con las imágenes, la gente de Hugging Face decidió crear una librería separada pero muy parecida a `transformers`. Esta se llama **`diffusers`**.

## ¿Qué es la "Difusión" (Diffusion)?
Los modelos como *Stable Diffusion* funcionan de manera algo contraintuitiva pero brillante:
1. El modelo empieza con una imagen de **ruido total** (como la nieve o estática gris de las televisiones antiguas).
2. Tienen un "Tokenizer Textual" que lee la frase que tú escribiste (ej: *"Un perro espacial"*).
3. A través de varios pasos matemáticos (iteraciones), la IA va "restando ruido" a la imagen gradualmente, dejando como resultado un dibujo que encaja con tu texto.

## ¿Qué nos ofrece `StableDiffusionPipeline`?
Igual que teníamos el `pipeline` de texto, en la librería `diffusers` tenemos su análogo.
Es un envoltorio (wrapper) de alto nivel que:
- Carga el sub-modelo generador.
- Transforma nuestro texto a un vector.
- Resta el ruido matemáticamente en bucle.
- Y devuelve una imagen perfecta en formato PIL (Pillow de Python) para que la guardemos.

---
En el archivo `01_generar_imagenes.py` utilizaremos el modelo tradicional de **Stable Diffusion 1.5**. Verás que en lugar de usar la librería `transformers`, importamos desde `diffusers`.
