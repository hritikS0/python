#while

# i = 0;

# while i < 3 :
#     print("meow")
#     i = i + 1



# for 

# for i in range(10000):
#     print("meow");

# improvement
# for _ in range(1000):
#     print("meow")


# print("meow\n" * 3)

# Validating input

# while True:
#     n = int(input("whats n"))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow");

# def main():
#     num = get_number()
#     meow(num)

# def get_number():
#     while True:
#         n = int(input("Whats is your number ? "))
#         if n > 0:
#             break
#     return n
# def meow(n):
#     for _ in range(n):
#         print("meow")


# main() 


# Interating list

# list


# students = ["Hermione","Harry","Ron"];

# print(students[0])
# print(students[1])
# print(students[2])

# for i in range(len(students)):
#     print(i+1 ,students[i])


# dicts / dictionaries

# students = {
     
     
     
# }

# students = [
#     {
#     "name":"Hermione",
#     "house":"gryf",
#     "charm":"Otter"
#     },
#     {
#     "name":"Harry",
#     "house":"gryf",
#     "charm":"Dear"
#     },
#     {
#     "name":"Ron",
#     "house":"gryf",
#     "charm":"Jack"
#     }
# ]
# for student in students:
#     print(student["name"])


#  mario

# def main():
#     print_column(3);

# def print_column(he):
#     for _ in range(he):
#         print("#")

# main()


# def main():
#     print_row(4);

# def print_row(w):
#     print("?" * w)

# main()

def main():
    print_square(10)



def print_square(size):
    for i in range(size):
        # for j in range(size):
        #     print("#",end="")
        print("#" * size)

main()