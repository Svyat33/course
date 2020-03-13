my_name = "Svyatoslav"
currday = "Неділя"
print("Good day "+my_name+"! "+currday+" is a perfect day to learn some python.")
print("Good day %s! %s is a perfect day to learn some python." % (my_name, currday))
print("Good day {}! {} is a perfect day to learn some python.".format(my_name, currday))
print("Good day {1}! {0} is a perfect day to learn some python.".format(currday, my_name))
print(f"Good day {my_name}! {currday} is a perfect day to learn some python.")

name = "Svyatoslav"
lname = "Kosenchuk"
print(name + " " + lname)

a = 8
b = 5
print("Addition\t\ta+b=", (a + b)  )
print("Subtraction\t\ta-b=", (a - b)  )
print("Division\t\ta/b=", (a / b)  )
print("Multiplication\t\ta*b=", (a * b)  )
print("Exponent\t\ta^b=", (a**b)  )
print("Modulus\t\t\ta%b=", (a % b)  )
print("Floor division\t\ta//b=", (a//b)  )

# задание на умение форматировать значения
print("{:0>6d} {} {:b} {:.2f}".format(12, "Василий", 54, 32.1))

# умение нарезать строки на слайсы
word = "Корован"
print(word[4].upper()+word[1]+word[2]+word[1]+word[6]+word[5])
print((word[4:0:-1] + word[6:4:-1]).title())