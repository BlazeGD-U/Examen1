def suma(n1, n2):
    return n1 + n2


n1 = int(input("Digite el primer numero: "))
n2 = int(input("Digite el segundo numero: "))
op = str(input("escriba en minusculas 'sum' si quiere sumar, 'res' si quiere restar o 'mul' si quiere multiplicar: "))

if op == "sum":
    resul = suma(n1, n2)
    print(f"El resultado de la suma es: {resul}")
elif op == "res":
    pass
elif op == "mul":
    pass
else:
    print("DIGITE UN VALOR CORRECTO")
