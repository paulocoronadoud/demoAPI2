from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

# Crear un objeto que represente mi aplicación

app = FastAPI()

# Configurar solicitudes cross-origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def saludar():
    saludo= {
        "mensaje": "Hola Mundo!!! API OK"
    }
    return saludo

@app.get("/despedir")
def despedirse():
    mensaje= {
        "mensaje": "Adiós mundo cruel!!! API OK"
    }
    return mensaje
