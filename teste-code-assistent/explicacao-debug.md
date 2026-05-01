# Explicação do Debug

## Erro encontrado

O erro estava na estrutura condicional if.

Código incorreto:

```python
if subtotal > 0:


# ARQUIVO 3 — num_primos.py

Cole:

```python id="x4g25h"
import math

def verificar_numero_primo(numero):

    if numero <= 1:
        return False

    limite = int(math.sqrt(numero)) + 1

    for divisor in range(2, limite):
        if numero % divisor == 0:
            return False

    return True


numero = int(input("Digite um número: "))

if verificar_numero_primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")