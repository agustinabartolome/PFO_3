import pika
import time

def callback(ch, method, properties, body):
    task = body.decode('utf-8')
    print(f"[Worker] Se ha recibido la tarea: {task}")
    

    time.sleep(2)
    
    print(f"[Worker] Se ha completado la tarea: {task}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_worker():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue')

    
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)

    print("[Worker] Esperando las tareas.")
    channel.start_consuming()

if __name__ == "__tarea__":
    start_worker()
