import httpx

API_URL = "https://api.thecatapi.com/v1"
API_KEY = "live_JBT0Ah0Nt12iyl2IpjQVLDWjcLk0GQwf4zI9wBMfmfejKmcC31mOJp4yJz5TsOUP"
HEADERS = {"x-api-key": API_KEY}

async def get_all_breeds():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{API_URL}/breeds", headers=HEADERS)
        return r.json()

async def get_breed_by_id(breed_id: str):
    breeds = await get_all_breeds()
    for breed in breeds:
        if breed["id"] == breed_id:
            return breed
    return None

async def search_breeds(query: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{API_URL}/breeds/search?q={query}", headers=HEADERS)
        return r.json()
