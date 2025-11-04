import socket
import threading
import pika

def handle_cliente(connection, address, channel):
    print(f"[Se ha establecido conexión] {address}")
    while True:
        data = connection.recv(1024)
        if not data:
            break
        task = data.decode()
        print(f"[Mensaje recibido] {task}")

        channel.basic_publish(
            exchange='', 
            routing_key='task_queue', 
            body=task)
        connection.send(b"Se ha recibido la tarea")
    connection.close()
    print(f"[Se ha cerrado la conexión] {address}")

def start_server():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue')

#Configuramos el socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0' , 9999))
    server.listen()
    print("[Se ha iniciado el servidor] Se están esperando conexiones")

    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_cliente, args=(connection, address, channel))
        thread.start()

if __name__ == "__tarea__":
    start_server()