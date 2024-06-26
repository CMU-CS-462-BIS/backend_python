import platform
from module import get_cfg
from notation_module import get_from_str, NOTATION_TYPES
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
    allow_methods=["*"],
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


# description: get cfg from code string
# params: code_str: string
# return: path: string
@app.post("/cfg/str")
async def get_cfg_str(code_str: str = File(...)):
    filename = "cfg_" + time.strftime("%Y%m%d%H%M%S")
    cfg = get_cfg(filename, code_str)
    notation = get_from_str(code_str)
    print(notation)
    return {"path": cfg, "notation": notation}


# ignore notation_area.py
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        reload_excludes=["notation_area.py"],
        log_level="info",
    )
