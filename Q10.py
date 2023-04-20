def main ():
    listnum = []

    for i in range(0,100):
        listnum.append(int(input("Digite um Número ou '0' para encerrar a lista: ")))
        if listnum[i] == 0:
            listnum.remove(0)
            break
    print("Os números pares digitados ", end="")
    for c in range(0,len(listnum)):
        if listnum[c] % 2 == 0:
            print(listnum[c], end=" ")

if __name__ == "__main__":
    main()