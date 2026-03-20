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

### Para el futuro...
Cuando quieras subir al nivel "Maestro" y hacer tu propio Fine-Tuning sin gastar miles de euros en súper-ordenadores, busca sobre el término **PEFT y LoRA** dentro del ecosistema de Hugging Face. Es la técnica moderna para hacer esto con tu tarjeta de vídeo en casa.

---
**¡Felicidades!** Has terminado el curso en Hugging Face. Ahora tienes los conocimientos para:
1. Usar Modelos directos con `pipeline`
2. Encontrar modelos en el Hub
3. Usar Tokenizers
4. Trabajar con datasets
5. Entender los conceptos de Fine-Tuning
