#print("hello world");
# functions 
# functions ->   Functions are reusable blocks of code designed to 
#                into smaller , manageable sections and reducing code duplication.
#                perform a specific task, helping to organize programs

#name = input("What is your name? ").strip().title();
#built-in function that captures user input from the keyboard, displaying an optional prompt message and waiting for the user to press Enter.  
#It always returns the entered data as a string, regardless of whether the user types numbers, text, or symbols. 

# String methods

# to remove whitespace from string
#name = name.strip(); 

# Capitalize users name
#name = name.capitalize()

#
#name = name.strip().title();

# split users name into first name and lastname
#first, last = name.split(" ");

#print("heloo "+ name);
#print("hello", sep="???");
#print('hello, "friend" ');
#print(f"hello,{name}");
#print(first , last)



# Functions 

def main():
    name = input("What is your name? ")
    hello(name)

def hello(name="World"):
    print("Hello, ",name)


main()