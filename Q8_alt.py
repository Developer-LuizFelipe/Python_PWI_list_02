def main ():
    listnum = []

    for i in range(0,100):
        listnum.append(int(input("Digite um Número ou '0' para encerrar a lista: ")))
        if listnum[i] == 0:
            listnum.remove(0)
            break

    
    print("Você digitou os valores,",listnum)
    listnum.sort()
    print("O maior valor digitado foi ", listnum[len(listnum)-1])
    print("O menor valor digitado foi ", listnum[0] )
   
if __name__ == "__main__":
    main()