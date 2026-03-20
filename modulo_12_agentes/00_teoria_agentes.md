# 12.0 Agentes con `smolagents`

Un **Agente** es el siguiente nivel en la evolución de la Inteligencia Artificial.
Hasta ahora los LLMs actuaban como un "cerebro en una caja". Podías hablar con él, pedirle que razonara o resumiera un texto, pero **no podía influir en el mundo exterior ni tomar acciones**.

Un Agente es dotar a ese cerebro de "brazos y piernas" mediante **Herramientas (Tools)**.

## ¿Cómo funciona un Agente?
1. El usuario pide una tarea compleja ("Investiga el clima actual en Tokio y envíalo a mi base de datos").
2. El Agente usa su LLM interno para hacer un **razonamiento (Thought)**: *"Primero necesito buscar el clima en Tokio, voy a usar la herramienta Search. Después, necesito guardarlo, voy a usar la herramienta Database"*.
3. El Agente ejecuta la herramienta número 1, recoge el resultado, vuelve a razonar, ejecuta la número 2, y te devuelve el éxito. Es cíclico y supervisado.

## La revolución: `smolagents` de Hugging Face
Crear agentes era muy difícil hasta que Hugging Face lanzó su propia librería de agentes minimalistas este año: **`smolagents`**.
La idea principal de esta librería es que **los agentes escriben temporalmente el código Python** necesario para resolver el problema, lo comprueban, y ejecutan las acciones en tu ordenador de forma aislada.

Puedes proporcionarle herramientas de código ya hechas por Hugging Face en el Hub (como la herramienta de búsqueda en Wikipedia web o el generador de imágenes) y el Agente decidirá cuándo y cómo debe invocarlas para resolver la petición que el humano le ha dado.

---
En nuestro script de Python conectaremos el agente `CodeAgent` con herramientas gratuitas y veremos cómo "razona" en voz alta antes de darte el resultado.
