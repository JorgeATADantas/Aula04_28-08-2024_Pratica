def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."
def main():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    choice = input("Digite o número da operação (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Entrada inválida.")
  
    if __name__ == "__main__":
      main()
