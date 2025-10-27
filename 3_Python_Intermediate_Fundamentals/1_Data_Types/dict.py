# Empty dictionary
empty_dict = {}
empty_dict = dict()

# Dictionary with items
person = {
    'name': {
        'first': 'Alice',
        'last': 'Smith'
    },
    'age': [30, 25, 35],
    'profession': ['Engineer', 'Designer', 'Manager']
}
print()
print(person['name']['last'])

# # Using dict() constructor
# person2 = dict(name='Bob', age=25, profession='Designer')

# # Accessing values
# print()
# print(person)
# print(person['name'])  # Alice
# print(person.get('age'))  # 30
# print(person.get('salary', 'Not specified'))  # Not specified (default value)
