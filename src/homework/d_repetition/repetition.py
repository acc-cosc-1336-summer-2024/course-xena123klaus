def get_factorial(num):
    if num < 0:
        return "Invalid Input"
    
    factorial = 1
    
    for i in range(1, num + 1):
        factorial *= i
    return factorial


def sum_odd_numbers(num):
    sum_odds = 0
    current_number = 1

    while current_number <= num:
        if current_number % 2 != 0:
            sum_odds += current_number
        current_number += 1
        
    return sum_odds



def menu():
    while True:
        print("Homework 3 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit")

        choice = input("Enter your Choice: ")

        
        
        
        
        
        if choice == "1":
            while True:
                num = int(input("Enter a number between 1 and 9: "))
                if 1<= num < 10:
                    print("The factorial of" , num, "is" , get_factorial(num))
                    break
                else:
                    print("Invalid input, Enter a number between 1 and 9")

        elif choice == "2" :
            while True:
                num = int(input("Enter a number between 1 and 99: "))
                if 1 <= num < 100:
                    print("The sum of odd numbers up to", num, "is" , sum_odd_numbers(num))
                    break
                else:
                    print("Invalid input. Enter a number between 1 and 99")

        elif choice == "3" :
            exit_choice = input("Do you want to exit? (yes/no): ")
            if exit_choice == "yes":
                print("Exiting the program")
                break

        else:
            print("Invalid choice. Please select a real option")

        continue_choice = input("Do you want to continue? (yes/no): ")
        if continue_choice != "yes" :
            print("Exiting the program ")
            break

