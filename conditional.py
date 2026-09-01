# > GREATER THAN
# >= GREATER THAN EQUAL TO
# < LESS THAN
# <= LESS THAN EQUAL TO
# == EQUAL
# != NOT EQUAL

# compare

#if
#elif
#or
# x = int(input("whats x "))
# y = int(input("whats y "))


# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x and y are equal");


# if x != y:
#     print("x is not equal to y")
# else: 
#     print("x is equal to y")

def main():
    x = int(input("Whats x"))
    if isEven(x):
        print("Even")
    else:
        print("Odd")
def isEven(n):
    return n % 2 == 0
   

main()


