import random


def suggest_names(input_string):
    names_database = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
    suggestions = [name for name in names_database if all(char in name for char in input_string)]
    return suggestions[:3]


if __name__ == "__main__":
    user_input = input("Enter a name or alphabets: ")
    print(suggest_names(user_input))
