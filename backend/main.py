from fastapi import FastAPI
from models.request_models import DebugRequest
from chains.debugger_chain import run_debugger

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Code Debugger API is running"}

@app.post("/debug")
def debug_code(request: DebugRequest):
    return run_debugger(request.code, request.language)