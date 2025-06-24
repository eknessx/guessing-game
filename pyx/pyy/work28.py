import random
import string



def abject(length=4):
    return ''.join(random.choices(string.ascii_letters+string.digits,k=length))

def generate_nested_dict():
    outer_key = abject()
    inner_key = abject()

    value = "Generated!"

    nested_dict = {
        outer_key: {
            inner_key: value
        }
    }
    return nested_dict
# Generate and print the nested dictionary
result = generate_nested_dict()
print(result) 