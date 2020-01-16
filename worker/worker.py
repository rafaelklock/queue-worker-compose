import redis, os, json
from time import sleep 
from random import randint

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')
    r = redis.Redis(host=redis_host, port=6379, db=0)
    print('Worker runnin...')
    while True:
        print('+ Verificando a fila no redis...')
        mensagem = json.loads(r.blpop('sender')[1])
        assunto = mensagem['assunto']
        # simulando envio de email
        print(f'mandando a mensagem: {assunto}')
        sleep(randint(10, 15))
        print(f'mensagem enviada {assunto}')

