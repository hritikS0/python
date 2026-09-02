# names = []

# for _ in range(3):
#     names.append(input("Whats your name?"))

# for name in sorted (names):
#     print(f"hello {name}")


name = input("whats yours name?")
file = open("name.txt","a")
file.write(name)
file.close()