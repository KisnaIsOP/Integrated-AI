from fastapi import FastAPI
from core.nlp import NLPProcessor
from core.ml import MLProcessor
from api.routes import router
import uvicorn

app = FastAPI(
    title="Integrated AI Assistant",
    description="A versatile AI assistant with multiple capabilities",
    version="1.0.0"
)

# Initialize processors
nlp_processor = NLPProcessor()
ml_processor = MLProcessor()

# Include API routes
app.include_router(router, prefix="/api")

@app.get("/")
async def root():
    return {
        "message": "Welcome to Integrated AI Assistant",
        "status": "active",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
