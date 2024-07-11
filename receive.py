import pika

# Conectar ao servidor RabbitMQ usando o nome do serviço definido no Docker Compose
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

# Declarar a fila. A fila precisa ser declarada em ambos os scripts para garantir que ela exista.
channel.queue_declare(queue='hello')

# Definir uma função de callback que será chamada quando uma mensagem for recebida
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Configurar a assinatura da fila
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
