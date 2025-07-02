from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get('/hello-world', response_class=JSONResponse)
async def hello_endpoint() -> dict[str, str]:
    return {'message': 'Hello, FastAI!'}
