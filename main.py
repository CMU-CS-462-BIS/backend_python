from typing import Union
from module import get_cfg
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/cfg")
def get_cfg_from_code(file_name: str, code_str: str) -> Union[dict, str]:
    try:
        cfg = get_cfg(file_name, code_str)
        return cfg
    except Exception as e:
        return str(e)
    
