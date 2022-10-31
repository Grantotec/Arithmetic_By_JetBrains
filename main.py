import random


class Qlight:
    def __init__(self):
        self.question = str(random.randint(2, 9)) + " " \
                        + random.choice(["+", "-", "*"]) + " " \
                        + str(random.randint(2, 9))
        expression = self.question.split()
        a = int(expression[0])
        b = int(expression[2])

        if expression[1] == "+":
            self.answer = a + b
        elif expression[1] == "-":
            self.answer = a - b
        elif expression[1] == "*":
            self.answer = a * b

    def __str__(self):
        return f"{self.question}"


class Qhard:
    def __init__(self):
        self.question = str(random.randint(11, 29))
        self.answer = int(self.question) * int(self.question)

    def __str__(self):
        return f"{self.question}"


def menu_1():
    q = Qlight()
    print(q)
    while True:
        try:
            answer = int(input(""))
            break
        except ValueError:
            print("Wrong format! Try again.")
    if answer == q.answer:
        print("Right!")
        return True
    else:
        print("Wrong!")
        return False


def menu_2():
    q = Qhard()
    print(q)
    while True:
        try:
            answer = int(input(""))
            break
        except ValueError:
            print("Wrong format! Try again.")
    if answer == q.answer:
        print("Right!")
        return True
    else:
        print("Wrong!")
        return False


def main():
    diff = input("Which level do you want? Enter a number:\n"
                 "1 - simple operations with numbers 2-9\n"
                 "2 - integral squares of 11-29\n")
    while diff not in ["1", "2"]:
        print("Incorrect format.")
        diff = input("Which level do you want? Enter a number:"
                     "1 - simple operations with numbers 2-9"
                     "2 - integral squares of 11-29\n")

    correct_light = 0
    correct_hard = 0

    if diff == "1":
        for i in range(5):
            if menu_1():
                correct_light += 1
        print(f"Your mark is {correct_light}/5. Would you like to save the result? Enter yes or no.")
        choice = input()
        if choice in ["yes", "YES", "y", "Yes"]:
            f = open("results.txt", "a")
            name = input("What is your name?\n")
            f.write(f"{name}: {correct_light}/5 in level 1 (simple operations with numbers 2-9)")
            print('The results are saved in "results.txt".')
        else:
            exit()
    elif diff == "2":
        for i in range(5):
            if menu_2():
                correct_hard += 1
        print(f"Your mark is {correct_hard}/5. Would you like to save the result? Enter yes or no.")
        choice = input()
        if choice in ["yes", "YES", "y", "Yes"]:
            f = open("results.txt", "a")
            name = input("What is your name?\n")
            f.write(f"{name}: {correct_hard}/5 in level 2 (integral squares 11-29)")
            print('The results are saved in "results.txt".')
        else:
            exit()


if __name__ == "__main__":
    main()
