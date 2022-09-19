from app.crud.joke import joke
from app.schemas.joke import CreateJoke, JokeHttp, UpdateJoke
from app.services.base_impl import BaseService, QueryType
from app.services.http.client import client


class JokeService(BaseService[CreateJoke, UpdateJoke]):
    def __init__(self, queries: QueryType):
        super().__init__(queries=queries)
        self.__client = client
        self.__factory_joke = {
            "Dad": self.__generate_dad,
            "Chuck": self.__generate_chuck,
        }

    async def generate_joke(self, *, type: str):
        kind = self.__factory_joke[type.name]
        return await kind()

    async def __generate_chuck(self):
        url = "https://api.chucknorris.io/jokes/random"
        response = await self.__client.get(
            url_service=url,
        )
        response = response.json()
        return JokeHttp(**response, source=url, joke=response["value"])

    async def __generate_dad(self):
        url = "https://icanhazdadjoke.com/"
        header = {"Accept": "application/json"}
        response = await self.__client.get(url_service=url, headers=header)
        response = response.json()
        return JokeHttp(**response, source=url)


joke_service = JokeService(queries=joke)
