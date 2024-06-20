from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# import uvicorn

app = FastAPI()


def sum_two_args(x, y):
    return x + y


# Hello World route
@app.get("/")
def read_root():
    return {"Hello": "World"}
app.mount("/static", StaticFiles(directory="static"), name="static")
templates=Jinja2Templates(directory="templates")
@app.get("/some_url/{something}", response_class=HTMLResponse)
async def read_something(request: Request, something: str):
 return templates.TemplateResponse("some.html", {"request": request,
"something": something})

# if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)
# запуск из консоли: uvicorn --host 127.0.0.1 --port 8000 fastlab:app
