from fastapi import FastAPI, Request
import uvicorn

from controllers import routes

app = FastAPI(title="Poker Bot do Kevin")

for router in routes:
    app.include_router(router)

@app.get("/", tags=["Root"], summary='Root endpoint')
def read_root(request: Request):
    return {"message": f'Go to {request.base_url}docs to see the API documentation.'}

if __name__ == "__main__":
    uvicorn.run(app='main:app', reload=True, port=8000)

