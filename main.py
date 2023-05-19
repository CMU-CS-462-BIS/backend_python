from module import get_cfg
from fastapi import FastAPI, File, UploadFile
import time
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

import pathlib

plt = platform.system()
# if linux
if plt == "Linux":
    pathlib.WindowsPath = pathlib.PosixPath

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


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


# TODO: Add a way to get the CFG from a string
# Parameters: code_str: str
@app.post("/cfg/str")
async def get_cfg_str(code_str: str = File(...)):
    filename = "cfg_" + time.strftime("%Y%m%d%H%M%S")
    cfg = get_cfg(filename, code_str)
    return {"path": cfg}
