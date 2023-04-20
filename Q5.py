def main():
    x,y  = int(input("Digite X: ")), int(input("Digite Y: "))
    if x>y:
        print(x, " é maior que ",y)
    elif y>x:
        print(y," é maior que ",x)
    else:
        print(x,"X é igual Y",y)
if __name__ == "__main__":
    main()