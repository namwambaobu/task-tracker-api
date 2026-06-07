from fastapi import FastAPI

app = FastAPI(
    title ="Task Tracker API",
    version="1.0.0"
)

@app.get("/")
def root() -> dict:
    return {
        "name" : "Task Tracker API",
        "version" : "1.0.0",
        "environment" : "development"
    }


@app.get("/health")
def health_check() -> dict:
    return {"status": "healthy"}
