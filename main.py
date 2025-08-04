from fastapi import FastAPI
from routers.router import router as agent_router

app = FastAPI(title="Modular AI Agent System")

app.include_router(agent_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Modular AI Agent System"}