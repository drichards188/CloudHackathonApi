from typing import Optional

from fastapi import APIRouter, HTTPException
from fastapi import Request, Header
import logging.config

from starlette import status

from app.handlers.transcript_handler import TranscriptHandler
from app.models.TranscribeRequest import TranscribeRequest

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/", tags=["Transcript"])
async def get_transcript_result(request: Request, data: dict,
                                is_test: Optional[bool] | None = Header(default=False)):
    if "symbol" not in data or "expression" not in data:
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail='please send valid TranscribeRequest in body')
    try:
        symbol = data["symbol"]
        # start_date = data.start_date
        # end_date = data.end_date
        expression = data["expression"]
        print(f'--> trying to get transcript results for {symbol} of {expression}')
        evaluation = TranscriptHandler.handle_get_transcript_results(data, True)
        return evaluation
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
