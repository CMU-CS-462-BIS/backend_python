from typing import Union
from module import get_cfg
from fastapi import FastAPI, File, UploadFile
import time
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/cfg")
async def upload_file(file: UploadFile = File(...)):
    file_contents = await file.read()
    filename = file.filename.split(".")[0] + "_" + time.strftime("%Y%m%d%H%M%S")
    cfg = get_cfg(filename, file_contents)
    return {"path": cfg}

@app.get("/cfg/{file_name}")
def get_cfg_file(file_name: str):
    return FileResponse("output/" + file_name + ".png", media_type="image/png")

