from src.models.posts import Posts
import requests


def donwload_posts() -> dict:
    """Função que realiza o download de todos os posts"""
    dict_return = {}
    posts = requests.get("https://jsonplaceholder.typicode.com/posts")
    if posts.status_code != 200:
        return {
            "error": posts.text
        }
    for post in posts.json():
        post_object = Posts(
            user_id=post["userId"],
            id=post["id"],
            title=post["title"],
            body=post["body"]
        )
        dict_return[post_object.id] = post_object
    posts.close()
    return dict_return
