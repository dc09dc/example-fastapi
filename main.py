from typing import Union

from fastapi import FastAPI, File, UploadFile
from rembg import remove
import requests
from io import BytesIO

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def download_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to download image from URL: {url}")
    return BytesIO(response.content)

@app.post("/remove_background")
async def remove_background(url: str):
    try:
        # Download the image from the URL
        image_content = download_image(url)
        # Remove background
        output = remove(image_content.read())
        return output
    except Exception as e:
        return {"error": str(e)}


 # at last, the bottom of the file/module
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5049)
