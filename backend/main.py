from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from backend.localidades import llamarAPI

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

@app.get("/getjson")

def getJSON(localidad:int):
    #Conectarse a la API de Jardín Botánico
    if localidad== 8:
        #Buscar el bbox de Kennedy
        nombre= "Kennedy"
    elif localidad== 7:
        #Buscar el bbox de Bosa
        nombre= "Bosa"
    elif localidad== 19:
        #Buscar el bbox de Ciudad Bolivar
        nombre= "Ciudad Bolivar"

    return llamarAPI(localidad)

