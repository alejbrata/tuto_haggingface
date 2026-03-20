from transformers import pipeline
import urllib.request
import os
import warnings
warnings.filterwarnings('ignore')

print("--- Sistema de Visión Artificial Automática ---\n")

print("1. Cargando el Analizador Visual (BLIP de Salesforce)...")
# Usamos un 'pipeline' especializado en "image-to-text"
descriptor_imagenes = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

# 2. Descargamos una foto de demo desde una URL y la guardamos
print("2. Descargando una fotografía de ejemplo de internet...")
url_foto = "https://images.unsplash.com/photo-1543466835-00a7907e9de1?q=80&w=640&auto=format&fit=crop"
archivo_temporal = "perrito_demo.jpg"

try:
    urllib.request.urlretrieve(url_foto, archivo_temporal)
    
    # 3. La magia pura: Le pasamos el nombre de la foto al modelo
    print("3. Analizando píxeles... ¿Qué hay en esta foto?")
    resultado = descriptor_imagenes(archivo_temporal)
    
    # Este modelo devuelve descripciones en inglés. 
    # (¡Podrías conectarlo después con tu modelo de traducción para pasarlo a español!)
    descripcion = resultado[0]['generated_text']
    
    print("-" * 50)
    print("El modelo observa: ")
    print(f"'{descripcion}'")
    print("-" * 50)
    
    # Limpiamos
    if os.path.exists(archivo_temporal):
        os.remove(archivo_temporal)
        
except Exception as e:
    print(f"Hubo un problema descargando o analizando la imagen: {e}")
