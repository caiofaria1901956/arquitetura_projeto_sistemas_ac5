import json


class Configuracao:
    """classe configuracao"""
    def __init__(self: object) -> None:
        """método construtor de Configuracao"""
        self.__salvar_json: bool


    @property
    def salvar_json(self: object) -> bool:
        """Função que retorna valor de salvar_json"""
        return self.__salvar_json

    @salvar_json.setter
    def salvar_json(self: object, novo_salvar_json: bool) -> None:
        """Função que altera salvar_json"""
        self.__salvar_json = novo_salvar_json
        return

    def carregar_configuracao(self: object) -> None:
        with open("conf//config.json", 'r') as file:
            load = json.load(file)
            self.salvar_json = load['salvar_json']
