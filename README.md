# Fútbol API Backend
API de estadísticas deportivas construida con FastAPI.
## Stack
- FastAPI + Uvicorn
- SQLAlchemy (PostgreSQL)
- Alembic (migraciones)
- Pydantic (validación)
## Estructura
app/
├── api/          # Rutas/endpoints
├── core/         # Configuración
├── db/           # Conexión a BD
├── models/       # Modelos SQLAlchemy
├── repositories/ # Acceso a datos
├── schemas/      # Esquemas Pydantic
├── services/     # Lógica de negocio
└── main.py
## Inicio rápido
```bash
python -m uvicorn app.main:app --reload