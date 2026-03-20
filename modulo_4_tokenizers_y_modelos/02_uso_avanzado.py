import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import warnings
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"
warnings.filterwarnings('ignore')

modelo_hub_id = "nlptown/bert-base-multilingual-uncased-sentiment"
print(f"Cargando Tokenizer y Modelo manualmente desde: {modelo_hub_id}\n")

# 1. Cargar las piezas
tokenizer = AutoTokenizer.from_pretrained(modelo_hub_id)
modelo = AutoModelForSequenceClassification.from_pretrained(modelo_hub_id)

texto = "¿Qué es un Tokenizer? ¡Esta lección me parece muy interesante!"

# 2. El paso del TOKENIZER: convertir texto a números
print(f"Texto original: '{texto}'")
# return_tensors="pt" significa "devuélvelo en el formato matemático de PyTorch (P-T)"
inputs = tokenizer(texto, return_tensors="pt") 
print("\nSalida matemática (Tokens numéricos):")
print(inputs["input_ids"])

# 3. El paso del MODELO: inferir
# Usamos torch.no_grad() para decirle al modelo que solo queremos predecir, no entrenar (ahorra RAM/GPU)
with torch.no_grad():
    salida_modelo = modelo(**inputs)

# 4. Post-procesamiento
# El modelo nos devuelve algo llamado "logits" (puntuaciones matemáticas crudas para cada etiqueta)
logits = salida_modelo.logits
print("\nLogits crudos que escupe el modelo:", logits)

# Convertimos los logits a un número de clase (ej. clase 4, que corresponde a 5 estrellas)
clase_predicha_id = logits.argmax().item()

# Mapeamos el ID de la clase a la etiqueta en lenguaje humano (1 star, 2 stars...)
etiqueta = modelo.config.id2label[clase_predicha_id]
print(f"\n¡Resultado Final! -> {etiqueta}")
print("-" * 50)
print("¡Has hecho el mismo trabajo que un pipeline de forma manual!")
