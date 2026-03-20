# 17.0 LangGraph: El motor de los Agentes Complejos

En el Módulo 15 vimos cómo **LangChain** utiliza "Cadenas" (Chains). 
El problema de una cadena es que **solo va en una dirección** (Entrada -> Modelo -> Salida).

Pero en el mundo real humano, si te equivocas haciendo algo, vuelves atrás y lo intentas de nuevo. Esta "reflexión iterativa" y estos "bucles" son imposibles de programar de forma limpia con una cadena recta.

Para resolver esto, los creadores de LangChain lanzaron **LangGraph**.

## ¿Qué es LangGraph?
Es una librería que nos permite definir nuestros programas de Inteligencia Artificial como un **Grafo de Estado Cíclico** (StateGraph).
Visualmente, imagina un diagrama de flujo con flechas que pueden apuntar hacia atrás.

Tiene tres componentes básicos:
1. **Estado (`State`):** Un objeto de memoria compartida (un diccionario de Python) que viaja por todos los nodos del sistema. Si el Nodo A escribe "El sol", el Nodo B puede leer "El sol".
2. **Nodos (`Nodes`):** Son las funciones o cajitas de tu diagrama. Normalmente, cada nodo es una llamada a un LLM distinto o una herramienta de búsqueda.
3. **Aristas (`Edges`):** Son las flechas que conectan los nodos. Aquí metes tu lógica de decisión condicional (Ej: *Si el texto está mal traducido, la flecha vuelve al modelo A; si está bien, la flecha avanza al nodo de Fin*).

## Hugging Face + LangGraph
A pesar de que el framework es externo, podemos seguir usando la librería de `transformers` (o `langchain-huggingface`) como los "Cerebros" internos dentro de cada uno de los Nodos del Grafo. Gracias a LangGraph, se ha democratizado la construcción de enjambres multi-agente.

---
En `01_flujo_langgraph.py` vamos a crear un diagrama de flujo simple de dos nodos (Un "Crítico" y un "Editor") que se pasan un mensaje de estado entre ellos.
