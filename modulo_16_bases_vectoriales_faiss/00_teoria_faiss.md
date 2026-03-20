# 16.0 FAISS y el Mundo de los Embeddings

Cuando programamos sistemas RAG (como vimos en el Módulo 11), introdujimos dos conceptos técnicos que merecen su propio módulo: **Los Embeddings y FAISS**.

## 1. El problema del texto
A nosotros nos parece obvio que "El sol brilla fuerte" y "Hay mucha luz solar hoy" significan casi lo mismo, pero para un ordenador ordinario, las letras no coinciden en absoluto (`sol` != `luz`).

Para solucionar esto matemáticamente, Hugging Face ofrece modelos de Inserción (**Embeddings**). 
Su único trabajo no es "hablar", sino coger tu frase y convertirla en una lista de **1024 números decimales** (un vector espacial).
Si dos frases significan lo mismo, sus números en esa lista serán casi iguales o apuntarán a la misma dirección física en un plano tridimensional geométrico imaginario.

## 2. Bases de Datos Vectoriales
Si tienes un millón de documentos de tu empresa, usas el modelo de Hugging Face y generas un millón de listas de números. 
Pero, cuando el usuario hace la pregunta "*¿Dónde están mis facturas?*", tendrías que restar los números de la pregunta del usuario contra el de un millón de frases para ver cuál se parece más. Eso consumiría todo el procesador.

Aquí entran en juego las famosísimas **Vector Databases** (Bases de datos Vectoriales). 

## 3. ¿Qué es FAISS?
**FAISS** (Facebook AI Similarity Search) no es una base de datos tradicional entera (no es una empresa de software como MongoDB o SQL). Es una **librería algorítmica** creada por investigadores de Meta (Facebook).

- Está escrita en C++ para ser hiper-rápida.
- En lugar de revisar el millón de frases una por una, usa algoritmos de agrupación y métodos estadísticos para **descartar el 99% de las opciones en nanosegundos**, y buscar solo en el bloque parecido.
- Todo ocurre cargado en la memoria RAM (a diferencia de otras bases que escriben al HDD).

Por eso FAISS es el rey local e inmediato en entornos Python de prueba. Si tuvieras datos que requieran perdurar en la red como servicio en la nube, la gente migra de FAISS hacia bases corporativas como *Qdrant*, *Chroma* o *Milvus*.

---
Abre el ejemplo práctico (`01_busqueda_semantica.py`) para ver numéricamente cómo se comparan "Frases" usando Embeddings de Hugging Face y matemáticas FAISS puras, sin LLMs.
