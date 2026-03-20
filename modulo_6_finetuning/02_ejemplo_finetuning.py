from transformers import AutoModelForSequenceClassification, AutoTokenizer, TrainingArguments, Trainer
from datasets import load_dataset
import warnings

warnings.filterwarnings('ignore')

print("--- Ejemplo Didáctico de Fine-Tuning Completo ---")
print("NOTA IMPORTANTE: Este script necesita una tarjeta gráfica (GPU) para ejecutarse en un tiempo razonable.")
print("Si lo corres en una CPU de escritorio, puede tardar horas.\n")

# 1. Cargar el modelo base pre-entrenado y su tokenizer
model_id = "nlptown/bert-base-multilingual-uncased-sentiment" # Modelo base
tokenizer = AutoTokenizer.from_pretrained(model_id)

# 2. Cargar tus propios datos (Aquí simulamos cargar un dataset pequeñito)
dataset = load_dataset("glue", "sst2", split="train[:50]")

# 3. Pre-procesar (Tokenizar) tus datos
def tokenizar_funcion(ejemplos):
    return tokenizer(ejemplos["sentence"], padding="max_length", truncation=True)

dataset_tokenizado = dataset.map(tokenizar_funcion, batched=True)

# 4. Descargar el modelo para empezar a entrenar
modelo = AutoModelForSequenceClassification.from_pretrained(model_id)

# 5. Configurar los hiperparámetros de entrenamiento
argumentos_entrenamiento = TrainingArguments(
    output_dir="./mi_modelo_finetuneado",
    evaluation_strategy="no",       # Para este ejemplo no evaluamos mientras entrena
    learning_rate=2e-5,             # Tasa de aprendizaje (qué tan rápido aprende)
    per_device_train_batch_size=8,  # Entrenarlas de 8 en 8 frases
    num_train_epochs=1,             # Épocas: Cuántas veces el modelo va a leer todos tus datos
    weight_decay=0.01,
)

# 6. Crear el objeto Trainer (El "Entrenador" automático)
trainer = Trainer(
    model=modelo,
    args=argumentos_entrenamiento,
    train_dataset=dataset_tokenizado,
)

print("¡La configuración está lista! Para empezar el entrenamiento descomenta la siguiente línea:")
# trainer.train()

print("Una vez finalice, el modelo 'inteligente' modificado se guardaría y podrías usarlo localmente.")
# trainer.save_model("./mi_modelo_finetuneado_final")
