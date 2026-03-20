from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from transformers import pipeline
import warnings

warnings.filterwarnings('ignore')

print("--- Montando un sistema RAG local ---")

# 1. Los "Documentos Secretos" de nuestra empresa
textos_empresa = [
    "Ticketia fue fundada en el año 2026 en Madrid, España.",
    "El producto principal de Ticketia es un CRM con Agentes de Inteligencia artificial.",
    "El CEO actual de la empresa es Alejandro y su política de devoluciones es de 14 días.",
    "Nuestros servidores operan al 100% con energía verde."
]

print("1. Descargando el 'Sentence-Transformer' (Convertidor de texto a matemáticas)...")
# Usamos un modelo incrustador pequeñito y rápido especializado en frases
modelo_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

print("2. Creando la base de datos vectorial (FAISS)...")
vectorstore = FAISS.from_texts(textos_empresa, embedding=modelo_embeddings)
recuperador = vectorstore.as_retriever(search_kwargs={"k": 2}) # Traer las 2 frases más relevantes

print("3. Cargando el Cerebro LLM...")
el_cerebro = pipeline("text-generation", model="datificate/gpt2-small-spanish", max_new_tokens=40)
llm_langchain = HuggingFacePipeline(pipeline=el_cerebro)

# 4. Hacemos la búsqueda según la pregunta del usuario
pregunta_usuario = "¿Quién es el CEO de Ticketia y qué producto venden?"
print(f"\nUsuario pregunta: '{pregunta_usuario}'")

documentos_encontrados = recuperador.invoke(pregunta_usuario)
contexto_extraido = "\n".join([doc.page_content for doc in documentos_encontrados])

print(f"\n--- Información recuperada de la Base de Datos ---\n{contexto_extraido}")

# 5. Pasamos todo al LLM (Generación Aumentada)
prompt_final = f"""Responde brevemente a la pregunta basándote SOLO en este Contexto:
Contexto: {contexto_extraido}
Pregunta: {pregunta_usuario}
Respuesta:"""

# Ejecutamos! (En un modelo como Llama3 la respuesta sería perfecta, en GPT-2 Small será algo menos coherente pero con los datos correctos)
respuesta_ia = llm_langchain.invoke(prompt_final)
print("\n--- Respuesta de la IA ---")
print(respuesta_ia)
