# + - * / ^

num1 = float(input("Numero 1 >>"))
oper = input()
num2 = float(input("Numero 2 >>"))

match oper:
    case '+':
        resul = num1 + num2
    case '_':
        resul = num1 - num2
    case '*':
        resul = num1 * num2
    case '/':
        resul = num1 / num2
    case '^':
        resul = num1 ** num2
    case _:
        print("Operación inválida")
        resul = "No ejecutado"

print(f"{num1} {oper} {num2} = {resul}")