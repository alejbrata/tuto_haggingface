from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from transformers import pipeline
import warnings

warnings.filterwarnings('ignore')

print("--- LangChain en Acción ---\n")

print("1. Cargando el cerebro de Hugging Face...")
# Un clásico: Texto a Texto. Modelo muy ligero.
cerebro_hf = pipeline("text-generation", model="datificate/gpt2-small-spanish", max_new_tokens=30)

# LangChain lo "envuelve" para poder usarlo en su ecosistema
llm = HuggingFacePipeline(pipeline=cerebro_hf)

print("2. Diseñando la plantilla del Prompt...")
# Las plantillas permiten estandarizar cómo le hablamos a la IA
# Imagina que tienes Frontend Web que te manda el "tema" que escribió el usuario.
plantilla = PromptTemplate.from_template(
    "Eres un poeta experto. Escribe un verso corto sobre el siguiente tema: {tema}\n\nVerso:"
)

# El output parser simplemente asegura que nos devuelvan 'string' puro sin formatos raros.
parseador = StrOutputParser()

print("3. Construyendo la 'Cadena' (Chain)...")
# Aquí usamos Langchain Expression Language (LCEL). El símbolo '|' es como una tubería.
# Los datos entran por la plantilla -> pasan por la IA -> salen limpios en string
cadena = plantilla | llm | parseador

print("\n=> Ejecutando la cadena de LangChain:")
# Una vez construida la máquina, solo necesitas darle a la manivela ('invoke') pasándole la variable
tema_elegido = "la luna"
print(f"Variable de entrada: {tema_elegido}")

# Aquí es donde LangChain hace todo el trabajo (rellena el prompt, llama a HF, limpia el output)
respuesta = cadena.invoke({"tema": tema_elegido})

print(f"\nResultado final de la cadena de LangChain:\n{respuesta.strip()}")
