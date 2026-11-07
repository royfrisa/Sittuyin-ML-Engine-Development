from fastapi import FastAPI

app = FastAPI(
    title="Sittuyin ML Engine API",
    description="Backend API for learning and playing Sittuyin.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}
