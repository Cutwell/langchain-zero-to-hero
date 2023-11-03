from fastapi import FastAPI
from langserve import add_routes
from my_app.chain import chain as my_app_chain

app = FastAPI()

add_routes(app, my_app_chain, path="/my-app")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
