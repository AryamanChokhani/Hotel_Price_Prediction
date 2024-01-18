import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message':'hello stranger'}

@app.get('/Welcome')
def get_name(name:str):
    return {'Welcome to deployment process ':f'{name}'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.5000', port=8000)