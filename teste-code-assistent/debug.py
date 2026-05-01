cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

subtotal = qtd1 * item1

if subtotal > 0:
    print("Compra válida")