def table(input_number):
    temp = 0
    for i in range(10):
        temp += 1
        line = input_number * temp
        print(f"{input_number} x {temp} = {line}")

input_number = int(input())
table(input_number)
