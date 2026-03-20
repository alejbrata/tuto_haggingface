# 3.1 Explorando el Hugging Face Hub

En el módulo anterior usamos `pipeline` y vimos que le pasamos un parámetro llamado `model` (como `nlptown/bert-base-multilingual-uncased-sentiment`). Pero, ¿de dónde sale ese nombre?

Bienvenido al **Hugging Face Hub** (https://huggingface.co/models).

El Hub es un repositorio web enorme donde la comunidad e investigadores suben sus modelos entrenados. Piensa en ello como una tienda de aplicaciones gratuita para la IA.

## ¿Cómo encontrar el modelo adecuado?
Si entras a la web de Hugging Face y vas a la pestaña "Models", verás filtros a la izquierda. 

Los filtros más importantes son:
1. **Tasks (Tareas):** ¿Qué quieres hacer? (Text Classification, Token Classification, Text Generation, Image-to-Text, etc.)
2. **Languages (Idiomas):** Vital si quieres que el modelo entienda o hable español (filtra por `es` o `Spanish`).
3. **Licenses (Licencias):** Importante si vas a hacer un proyecto comercial para tu empresa (busca licencias permisivas como `MIT` o `Apache 2.0`).

## La tarjeta del modelo (Model Card)
Cuando haces clic en un modelo (ej. `dccuchile/bert-base-spanish-wwm-uncased`), vas a su "Model Card". Es como el manual de instrucciones. 
Ahí los creadores te explican:
- **Para qué sirve el modelo.**
- **Con qué datos se entrenó** (Ej: Toda la Wikipedia en español).
- **Limitaciones o sesgos** del modelo.
- **Pequeños ejemplos de código** de cómo usarlo.

## Nomenclatura común
Notarás que los modelos suelen nombrarse así: `creador/nombre-del-modelo`
Por ejemplo:
- `microsoft/resnet-50` (Creado por Microsoft, modelo ResNet-50)
- `meta-llama/Llama-2-7b` (Familia Llama de Meta)
- `PlanTL-GOB-ES/roberta-base-bne` (Modelo del Gobierno de España basado en RoBERTa)

---
Ve al siguiente archivo (`02_usar_modelo_especifico.py`) donde veremos cómo usar un modelo específico que nosotros mismos hemos seleccionado desde el Hub, pasándole el ID que sacamos de la página web.
