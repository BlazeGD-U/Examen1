def suma(n1, n2):
    return n1 + n2


def res(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


n1 = int(input("Digite el primer numero: "))
n2 = int(input("Digite el segundo numero: "))
op = str(input("escriba en minusculas 'sum' si quiere sumar, 'res' si quiere restar o 'mul' si quiere multiplicar: "))

if op == "sum":
    resul = suma(n1, n2)
    print(f"El resultado de la suma es: {resul}")
elif op == "res":
    resul = res(n1, n2)
    print(f"El resultado de la resta es: {resul}")
elif op == "mul":
    resul = mul(n1, n2)
    print(f"El resultado de la multiplicacion es: {resul}")
else:
    print("DIGITE UN VALOR CORRECTO")
