from fastapi import FastAPI, BackgroundTasks
from model import query
import io
import os
from PIL import Image
from fastapi.responses import FileResponse

app = FastAPI()

def delete_image_file(file_path: str):
    os.remove(file_path)

@app.get('/generate image')
def generate_image(input: str, background_tasks: BackgroundTasks):
    result = query(input)
    image = Image.open(io.BytesIO(result))
    image = image.save('image.png')
    response = FileResponse('image.png')
    background_tasks.add_task(delete_image_file, 'image.png')
    return response
