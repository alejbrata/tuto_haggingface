from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import glob
import subprocess

app = FastAPI(title="Hugging Face Course API")

# Habilitar CORS para que el frontend (React en el puerto 5173) pueda pedir datos
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/modules")
def get_modules():
    """Devuelve la lista de carpetas de módulos disponibles."""
    carpetas = glob.glob("modulo_*")
    
    modulos_limpios = []
    for c in carpetas:
        # Limpiar el nombre (ej: "modulo_1_introduccion" -> "1 - Introduccion")
        partes = c.split("_")
        try:
            numero = int(partes[1])
            nombre = " ".join(partes[2:]).title()
            modulos_limpios.append({"id": c, "numero": numero, "nombre": nombre})
        except ValueError:
            pass
            
    # Ordenar estrictamente por el valor numérico
    modulos_limpios.sort(key=lambda x: x["numero"])
        
    return {"modules": modulos_limpios}

@app.get("/api/modules/{module_id}/theory")
def get_theory(module_id: str):
    """Devuelve el texto en Markdown de la teoría del módulo."""
    archivos_md = sorted(glob.glob(f"{module_id}/*.md"))
    if not archivos_md:
        return {"content": "# Este módulo no tiene archivo Markdown teórico."}
    
    with open(archivos_md[0], "r", encoding="utf-8") as f:
        return {"content": f.read(), "filename": archivos_md[0]}

@app.get("/api/modules/{module_id}/script")
def get_script_name(module_id: str):
    """Devuelve el nombre del script de python asociado y su código fuente."""
    archivos_py = sorted(glob.glob(f"{module_id}/*.py"))
    if not archivos_py:
        return {"filename": None, "source_code": None}
    
    with open(archivos_py[0], "r", encoding="utf-8") as f:
        codigo = f.read().replace("\r\n", "\n")
        
    return {"filename": archivos_py[0], "source_code": codigo}

@app.post("/api/modules/{module_id}/execute")
def execute_script(module_id: str):
    """Ejecuta el script de python de forma aislada y devuelve lo que imprimió en consola."""
    
    # Evitar inyecciones de comandos básicas
    if ".." in module_id or not module_id.startswith("modulo_"):
        return {"output": "Acceso denegado a esta carpeta."}
        
    archivos_py = sorted(glob.glob(f"{module_id}/*.py"))
    if not archivos_py:
        return {"output": "> No se encontró código ejecutable en este módulo."}
    
    script = archivos_py[0]
    
    try:
        # Ejecutamos con timeout razonable para modelos pequeños (3 minutos max)
        resultado = subprocess.run(["python", script], capture_output=True, text=True, timeout=180)
        output = resultado.stdout
        
        if resultado.stderr:
            output += "\n\n[WARNINGS O ERRORES DEL SISTEMA]:\n" + resultado.stderr
            
        return {"output": output.strip()}
    except subprocess.TimeoutExpired:
        return {"output": "> [TIMEOUT]: El script tardó más de 3 minutos. Es normal si el modelo pesa varias gigas y descargarlo tarda mucho por tu internet."}
    except Exception as e:
        return {"output": f"> [ERROR CRÍTICO]: {str(e)}"}
