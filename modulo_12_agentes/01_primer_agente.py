from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool
import warnings
warnings.filterwarnings('ignore')

print("--- Tu primer Agente Autónomo (smolagents) ---\n")
print("El agente intentará usar una herramienta de búsqueda de DuckDuckGo en internet para responderte.")

# 1. Definimos qué cerebro va a usar el Agente. 
# En smolagents, Hugging Face te regala el uso de modelos por API (por la nube) sin necesidad de descargar nada.
# Usaremos 'Qwen2.5-Coder', un modelo espectacular enfocado en programar y razonar, alojado gratuitamente por HF.
cerebro_llm = HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")

# 2. Le damos "brazos y piernas" (Herramientas)
# DuckDuckGoSearchTool busca en internet resultados reales y actualizados, cosa que un modelo congelado no puede hacer.
herramientas = [DuckDuckGoSearchTool()]

# 3. Construimos el Agente
agente = CodeAgent(
    tools=herramientas, 
    model=cerebro_llm,
    add_base_tools=True # Le da herramientas extra como un intérprete de Python básico
)

# 4. ¡A trabajar!
print("\nEl agente va a recibir una instrucción compleja. Mira cómo escribe su razonamiento ('Thought') paso a paso en tu terminal.")
instruccion = "¿Quién ganó el mundial de fútbol masculino en 2022 y con qué resultado quedó la final?"

print(f"\n=> Instrucción: {instruccion}\n")

try:
    # Run lanza el ciclo iterativo autónomo
    agente.run(instruccion)
except Exception as e:
    print("\n[Nota]: Si hubo un error o pide una API Key de Hugging Face de autenticación (HF_TOKEN),")
    print("significa que has superado el límite gratuito público o necesitas crear una cuenta gratuita en HF para obtener tu Token.")
