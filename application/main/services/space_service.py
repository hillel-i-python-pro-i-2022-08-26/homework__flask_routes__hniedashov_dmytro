from dataclasses import dataclass
import aiohttp
import asyncio


@dataclass
class SpaceService:
    api_url: str = "http://api.open-notify.org/"
    current_location_route: str = "iss-now.json"
    astros_route: str = "astros.json"

    async def request(self, route: str) -> str:
        async with aiohttp.ClientSession(self.api_url) as session:
            async with session.get(f"/{route}") as response:
                return await response.json()

    def run(self, route: str) -> str:
        return asyncio.run(self.request(route))

    def get_astros(self) -> str:
        return self.run(self.astros_route)

    def get_current_location(self) -> str:
        return self.run(self.current_location_route)
