from fastapi import FastAPI

app = FastAPI()

VERSION = "v2"

@app.get("/")
def root():
    return {"message": "ArgoCD demo funcionando!", "version": VERSION}

@app.get("/health")
def health():
    return {"status": "ok", "version": VERSION}
