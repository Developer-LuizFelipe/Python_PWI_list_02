def fib(n):
    if n<2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def main ():
    n = int(input("Digite um número :"))
  
    for i in range(0,n):
        fi= fib(n)
        if fi<=n:
            print(fi,end=" ")
        else:
            break
            


if __name__ == "__main__":
    main()
