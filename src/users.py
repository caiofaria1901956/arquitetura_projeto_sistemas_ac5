from src.models.users import Geo, Address, Company, User
import requests


def donwload_users() -> dict:
    """Função que realiza o download de todos os users do jsonplaceholder"""
    dict_return = {}
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    if users.status_code != 200:
        return {
            "error": users.text
        }
    for user in users.json():
        geo = Geo(
            lat=user['address']['geo']['lat'],
            lng=user['address']['geo']['lng']
        )
        address = Address(
            street=user["address"]["street"],
            suite=user["address"]["suite"],
            city=user["address"]["city"],
            zip_code=user["address"]["zipcode"],
            geo=geo
        )
        company = Company(
            name=user["company"]["name"],
            catch_phrase=user["company"]["catchPhrase"],
            bs=user["company"]["bs"]
        )
        dict_return[user["id"]] = User(
            id=user["id"],
            name=user["name"],
            username=user["username"],
            email=user["email"],
            address=address,
            phone=user["phone"],
            website=user["website"],
            company=company
        )
    users.close()
    return dict_return