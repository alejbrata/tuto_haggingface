# 11.0 RAG (Retrieval-Augmented Generation)

Bienvenido a la técnica más buscada por las empresas en 2024 y 2025.

**El problema:** Los modelos de Hugging Face son muy listos, pero su memoria se detiene el día que terminaron de entrenarlos. No saben qué está pasando en tu empresa hoy, ni han leído tus PDFs privados, ni conocen los precios actualizados de tu tienda.
Si les preguntas algo de esto, **van a alucinar (inventarse la respuesta).**

**La solución:** RAG.

## ¿Cómo funciona RAG de forma muy resumida?
En vez de pedirle al modelo de lenguaje (LLM) que responda "de memoria", conviertes tu aplicación en un proceso de 3 pasos:

1. **Indexación:** Coges todos los PDFs o datos de tu empresa y se los pasas a un modelo especial de Hugging Face de "Embeddings" (Ej: `sentence-transformers`). Este modelo convierte tus textos en listas gigantes de números (vectores) y los guarda en una Base de Datos Vectorial (Ej: *FAISS*, *Qdrant* o *ChromaDB*).
2. **Retrieval (Recuperación):** Cuando el usuario hace una pregunta, conviertes su pregunta a números y buscas en tu Base de Datos los 3 fragmentos de texto más similares matemáticamente.
3. **Generation (Generación):** Le envías al LLM un *prompt* que dice: *"Teniendo en cuenta estos 3 fragmentos de documentos que he encontrado en mi base de datos de la empresa, responde a la pregunta del usuario: [Pregunta]"*.

De esta forma, la IA **razona** la respuesta pero lee la información **de tus documentos de verdad**.

---
Para unir todo este caos de bases de datos y modelos, usamos librerías intermedias orquestadoras. La más famosa es **LangChain**, que tiene una integración directa llamada `langchain-huggingface`. 

En `01_ejemplo_rag_local.py` verás un ejemplo de cómo crear una mini Base de Datos Vectorial y usarla para que el modelo responda basándose en esa información inyectada.
