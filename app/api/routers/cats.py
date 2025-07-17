from fastapi import APIRouter, HTTPException, Query
from app.services import catService
from app.schemas.catSchema import CatBreed
from typing import List

router = APIRouter()

@router.get("/", response_model=List[CatBreed])
async def get_breeds():
    return await catService.get_all_breeds()

@router.get("/{breed_id}", response_model=CatBreed)
async def get_breed(breed_id: str):
    breed = await catService.get_breed_by_id(breed_id)
    if not breed:
        raise HTTPException(status_code=404, detail="Breed not found")
    return breed

@router.get("/search/")
async def search_breed(q: str = Query(..., min_length=1)):
    return await catService.search_breeds(q)
