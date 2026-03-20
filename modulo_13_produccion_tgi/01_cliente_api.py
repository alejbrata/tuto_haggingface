import requests
import warnings
warnings.filterwarnings('ignore')

print("--- Consumiendo un Modelo Expuesto como API (Producción) ---\n")

# Cuando usas Inference Endpoints o TGI en Docker, recibes una URL
# Aquí utilizaremos la API gratuita y pública general de Hugging Face a modo de ejemplo.
# Usaremos un modelo de relleno de palabras faltantes (fill-mask) muy rápido como BERT.
URL_API = "https://api-inference.huggingface.co/models/dccuchile/bert-base-spanish-wwm-uncased"
MI_HF_TOKEN = "hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Aquí pondrías el token privado de tu cuenta en producción

headers = {
    "Authorization": f"Bearer {MI_HF_TOKEN}",
    "Content-Type": "application/json"
}

# La frase tiene "[MASK]", que es la palabra que queremos que el modelo adivine y complete.
texto_de_entrada = {
    "inputs": "Madrid es la [MASK] de España."
}

print(f"Haciendo petición GET remota a -> {URL_API}")
print(f"Texto enviado: '{texto_de_entrada['inputs']}'")

# Las peticiones reales se hacen así, por HTTP, no cargando el modelo en la RAM del backend.
try:
    respuesta = requests.post(URL_API, headers=headers, json=texto_de_entrada)
    datos_completos = respuesta.json()
    
    # Manejar un posible error de autenticación porque mi token aquí es falso
    if "error" in datos_completos:
        print("\n¡Atención! Recibimos error del servidor (Normal porque necesitamos un Token real):")
        print(datos_completos)
        print("Si quisieras que esto funcionase, ve a Hugging Face -> Settings -> Access Tokens, y ponlo en `MI_HF_TOKEN`")
    else:
        # Si la llamada fue éxito
        palabra_adivinada = datos_completos[0]["token_str"]
        print("\nEl Servidor Web LLM respondió con éxito.")
        print(f"Se completó la frase como: 'Madrid es la {palabra_adivinada} de España.'")

except Exception as error:
    print("Error de conexión:", error)
