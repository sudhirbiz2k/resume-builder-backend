from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_resume():
    return {"message": "Resume route is working"}
