import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.base_exception_handler import BaseExceptionHandler



class WebServer():

    # fast api endpoint specification /docs
    # fast api alternative endpoint specification /redoc
    fast_api_obj = FastAPI()


    @classmethod
    def start_web_server(cls):
        try:
            cls.fast_api_obj.add_middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

            uvicorn.run(cls.fast_api_obj, host="0.0.0.0", port=8000)
        except Exception as ex:
            raise BaseExceptionHandler(description=str(ex))
