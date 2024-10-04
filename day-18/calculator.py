def calculator(first_number: int, second_number: int, operator: str) -> int:
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        return first_number / second_number
    
first_number : int = int(input("What's the first nummber? "))
print("+")
print("-")
print("*")
print("/")
operator : str = str(input("Pick an option: "))
second_number : int = int(input("What's the second number? "))
print(calculator(first_number, second_number, operator))