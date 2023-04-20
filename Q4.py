def main ():
    i = int(input("Digite um Número: "))
    if i < 0:
        print("Esse número e negativo.")
    elif i > 0:
        print("Esse número e positivo.")
    else:
        print("Esse número é nulo.")

if __name__ == "__main__":
    main()