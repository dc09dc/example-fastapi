from typing import Union

from fastapi import FastAPI, File, UploadFile
from rembg import remove

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/remove_background")
async def remove_background(file: UploadFile = File(...)):
    # Read image content
    contents = await file.read()
    # Remove background
    output = remove(contents)
    return output
