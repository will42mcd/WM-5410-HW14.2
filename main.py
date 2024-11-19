# Switcher code taken from: https://data-flair.training/blogs/python-switch-case/
# Author: DataFlair Team
# Acessed on 11/18/2024
# License: None Listed
# Changelog: 
#   -applied to a calculator program and added driver code


class Switcher(object):
    def indirect(self,i):
            method_name='number_'+str(i)
            method=getattr(self,method_name,lambda :'Invalid')
            return method()
    def menu(self):
        print("+ Addition")
        print("- Subtraction")
        print("* Multiplication")
        print("/ Division")
        print("pow Raise A to power of B")
    def number_0(self):
        a = int(input("Enter A:"))
        b = int(input("Enter B:"))
        return a+b
    def number_1(self):
        a = int(input("Enter A:"))
        b = int(input("Enter B:"))
        return a-b
    def number_2(self):
        a = int(input("Enter A:"))
        b = int(input("Enter B:"))
        return a*b
    def number_3(self,a,b):
        a = int(input("Enter A:"))
        b = int(input("Enter B:"))
        return a/b
    def number_4(self):
        a = int(input("Enter A:"))
        b = int(input("Enter B:"))
        return a**b
    
def main():
    sw=Switcher()
    sw.menu()
    # input choice
    ch=input("Enter Choice: ")
    if ch == '+':
        print(sw.indirect(0))
    elif ch == '-':
        print(sw.indirect(1))
    elif ch == '*':
        print(sw.indirect(2))
    elif ch == '/':
        print(sw.indirect(3))
    elif ch == 'pow':
        print(sw.indirect(4))
#end main()

if __name__ == "__main__":
    main()