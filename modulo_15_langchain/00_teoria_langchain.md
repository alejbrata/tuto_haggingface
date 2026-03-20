# 15.0 LangChain: El pegamento de la Inteligencia Artificial

A lo largo del ecosistema Hugging Face hemos visto cómo invocar modelos que, por sí solos, actúan como un mero traductor o adivinador de textos ("entra texto A, sale texto B").

Pero los productos de software reales (como Notion AI o Microsoft Copilot) necesitan conectar esa IA con:
1. Bases de datos SQL.
2. Historiales de chat (Memoria).
3. Varios modelos de IA trabajando en equipo.

Para hacer todo esto fácil nació **LangChain**, un *framework* (marco de trabajo) extremadamente popular de Python y JavaScript.

## 1. El concepto de "Chain" (Cadena)
En LangChain, la abstracción principal es la **Cadena**. 
En lugar de escribir código espagueti para llamar a la IA, procesar la respuesta y pasársela a otra función, LangChain te permite construir "tuberías" usando un operador especial (`|`).

Por ejemplo, una cadena simple sería:
`Cadena = Plantilla_De_Prompt | Modelo_De_HuggingFace | Convertidor_A_Texto`

## 2. Prompts Dinámicos (Prompt Templates)
Mientras que en Python base tú harías formateo de strings (Ej: `f"Hola {nombre}, actua como un {rol}"`), LangChain trae plantillas (`PromptTemplates`). Estas plantillas son robustas, pueden ser importadas desde el Hub de LangChain, y saben en todo momento qué variables de entrada les faltan por rellenar antes de invocar a la IA.

## 3. Integración Directa con HF
LangChain no entrena modelos, LangChain **orquesta**. 
Gracias a su paquete hermano avanzado `langchain-huggingface`, puedes decirle a la cadena que use una pipeline de Hugging Face como "cerebro lógico".

---
En el archivo `01_ejemplo_cadenas.py` verás lo sencillo que es crear una cadena en la sintaxis moderna de LangChain (conocida como *LCEL - LangChain Expression Language*) sin apenas esfuerzo estructural.
