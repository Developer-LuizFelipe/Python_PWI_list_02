def main ():
    listnum = []
    soma = 0

    for i in range(0,100):
        listnum.append(int(input("Digite um Número ou '0' para encerrar a lista: ")))
        if listnum[i] == 0:
            listnum.remove(0)
            break
        soma=soma+listnum[i]

    print("A soma dos números digitados é ", soma)

if __name__ == "__main__":
    main()