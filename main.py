import io
import logging

import uvicorn
from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from PIL import Image

from model import ImageCaptioningModel

logging.basicConfig(level=logging.INFO)

app = FastAPI()

logging.info("Loading model...")
model = ImageCaptioningModel()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(name="index.html", context={"request": request})


@app.post("/upload", response_class=HTMLResponse)
async def upload_image(
    request: Request,
    image: UploadFile = File(...),
    concept_sentence: bool = Form(False),
):
    try:
        contents = await image.read()
        image_pil = Image.open(io.BytesIO(contents)).convert("RGB")
        logging.info(f"Image uploaded: {image.filename}")
    except Exception as e:
        logging.error(f"Error processing image upload: {e}")
        return templates.TemplateResponse(
            name="upload.html",
            context={"request": request, "error": "Invalid image uploaded."},
        )

    try:
        logging.info(f"Generating caption...")
        caption = model.generate_caption(image_pil, concept_sentence)
    except Exception as e:
        logging.error(f"Error generating caption: {e}")
        return templates.TemplateResponse(
            name="upload.html",
            context={"request": request, "error": "Error generating caption."},
        )

    return templates.TemplateResponse(
        name="upload.html", context={"request": request, "caption": caption}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
