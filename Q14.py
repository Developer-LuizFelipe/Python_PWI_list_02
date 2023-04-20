def main ():
    listnum = []

    for i in range(0,100):
        listnum.append(int(input("Digite um Número ou '0' para encerrar a lista: ")))
        if listnum[i] == 0:
            listnum.remove(0)
            break
    listnum.sort(reverse=True)
    print("Os numeros digitados foram: ", listnum)

if __name__ == "__main__":
    main()