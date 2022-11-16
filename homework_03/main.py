from fastapi import FastAPI


app = FastAPI()


@app.get("/ping")
def read_root():
    return {"message": " pong "}


@app.get("/{path:path}")
def all_other(path: str):
    return {"request to": path}

