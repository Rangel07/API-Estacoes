import hashlib
import string
import random

def gerar_hashcode():
    n = random.randint(30,50)
    letras = string.ascii_letters
    gerador = ''.join(random.choice(letras) for i in range(n))
    sha_signature = hashlib.sha256(gerador.encode()).hexdigest()
    return sha_signature