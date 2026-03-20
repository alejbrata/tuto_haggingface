# 13.0 Producción Real: Text-Generation-Inference (TGI) y Endpoints

A lo largo del curso hemos programado scripts en Python que descargaban modelos gigantescos al disco duro y luego los ejecutaban. 
**Esto NUNCA se hace así en una empresa real.**

Si pones uno de estos scripts como el "backend" de tu app de Ticketia, y tres clientes intentan chatear al mismo tiempo, el código reventará por falta de memoria RAM.

## Text-Generation-Inference (TGI)
Hugging Face desarrolló **TGI**, una herramienta de infraestructura (escrita en lenguajes ultrarrápidos como Rust) diseñada para correr contenedores de Docker optimizados.
Un servidor corriendo TGI hace maravillas:
1. Pone en cola cientos de peticiones a la vez (*Continuous Batching*).
2. Optimiza la memoria de la tarjeta gráfica al máximo.
3. Te ofrece instantáneamente una "API" (como una URL web) a la que puedes enviar peticiones `curl` o JSON desde tu frontend en JavaScript, React o Flutter.

¡Incluso OpenAI probablemente use técnicas parecidas para hacer que ChatGPT de servicio a millones de usuarios!

## Hugging Face Inference Endpoints
Si no tienes el dinero para comprar tus propios servidores con tarjetas NVIDIA, Hugging Face te alquila los suyos. 
Dentro del Hub, tienes el apartado **"Inference Endpoints"**. Buscas cualquier modelo, le das un click, pagas por horas, e instantáneamente tendrás tu contenedor privado de TGI desplegado en la nube con una URL privada lista para usar.

---
En `01_cliente_api.py` te dejo la estructura básica recomendada de cómo debe conectarse tu programa (por ejemplo, el Backend de Django o Node.js) mediante la **Inference API**, sin necesidad de usar `transformers` en local.
