def main():
    student = get_student()
    if student[0] == "padma":
        student[1] = "RavenClaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("name : ")
    house =  input("House : ")
    return [name,house]

if __name__ == "__main__":
    main()