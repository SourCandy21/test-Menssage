import boto3
#Criando um cliente SQS

sqs = boto3.cliente('sqs')

# Criando uma fila SQS
response = sqs.create_queue(
    QueueName='fila-teste',
    Attributes={'DelaySeconds': '5'}
    )

print(response['Queue1'])

# URL da Fila obtida nteriormente
queue_url = response['QueueUrl']

# Enviar mensagem para a fila 
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody = 'Mensagem de Teste'
)

print(response['MessageId'])

# Receber mensagem da fila
message = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1
)

if 'Messages' in message:
  message = message['Messages'][0]
  receipt_handle = message['ReceiptHandle']
  
  # Processar a mesagem aqui

  # Deletar a mensagem da fila após o processamento 
  sqs.delete_message(
      QueueUrl=queue_url,
      ReceiptHandle=receipt_handle
  )
  