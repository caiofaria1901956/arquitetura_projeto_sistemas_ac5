""""
Este programa irá fazer o download de posts na jsonplaceholder
e irá envia-los para uma fila do rabbitmq
"""
from src.rabbitmq import send_posts, receive_message
from conf import Configuracao
from multiprocessing import Process

def main() -> None:
    conf = Configuracao()
    conf.carregar_configuracao()
    p1 = Process(target=send_posts, kwargs={
        "queue": "posts_jsonplaceholder",
        "salvar_json": conf.salvar_json
    })
    p2 = Process(target=receive_message, kwargs={
        "queue": "posts_jsonplaceholder"
    })
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    return
if __name__ == "__main__":
    main()