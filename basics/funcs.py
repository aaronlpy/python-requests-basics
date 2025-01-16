
def greetings(user: str):
    return f"Hello {user}!!"

print(greetings('Pepe'))

user = "Aaronlopezo"
print(user.upper())
print(len(user))
print(user[0:8])
print(user.capitalize())
print(user.lower())

if user.islower():
    print("is lower")