from datasets import load_dataset

print("Librería 'datasets' de Hugging Face: ¡Tu fuente inmensa de datos!\n")

print("Descargando un dataset de ejemplo...")
# Vamos a descargar un dataset muy famoso llamado 'glue', específicamente la tarea 'sst2' (análisis de sentimiento)
# Como ocupa mucho, solo descargaremos una división pequeña (split="train[:1%]" -> el primer 1%)
dataset = load_dataset("glue", "sst2", split="train[:1%]")

print("\n--- ¡Dataset Descargado! ---")
print(f"El dataset que acabamos de descargar tiene {len(dataset)} filas/ejemplos.")

print("\n¿Cómo se ve el primer ejemplo?")
print(dataset[0])
# Salida esperada: {'sentence': '...', 'label': 1, 'idx': 0}

print("\nPodemos iterar o filtrar estos datos muy fácilmente.")
print("Veamos las 3 primeras frases (sentences):")

for i in range(3):
    frase = dataset[i]['sentence']
    etiqueta = dataset[i]['label']
    print(f"{i+1}. [Etiqueta {etiqueta}] {frase}")

print("\n¿Por qué es importante esto?")
print("Porque para entrenar o ajustar (Fine-Tune) un modelo propio, necesitarás colecciones de miles de textos.")
print("La librería `datasets` te permite cargar archivos CSV locales o descargar datasets gigantescos de la web ")
print("optimizando enormemente la memoria RAM de tu ordenador.")
