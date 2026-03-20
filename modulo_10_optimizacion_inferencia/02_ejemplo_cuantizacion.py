from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
import warnings

warnings.filterwarnings('ignore')

print("--- Optimizando la Carga del Modelo ---")
model_id = "datificate/gpt2-small-spanish" 

# OPCIÓN 1: Half-Precision (FP16) - Reduce la memoria a la MITAD
print("\nOpción 1: Cargando el modelo en Float16 (Mitad de RAM/VRAM)...")
# Al poner torch_dtype=torch.float16, el modelo ocupa literalmente la mitad de memoria al cargarse.
modelo_fp16 = AutoModelForCausalLM.from_pretrained(
    model_id, 
    torch_dtype=torch.float16
)

print(f"Éxito. Este modelo ahora ocupa casi la mitad de memoria.")

# ---------------------------------------------------------------------------------
# OPCIÓN 2: Cuantización de 8-bits usando BitsAndBytes
# NOTA: Este bloque está comentado porque requiere instalar 'bitsandbytes'
# > pip install bitsandbytes
# Y generalmente necesita estar corriendo en Linux o usando WSL en Windows con GPU.
# ---------------------------------------------------------------------------------
"""
from transformers import BitsAndBytesConfig

print("\nOpción 2: Cargando en 8 bits (Reduce la memoria a una CUARTA parte)...")

quant_config = BitsAndBytesConfig(load_in_8bit=True)

modelo_8bit = AutoModelForCausalLM.from_pretrained(
    model_id, 
    quantization_config=quant_config,
    device_map="auto" # Esto automáticamente parte el modelo en tu CPU y tu GPU
)
print("¡El modelo se ha comprimido mágicamente en tiempo real de 32 bits a 8 bits!")
"""

print("\nCon estas técnicas (especialmente la cuantización), es como lograr meter el motor de un tractor dentro de un coche normal.")
