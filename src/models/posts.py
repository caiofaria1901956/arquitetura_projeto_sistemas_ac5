from src.models.users import User


class Posts:
    """Classe posts"""

    def __init__(
            self: object,
            user_id: int,
            id: int,
            title: str,
            body: str
    ) -> None:
        """Método construtor de Posts"""
        self.__user_id = user_id
        self.__id = id
        self.__title = title
        self.__body = body
        return

    @property
    def user_id(self: object) -> int:
        """property que retorna o valor de user_id"""
        return self.__user_id

    @property
    def id(self: object) -> int:
        """property que retorna o valor de id"""
        return self.__id

    @property
    def title(self: object) -> str:
        """property que retorna o valor de title"""
        return self.__title

    @property
    def body(self: object) -> str:
        """property que retorna o valor de body"""
        return self.__body

    def dict(self: object) -> dict:
        """Função que retorna dicionário com todos os valores"""
        return {
            "user_id": self.user_id,
            "id": self.id,
            "title": self.title,
            "body": self.body
        }
