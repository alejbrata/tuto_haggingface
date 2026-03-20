# 8.0 Dándole Oídos a la IA (Whisper)

La Inteligencia Artificial ha evolucionado para volverse **multimodal** (capaz de ver, escuchar y hablar). 
En este módulo trabajaremos con uno de los modelos más disruptivos construidos por *OpenAI* y portado a formato open-source en Hugging Face: **Whisper**.

## ¿Por qué Whisper es especial?
Históricamente, los algoritmos de transcripción de voz (ASR - *Automatic Speech Recognition*) eran lentos, caros y malísimos entendiendo a gente con acentos fuertes o con ruido de fondo ambiental.

Whisper se entrenó con nada menos que **680.000 horas** de audio (multilingüe) de la web. Esto lo hace impresionantemente robusto.

## Usos asombrosos de Whisper en tus proyectos
Si conoces cómo cargar este modelo en Hugging Face, puedes programar apps muy valiosas:
- **Subtitulado automático** de vídeos para tus redes sociales (transcribiendo con fechas de tiempo o "timestamps").
- Apps para médicos que **tomen notas de la consulta** escuchando de fondo.
- Transcribir **clases y reuniones enteras** de la universidad en pocos minutos.
- Tu propio **asistente de voz** (como Siri o Alexa) pero inteligente y casero.

## Trabajando con audios en HF
Al llamar al `pipeline` con la etiqueta `"automatic-speech-recognition"`, tú solo le das la ruta a un archivo de audio (ej: `.mp3`, `.wav`) y Hugging Face se encargará de extraer las ondas de audio, vectorizarlas y convertirlas a letras.

*(Importante: Generalmente requiere que tengas instalada la librería `soundfile` en tu entorno)*

---
Echa un vistazo al código práctico `01_transcribir_audio.py` donde el ordenador literalmente "escuchará" un audio desde HuggingFace Datasets.
