from fastapi import APIRouter


router = APIRouter(prefix='/explorer')

@router.get('/')
def top():
    return 'Top explorer endpoint'

@router.get('/items')
def top():
    return 'list of items'