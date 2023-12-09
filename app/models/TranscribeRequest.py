from pydantic import BaseModel


class TranscribeRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str
    expression: str
