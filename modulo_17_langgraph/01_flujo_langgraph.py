from typing import TypedDict
from langgraph.graph import StateGraph, START, END
import warnings

warnings.filterwarnings('ignore')

print("--- Flujos de Trabajo con LangGraph ---\n")

# 1. Definimos el 'State' (El paquete de datos que viaja por nuestro diagrama de flujo)
class EstadoAgentes(TypedDict):
    mensaje: str
    revisiones: int

# 2. Definimos los NODOS (Las funciones de Python que pueden contener llamas a LLMs de HuggingFace)
# NOTA: Para no sobrecargar tu memoria con múltiples LLMs locales en este test, 
# simularemos la respuesta de los LLMs con strings tradicionales.

def nodo_generador(estado: EstadoAgentes):
    print("🤖 Generador: Escribiendo texto...")
    if estado["revisiones"] == 0:
        texto = "Este modelo the Huging Fasce es super xhunix."
    else:
        texto = "Este modelo de Hugging Face es muy completo."
        
    return {"mensaje": texto}

def nodo_corrector(estado: EstadoAgentes):
    print("👓 Corrector: Revisando la ortografía...")
    texto_actual = estado["mensaje"]
    rev = estado["revisiones"] + 1
    
    if "xhunix" in texto_actual:
        return {"mensaje": "Hay errores graves de escritura.", "revisiones": rev}
    else:
        return {"mensaje": "Texto perfecto sin errores.", "revisiones": rev}

# 3. Función Condicional (Decide de qué Nodo a qué Nodo van las flechas)
def ruta_decision(estado: EstadoAgentes):
    if "errores graves" in estado["mensaje"]:
        print("🔀 Decisión: Hay errores. El flujo vuelve hacia atrás (Generador).")
        return "volver_al_generador"
    else:
        print("🔀 Decisión: Todo correcto. El flujo termina.")
        return "terminar_flujo"

# 4. Construimos el Grafo (Diagrama)
flujo_builder = StateGraph(EstadoAgentes)

# Añadimos los dos cajones
flujo_builder.add_node("Generador", nodo_generador)
flujo_builder.add_node("Corrector", nodo_corrector)

# Añadimos las flechas fijas
flujo_builder.add_edge(START, "Generador")
flujo_builder.add_edge("Generador", "Corrector")

# Añadimos la "Flecha Condicional" que permite crear bucles (volver atrás)
flujo_builder.add_conditional_edges(
    "Corrector", 
    ruta_decision,
    {
        "volver_al_generador": "Generador",
        "terminar_flujo": END
    }
)

# Compilamos la aplicación de inteligencia artificial
grafo_app = flujo_builder.compile()

# 5. Ejecutamos pasándole un estado inicial limpio en la línea de salida
print("=> Lanzando la ejecución del Grafo LangGraph:\n")
estado_inicial = {"mensaje": "", "revisiones": 0}
estado_final = grafo_app.invoke(estado_inicial)

print("\n--- Resultado Final del Sistema de Agentes ---")
print(estado_final)
