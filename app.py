from fastapi import FastAPI
from agents.coordinator import CoordinatorAgent

app = FastAPI()

coordinator = CoordinatorAgent()

@app.get("/")
async def root():
    return {"status": "running"}

@app.post("/diagnose")
async def diagnose(data: dict):
    result = await coordinator.run(data)
    return result
