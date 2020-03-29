def mymath(a,b):
    try:
        x,y = int(a), int(b)
        return x**2 / y
    except ValueError:
        print("Произошла ошибка при приведении типа")
    except ZeroDivisionError:
        print("Деление на ноль дает бесконечность, а ее нам не в чем хранить")

        