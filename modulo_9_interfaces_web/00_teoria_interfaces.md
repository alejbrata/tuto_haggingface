# 9.0 Creando Interfaces Visuales con Gradio

Es genial tener scripts de Python avanzados que funcionen en nuestra consola térmica de comandos, pero si seamos honestos: tu jefe, tus amigos de clase, o el equipo de Marketing de tu empresa no van a descargar Visual Studio Code para probar tu IA. 

¡Necesitan botones que puedan clickar!

## Saluda a Hub e Interfaces Rápidas
Por lo general, crear una página web involucra escribir código en HTML, CSS y configurar servidores pesados con React o Django. 

Para ahorrar ese tiempo brutal, el ecosistema de IA de Hugging Face adquirió y mejoró una librería oficial llamada **`Gradio`**.

## Gradio: Crea una Web App en Segundos
Gradio está específicamente diseñado para Modelos de Machine Learning.
Tú proporcionas:
1. Tu **función** predictiva (con los inputs para recibir texto y los outputs para sacar la respuesta de modelo).
2. Qué tipo de control gráfico quieres (`gr.Textbox()`, `gr.Image()`, `gr.Audio()`).

Y mágicamente Gradio arranca un servidor instantáneo en `http://localhost:7660` y genera una Interfaz de Usuario bonita con un clic de ejecución.

### Hugging Face "Spaces" (Demos Gratis)
Además de usarlo localmente, la web de Hugging Face tiene una sección llamada **Spacces**.
Cualquier código de de Python de `Gradio` que subas allí como repositorio será hospedado de forma gratuita (en servidores de CPU estándar) como aplicación pública 24/7. Es tu portfolio de programador IA definitivo online.

---
En nuestro último script (y más espectacular), `01_mi_primera_demo.py`, envolveremos una red de análisis de opiniones en un botón web.
