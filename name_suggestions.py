import random
import string


# Generate a random name
def generate_random_name(length=5):
    vowels = 'aeiou'
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
    name = ''.join(random.choice(consonants if i % 2 == 0 else vowels) for i in range(length))
    return name.capitalize()


# Generate a list of 100,000 random names
def generate_names_database(size=100000):
    return [generate_random_name(random.randint(3, 8)) for _ in range(size)]


# Create the names database
names_database = generate_names_database()


# Function to suggest names
def suggest_names(input_string, database=names_database):
    input_string = input_string.lower()
    suggestions = [name for name in database if all(char in name.lower() for char in input_string)]
    return suggestions[:5]  # Return at most 5 suggestions


if __name__ == "__main__":
    user_input = input("Enter a name or alphabets: ")
    print(suggest_names(user_input))
