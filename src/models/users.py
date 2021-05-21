class Geo:
    """Está classe receberá a latitude e longitude de algum usuário"""
    def __init__(self: object, lat: float, lng: float) -> None:
        """Metódo construtor da classe Geo"""
        self.__lat = lat
        self.__lng = lng
        return


    @property
    def lat(self: object) -> float:
        """property que retorna latitude"""
        return self.__lat

    @property
    def lng(self: object) -> float:
        """property que retorna longitude"""
        return self.__lng


    def dict(self: object) -> dict:
        """função que retorna dicionário com todos os dados"""
        return {
            "lng": self.lng,
            "lat": self.lat
        }


class Address:
    """Está classe receberá o endereço de um usuário"""
    def __init__(
            self: object,
            street: str,
            suite: str,
            city: str,
            zip_code: str,
            geo: Geo
    ) -> None:
        """Metódo construtor da classe Address"""
        self.__street = street
        self.__suite = suite
        self.__city = city
        self.__zip_code = zip_code
        self.__geo = geo
        return


    @property
    def street(self: object) -> str:
        """property que retorna o campo street"""
        return self.__street


    @property
    def suite(self: object) -> str:
        """property que retorna o campo suite"""
        return self.__suite

    @property
    def city(self: object) -> str:
        """property que retorna o campo city"""
        return self.__city

    @property
    def zip_code(self: object) -> str:
        """property que retorna o campo zip_code"""
        return self.__zip_code

    @property
    def geo(self: object) -> Geo:
        """property que retorna o campo Geo"""
        return self.__geo


    def dict(self: object) -> dict:
        """função que retorna dicionário com todos os dados"""
        return {
            "street": self.street,
            "suite": self.suite,
            "city": self.city,
            "zip_code": self.zip_code,
            "geo": self.geo.dict()
        }


class Company:
    """Esta classe receberá a empresa do usuário"""
    def __init__(
            self: object,
            name: str,
            catch_phrase: str,
            bs: str
    ) -> None:
        """Método construtor da classe Company"""
        self.__name = name
        self.__catch_phrase = catch_phrase
        self.__bs = bs
        return

    @property
    def name(self: object) -> str:
        """Property que retorna valor do campo name"""
        return self.__name

    @property
    def catch_phrase(self: object) -> str:
        """Property que retorna valor do campo catch_phrase"""
        return self.__catch_phrase

    @property
    def bs(self: object) -> str:
        """Property que retorna valor do campo bs"""
        return self.__bs


    def dict(self: object) -> dict:
        """Função que retorna dicionário com todos os dados"""
        return {
            "name": self.name,
            "catchPhrase": self.catch_phrase,
            "bs": self.bs
        }


class User:
    """Classe User"""
    def __init__(
            self: object,
            id: int,
            name: str,
            username: str,
            email: str,
            address: Address,
            phone: str,
            website: str,
            company: Company
             ) -> None:
        """Método construtor de User"""
        self.__id = id
        self.__name = name
        self.__username = username
        self.__email = email
        self.__address = address
        self.__phone = phone
        self.__website = website
        self.__company = company
        return


    @property
    def id(self: object) -> int:
        """property que retorna valor do campo id"""
        return self.__id

    @property
    def name(self: object) -> str:
        """property que retorna valor do campo name"""
        return self.__name

    @property
    def username(self: object) -> str:
        """property que retorna valor do campo username"""
        return self.__username

    @property
    def email(self: object) -> str:
        """property que retorna valor do campo email"""
        return self.__email

    @property
    def address(self: object) -> Address:
        """property que retorna valor do campo address"""
        return self.__address

    @property
    def phone(self: object) -> str:
        """property que retorna valor do campo phone"""
        return self.__phone

    @property
    def website(self: object) -> str:
        """property que retorna valor do campo website"""
        return self.__website

    @property
    def company(self: object) -> Company:
        """property que retorna valor do campo company"""
        return self.__company


    def dict(self: object) -> dict:
        """Função que retorna dicionário com todos os dados"""
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "address": self.address.dict(),
            "phone": self.phone,
            "website": self.website,
            "company": self.company.dict()
        }
