def main ():
    listnum = []
    mai = men = 0

    for i in range(0,100):
        listnum.append(int(input("Digite um Número ou '0' para encerrar a lista: ")))
        if listnum[i] == 0:
            listnum.remove(0)
            break
        if i == 0:
            mai = men = listnum[i]
        else:
            if listnum[i] > mai:
                mai = listnum[i]
            elif listnum[i] < men:
                men = listnum[i]

    print("Você digitou os valores,",listnum)
    print("O maior número digitado foi ", mai)
    print("O menor número digitado foi ", men)
   
if __name__ == "__main__":
    main()