import tempfile
import traceback
from fastapi import (FastAPI, File, 
                    UploadFile, Form)

from fastapi.responses import JSONResponse

from address_parser import parse

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "OK"}
  
@app.post("/")
async def address_from_text(text: str=Form(...)):
  resp = {"address": None}
  try:
    resp["address"] = parse.extract(text)
    if resp["address"] is None:
      return JSONResponse(status_code=404,
                          content=resp)

    return JSONResponse(status_code=200, 
                        content=resp)
  except Exception as e:
    # print(traceback.print_exc())
    return JSONResponse(status_code=500, 
                        content=resp)    

@app.post("/image")
async def address_from_image(image: UploadFile = File(...)):
    resp = {"address": None}
    try:
        im_bytes = await image.read()
        with tempfile.NamedTemporaryFile(suffix='.jpg') as tmp_shp:
            tmp_shp.write(im_bytes)

            resp["address"] = parse.extract_from_image(tmp_shp.name)

            if resp["address"] is None:
                return JSONResponse(status_code=404,
                                        content=resp)

            return JSONResponse(status_code=200, 
                                content=resp)

    except Exception as e:
        # print(traceback.print_exc())
        return JSONResponse(status_code=500, 
                                content=resp)
