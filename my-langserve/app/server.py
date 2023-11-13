from fastapi import FastAPI
from langserve import add_routes
from pirate_assistant.chain import chain as pirate_assistant_chain

app = FastAPI()

add_routes(app, pirate_assistant_chain, path="/pirate")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
