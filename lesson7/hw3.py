def make_operation(action, a, *args):
    if action=="+":
        return a + sum(args)

    if action == "-":
        for i in args:
            a -= i
        return a

    if action == "*":
        for i in args:
            a *= i
        return a

if __name__ == "__main__":
    print(make_operation("+", 1, 2, 3) == 6)
    print(make_operation("-", 10, 2, 3) == 5)
    print(make_operation("*", 5, 5) == 25)