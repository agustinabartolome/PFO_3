import socket

def send_task(task):
    try:

        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(('localhost', 9999))
    
        cliente.send(task.encode())
    
        response = cliente.recv(1024).decode('utf-8')
        print(f"[Respuesta dada por el servidor] {response.decode()}")
    
    except ConnectionRefusedError:
        print("No se ha podido realizar la conexion con el servidor")
    
    finally:
        cliente.close()


if __name__ == "__tarea__":
    while True:
        tarea = input("Ingrese una tarea o salir para terminar")
        if tarea.lower() == 'salir':
            break
        send_task(tarea)