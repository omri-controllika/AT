from fastapi import APIRouter

router = APIRouter()

@router.post("/compile")
async def compile_algo():
    return {"status": "queued"}
