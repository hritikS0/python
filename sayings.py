def main():
    hello("world")
    goodby("world")

def hello(name):
    print(f"hello, {name}");

def goodby(name):
    print(f"goodbye, {name}")

# will not run main function
if __name__ == "__main__": 
    main()