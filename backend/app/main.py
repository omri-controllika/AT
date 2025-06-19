from fastapi import FastAPI
from .api.v1.routes import auth, strategies, quantconnect

app = FastAPI(title="Algo Trading API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(strategies.router, prefix="/strategies", tags=["strategies"])
app.include_router(quantconnect.router, prefix="/quantconnect", tags=["quantconnect"])

@app.get("/")
async def root():
    return {"message": "Backend running"}

