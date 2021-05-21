from src.posts import donwload_posts
from src.users import  donwload_users
from uuid import uuid4
import pika
import json


def send_posts(queue: str = "posts_jsonplaceholder", salvar_json: bool = True) -> None:
    """function send posts to rabbit"""
    users = donwload_users()
    posts = donwload_posts()
    for key, value in posts.items():
        print(f"Post de id: {key} sendo enviado!")
        post = value.dict()
        post["user"] = users[post['user_id']].dict()
        post.pop("user_id")
        if salvar_json:
            guid_post = str(uuid4())
            file_local = f"src//json_files//requests//{guid_post}.json"
            with open(file_local, "w") as file:
                json.dump(post, file)
                print(f"Post que foi enviado: {file_local}")
        print(f"Post: {post}")
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        channel = connection.channel()
        channel.queue_declare(queue=queue)
        channel.basic_publish(
            exchange='',
            routing_key=queue,
            body=str(post)
        )
        channel.close()
        connection.close()
    return


def receive_message(queue: str = "posts_jsonplaceholder") -> None:
    """
    function receive message for rabbit
    """
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        channel = connection.channel()
        channel.queue_declare(queue=queue)
        channel.basic_consume(
            queue,
            lambda ch, method, properties, body: print(f"[x] receive {body}"),
            auto_ack=True
        )
        print(f"[*] waiting for messages.")
        channel.start_consuming()
        connection.close()
    except Exception as err:
        print(f"message {(str(err))}")
        return False

