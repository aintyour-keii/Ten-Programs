odd = 0

for i in range(10):
    user_input = int(input("Enter a number: "))
    if user_input % 2 == 1:
        odd += 1

print(odd)