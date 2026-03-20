# 14.1 Multimodalidad: Modelos de Visión y Lenguaje (VLM)

Durante meses, los modelos de Inteligencia Artificial solo comprendían un idioma: el texto. Pero para el año 2024, la revolución multimodal ha dominado la industria.

La librería de `transformers` soporta arquitecturas increíbles conocidas como **Vision-Language Models (VLM)**. Estos son modelos de lenguaje, pero que tienen "ojos", permitiéndote combinar texto y píxeles en el mismo código sin despeinarse.

## Casos de Uso
1. **Accesibilidad:** Leer descripciones de imágenes en voz alta a personas con deficiencia visual (Blind Assist).
2. **Análisis Automático:** Tu tienda online tiene millones de fotos subidas por los usuarios. Un VLM puede etiquetarlas, clasificarlas y censurar las inapropiadas, todo de manera instantánea.
3. **Lectura de Documentos y Facturas:** Le pasas el modelo la foto del recibo físico en PDF o papel y le preguntas: *"¿Cuánto es el total de la compra?"* (Modelos de Document-QA).

## Nomenclaturas Relevantes
Si entras al Hub de Hugging Face a buscar modelos de Visión multimodales, los nombres más populares y potentes de código abierto que debes investigar en el futuro son:
- **LlaVA:** Uno de los primeros y más versátiles LLMs de visión en código abierto (basado en arquitecturas Llama).
- **Qwen-VL:** Los modelos chinos más impresionantes para razonar sobre fotografías (Alibaba).
- **BLIP:** Excelente modelo de Salesforce ideal para describir imágenes (Image Captioning) con muy pocos recursos.

---
En el archivo `01_analizar_imagen.py` utilizaremos un modelo pre-configurado de Image Captioning (descripción visual). Te darás cuenta de que la sintaxis de Hugging Face... ¡sigue siendo exactamente la misma que aprendimos con texto en el Módulo 2!
