#/bin/python3
import time
import traceback
import logging, sys

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


logging.getLogger("uvicorn.error").propagate = False
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

log = logging.getLogger(__name__)

app = FastAPI()


class SampleBody(BaseModel):
    some_data: str
    calc_in: Optional[str] = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/endpoint", response_model=SampleBody)
def endpoint(body: SampleBody):
    """
    A sample post endpoint
    """
    some_data = body.some_data
    tic = time.perf_counter()
    try:
        # Do something here
        pass
    except Exception as e:
        log.info('An exception occurred: {}'.format(e))
        log.error(traceback.format_exc())

    toc = time.perf_counter()

    log.info(f"Endpoint ran in {toc - tic:0.4f} seconds")
    body.calc_in = toc - tic
    
    json_body = jsonable_encoder(body)
    return JSONResponse(content=json_body)
