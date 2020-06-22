def Condition(number):
    if number % 2 != 0:
        print("Weird")
    if number % 2 == 0:
        if 1 < number < 6:
            print("Not Weird")
        elif 5 < number < 21:
            print("Weird")
        if number > 20:
            print("Not Weird")
    return None

number = int(input())
Condition(number)