from fastapi import FastAPI

# Instanciar la aplicacion. Esta variable "app" es el motor de todo tu backend.
app = FastAPI(
    title="Futbol API",
    description="Motor de estadisticas deportivas",
    version="1.0.0"
)

# Crear la primera ruta HTTP (Un GET simple)
@app.get("/")
def read_root():
    return{
        "mensaje": "¡Bienvenido a la API de fútbol!",
        "estado": "El servidor está corriendo perfectamente."
    }
    