# This function will figure out if an integer is odd or even. Give it a try! #
def Is_Odd_Even(number):
    if number %2==0:
        print("Even!")
    elif number %2==1:
        print("Odd!")
    else:
         print("This isn't a number.")

# Call the function, and in the parameter, type an integer. #
Is_Odd_Even(2)

Is_Odd_Even(3)

#Honestly, we could make this much simpler:
def Is_Odd_Even(number):
    if number %2==0:
        print("Even!")
    else:
         print("Odd!")

#Given a list of integers, pass the list through a function to output a phone number in this form: "(555) 555-5555"
# This solution is absolutely crazy-good that I saw from other users on a code challenge site!
def phone(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(phone([2, 3, 4, 5, 6, 7, 7, 8, 9, 3]))

# This was my solution:
def number(n):
    new = "".join(map(str, n))
    return f"({new[:3]}) {new[3:6]}-{new[6:]}"
