def table(num):
    range=int(input("enter range of table: "))
    while range>=1:
        print(num,"*",range,"=",num*range)
        range=range-1
def main():
    table(5)
if __name__ == '__main__':
    main()