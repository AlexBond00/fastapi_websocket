from fastapi import APIRouter, WebSocket, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app = APIRouter()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


@app.websocket("/api/v1/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    counter = 0
    while True:
        request_data = await websocket.receive_json()
        counter += 1
        response_data = {
            'id': counter,
            'message': request_data['message'],
        }
        await websocket.send_json(response_data)


@app.get('/')
def root(request: Request):
    context = {
        'request': request,
        'title': 'Use Websocket'
    }
    return templates.TemplateResponse('index.html', context=context)
