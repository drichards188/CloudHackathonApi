from fastapi import APIRouter, HTTPException
import logging.config

from starlette import status

from app.handlers.transcript_handler import TranscriptHandler

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/", tags=["Transcript"])
async def get_transcript_result(data: dict):
    if "symbol" not in data or "expression" not in data:
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail='please send valid TranscribeRequest in body')
    try:
        symbol = data["symbol"]
        expression = data["expression"]
        print(f'--> trying to get transcript results for {symbol} of {expression}')
        data["symbol"] = symbol.upper()
        evaluation = TranscriptHandler.handle_get_transcript_results(data, True)
        return evaluation
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
