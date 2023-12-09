import uuid
import uvicorn

from fastapi import FastAPI, HTTPException
from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware

from app.routes import transcript_router
from app.monitoring import logging_config
from app.middlewares.correlation_id_middleware import CorrelationIdMiddleware
from app.middlewares.logging_middleware import LoggingMiddleware
from app.handlers.exception_handler import exception_handler
from app.handlers.http_exception_handler import http_exception_handler

###############################################################################
#   Application object                                                        #
###############################################################################

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

###############################################################################
#   Logging configuration                                                     #
###############################################################################

logging_config.configure_logging(level='DEBUG', service='cloud_hackathon', instance=str(uuid.uuid4()))

###############################################################################
#   Error handlers configuration                                              #
###############################################################################

app.add_exception_handler(Exception, exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)

###############################################################################
#   Middlewares configuration                                                 #
###############################################################################

# Tip : middleware order : CorrelationIdMiddleware > LoggingMiddleware -> reverse order
app.add_middleware(LoggingMiddleware)
app.add_middleware(CorrelationIdMiddleware)


###############################################################################
#   Routers configuration                                                     #
###############################################################################
@app.get("/")
async def root():
    print("---> root called")
    return {"message": "Hello From Cloud Hackathon Api"}


@app.get("/health")
async def health():
    print("---> Health Check")
    return {"message": "Api Running"}


app.include_router(transcript_router.router, prefix='/transcript', tags=['transcript'])

###############################################################################
#   Handler for AWS Lambda                                                    #
###############################################################################

handler = Mangum(app)

###############################################################################
#   Run the self contained application                                        #
###############################################################################

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
