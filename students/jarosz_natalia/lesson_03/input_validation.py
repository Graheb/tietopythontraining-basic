def collatz(arg):
    if arg % 2 == 0:
        print(arg // 2)
        return arg // 2
    else:
        print(3 * arg + 1)
        return (3 * number) + 1


try:
    number = int(input())
    collatz(number)
except ValueError:
    print("You did not enter a number.")
