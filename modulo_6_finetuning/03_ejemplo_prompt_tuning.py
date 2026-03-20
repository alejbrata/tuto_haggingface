from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import get_peft_model, PromptTuningConfig, TaskType, PromptTuningInit
import warnings

warnings.filterwarnings('ignore')

print("--- Ejemplo Didáctico de Prompt Tuning (Técnica PEFT) ---")
print("A diferencia del Fine-Tuning completo, aquí el modelo base NO se modifica matemáticamente.")
print("En vez de eso, añadimos una 'capa de tokens mágicos' súper liviana.\n")

model_id = "datificate/gpt2-small-spanish"

# 1. Cargar Tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)

# 2. Cargar el Modelo Base ORIGINAL
modelo_base = AutoModelForCausalLM.from_pretrained(model_id)
print(f"Parámetros totales del modelo base: {modelo_base.num_parameters():,}")

# 3. La Magia Funcional: Configurar PROMPT TUNING
configuracion_prompt_tuning = PromptTuningConfig(
    task_type=TaskType.CAUSAL_LM,
    prompt_tuning_init=PromptTuningInit.TEXT,
    # Estos son los tokens iniciales virtuales. El modelo va a mutar los números detrñas de estas palabras
    # para aprender cómo responder mejor a nuestra tarea.
    prompt_tuning_init_text="Imita el estilo literario formal español: ", 
    num_virtual_tokens=8,
    tokenizer_name_or_path=model_id,
)

# 4. Aplicar el wrapper de PEFT al modelo
modelo_peft = get_peft_model(modelo_base, configuracion_prompt_tuning)

# Vamos a ver cuántos parámetros va a entrenar realmente
peft_params = modelo_peft.get_nb_trainable_parameters()
print(f"Parámetros a entrenar con Prompt Tuning: {peft_params[0]:,} (apenas el {peft_params[2]:.4f}% del modelo gigante)")

# Con esto te ahorras todo el uso abusivo de tarjeta gráfica.

# 5. El resto es exactamente igual que el "Trainer" convencional
# trainer = Trainer(
#    model=modelo_peft,
#    train_dataset=tu_dataset_tokenizado,
#    args=TrainingArguments(...)
# )
# trainer.train()
# modelo_peft.save_pretrained("./mi_prompt_tuning_final")
