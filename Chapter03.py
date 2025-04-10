#Automate The Boring Stuff practice projects
#Phillip Oiwoh
#Chapter 3

def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return(number)
    elif number % 2 == 1:
        number = 3 * number + 1 
        print(number)
        return number

try:
    print("Enter number:")
    number = input()
    while(number!=1):
        number = collatz(int(number))
        
except ValueError:
    print("Please enter interger value")
    





