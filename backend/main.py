from fastapi import FastAPI

app = FastAPI(title="ISTQB Study Game API")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"status": "ok", "message": "ISTQB Study Game API is running"}