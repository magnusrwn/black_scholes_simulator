from fastapi import Request, FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .calcs import plot_values



app = FastAPI()
templates = Jinja2Templates("templates/")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", { "request":request })



@app.post("/calc")
async def calc(
    optionType: str = Form(...),
    s: float = Form(...),
    k: float = Form(...),
    r: float = Form(...),
    sigma: float = Form(...),
    q: float = Form(...),
    t: float = Form(...),
):
    # Grab co-ordinates
    data = plot_values(direction=optionType, s=s, k=k, r=r, sigma=sigma, q=q, t=t)
    return data
