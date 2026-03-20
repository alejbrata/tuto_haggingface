# 6.1 El "Fine-Tuning" (Ajuste Fino)

¡Llegaste a la última lección teórica! 

Hasta ahora hemos aprendido a usar **Modelos Base** o **Pre-entrenados**. Es decir, aprovecharnos de las miles de horas y millones de dólares que alguien más gastó en entrenar una IA.

Pero a veces, el modelo pre-entrenado no sabe hacer exactamente lo que tú quieres.
- ¿Qué pasa si quieres que un modelo analice la jerga de los adolescentes de tu país?
- ¿O que un modelo médico analice electrocardiogramas locales?
- ¿O adaptar a Llama-3 para que responda siempre como el asistente amable de tu empresa, "Ticketia"?

Aquí es donde entra el **Fine-Tuning**.

## ¿Qué es?
Fine-Tuning es el proceso de tomar un modelo inteligente que ya sabe "hablar y razonar", y "darle un postgrado" o un curso intensivo sobre TUS datos y TU tarea específica.

En vez de entrenar desde cero (lo cual costaría millones), coges el modelo existente y le muestras miles de pares de ejemplos *(Entrada -> Salida esperada)* correspondientes a tu problema. Luego actualizas ligeramente sus "neuronas" matemáticas. 

## ¿Cómo se hace en Hugging Face?
Para hacer Fine-Tuning usarás otra clase súper poderosa de la librería `transformers` llamada `Trainer`.

1. **Creas tu conjunto de datos** usando la librería `datasets` (Módulo 5).
2. **Cargas el modelo y el tokenizer base** (Módulo 4).
3. **Usas la clase `Trainer`**, que es una configuración donde le dices cuántas veces quieres que el modelo lea los datos (épocas), qué tasa de aprendizaje (learning rate) usar, y le pasas el modelo + los datos.
4. Ejecutas `trainer.train()`. Y después de unas horas (y una buena tarjeta gráfica GPU)... ¡tienes un modelo 100% hecho a tu medida!

### Fine-Tuning tradicional vs Prompt Tuning

En los últimos años, hacer fine-tuning a modelos completos (con billones de parámetros) se ha vuelto extremadamente costoso computacionalmente. Por eso han nacido las técnicas **PEFT** (Parameter-Efficient Fine-Tuning), y entre ellas destaca el **Prompt Tuning**.

- **Fine-Tuning Completo:** Tomas todas las tuercas y engranajes del cerebro del modelo y las alteras. Requiere mucha memoria (múltiples GPUs gigantes).
- **Prompt Tuning:** En lugar de tocar el cerebro original del modelo, añades una pequeña "capa" adicional o un grupo de "tokens virtuales" al principio del texto de entrada que el modelo aprende a ajustar. Es decir, el modelo original se queda intacto (congelado), y solo cambias el *prompt interno* matemático para guiar sus respuestas. Esto permite entrenar modelos enormes en tu portátil o con una tarjeta gráfica normal de escritorio.

Cuando quieras explorar cómo hacer esto tú mismo en Hugging Face, busca la librería llamada **`peft`**, que permite hacer Prompt Tuning o LoRA sobre cualquier modelo de la biblioteca `transformers` de manera muy sencilla.

---
**¡Felicidades!** Has terminado el curso base en Hugging Face. Ahora conocerás las aplicaciones más llamativas en la **Fase 2 del curso** (Módulos 7, 8 y 9).
