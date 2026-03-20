from diffusers import StableDiffusionPipeline
import torch

print("¡Bienvenido al mundo de la Generación de Imágenes (Text-to-Image)!")
print("Cargando el pipeline de Stable Diffusion...")
print("(NOTA: Si estás en un PC sin tarjeta de video NVIDIA, esto puede usar mucha memoria RAM y tardar unos minutos en descargar)\n")

# Para generación de imágenes, Hugging Face tiene una librería hermana de 'transformers' llamada 'diffusers'
# El ID del modelo en el Hub correspondiente a una versión accesible de Stable Diffusion
model_id = "runwayml/stable-diffusion-v1-5"

# Si tienes GPU de Nvidia y torch configurado con CUDA, cambiarías "cpu" a "cuda" y pondrías `torch_dtype=torch.float16`
# Para hacerlo universal en CPU, usamos valores por defecto:
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)

# Descomenta esto SI TIENES TARJETA GRÁFICA NVIDIA instalada 
# pipe = pipe.to("cuda")

# 1. Definir tu prompt (El texto mágico)
prompt = "Un perro astronauta flotando en el espacio exterior, ilustración digital de altísima calidad"

print(f"Dibujando: '{prompt}'")
print("\nPor favor espera, generando... (En un ordenador portátil normal sin GPU puede tardar ~5 minutos)")

# 2. Generar y guardar imagen
imagen = pipe(prompt).images[0]
imagen.save("perro_espacial.png")

print("\n¡Imagen generada exitosamente! Abre tu explorador de archivos y busca 'perro_espacial.png' en esta carpeta.")
