import pika
import datetime

# Conectar ao servidor RabbitMQ usando o nome do serviço definido no Docker Compose
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
# Declarar a fila
channel.queue_declare(queue='hello')


# Original string
body = 'Hora:'

# Get current time
current_time = datetime.datetime.now()

# Format the time as a string, e.g., HH:MM:SS
time_str = current_time.strftime('%H:%M:%S')

# Concatenate the time to the original string
body_with_time = body + ' ' + time_str

# Enviar uma mensagem
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=body_with_time)
                      
print(" [x] Sent 'Hello World!'")

# Fechar a conexão
connection.close()
