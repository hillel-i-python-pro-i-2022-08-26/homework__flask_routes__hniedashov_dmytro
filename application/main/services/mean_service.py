import asyncio
import ssl
from os import path
import pandas as pd

import aiohttp
from application.constants import MEAN_FILE_LINK, MEAN_FILE_PATH, INCHES_TO_CM_INDEX, POUNDS_TO_KG_INDEX


class MeanService:
    def get_mean_metric_rounded(self):
        mean = self.get_mean_pretty()

        return {
            "height": round(mean["height"] * INCHES_TO_CM_INDEX, 2),
            "weight": round(mean["weight"] * POUNDS_TO_KG_INDEX, 2),
        }

    def get_mean_pretty(self) -> dict[str, float]:
        mean = self.get_mean()

        return {"height": mean[0], "weight": mean[1]}

    def get_mean(self) -> list:
        if not path.exists(MEAN_FILE_PATH):
            self.load_file()

        with open(MEAN_FILE_PATH) as file:
            data = pd.read_csv(file)
            return list(data.mean())[1:]

    def load_file(self) -> None:
        content = asyncio.run(self.request())

        with open(MEAN_FILE_PATH, "w") as file:
            file.write(content)

    @staticmethod
    async def request() -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(MEAN_FILE_LINK, ssl=ssl.SSLContext()) as response:
                return await response.text()
