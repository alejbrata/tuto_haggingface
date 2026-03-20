from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import warnings

warnings.filterwarnings('ignore')

print("--- Entendiendo Vector Databases (FAISS) ---\n")

print("1. Cargando el motor matemático (Embeddings)...")
# Este modelo de HF es buenísimo haciendo que las frases en español (multilingual) 
# se vuelvan números listos para buscarse semánticamente (por contexto).
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# Frases del inventario de un hospital, por ejemplo.
documentos_hospital = [
    "La sala de Urgencias está ubicada en la planta baja, acceso trasero.",
    "El horario de visitas es de 16:00 a 19:00 horas todos los días.",
    "Contamos con 4 respiradores artificiales y 2 desfibriladores.",
    "El dr. Ramírez es el cardiólogo a cargo de la sección de cirugía.",
    "En la cafetería venden menú del día a 9 euros."
]

print("2. FAISS: Indexando documentos en la memoria de LangChain...")
db_faiss = FAISS.from_texts(documentos_hospital, embedding=embeddings)

print("\nHagamos algunas búsquedas (Semánticas, no de texto exacto):\n")

# CASO 1: Contexto médico
pregunta_1 = "¿Quién es el médico especializado en el corazón?"
# En la pregunta NO aparece la palabra "Ramírez", "Cardiólogo", ni "cirugía", 
# FAISS lo encontrará solo por 'coincidencia matemática'
cercanos_1 = db_faiss.similarity_search(pregunta_1, k=1)
print(f"P: {pregunta_1}")
print(f"Razón matemática encontró: '{cercanos_1[0].page_content}'\n")

# CASO 2: Ubicaciones sin mencionarlas exacto
pregunta_2 = "¿Dónde puedo entrar corriendo si tengo un accidente?"
cercanos_2 = db_faiss.similarity_search(pregunta_2, k=1)
print(f"P: {pregunta_2}")
print(f"Razón matemática encontró: '{cercanos_2[0].page_content}'\n")

print("-" * 50)
print("¡Impresionante! Entendió el contexto sin encontrar palabras clave concretas.")
print("Esto es exactamente el paso previo clave para que un LLM (ChatGPT) te responda.")
