from fastapi import FastAPI
from query_router import router
import uvicorn

app = FastAPI(title="Threat Search")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)