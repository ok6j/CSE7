def reverse_order(first_name, last_name):
    # print("%s %s" % (last_name, first_name))
    print("%s %s" % (last_name, first_name))  # Concatenation


def reverse_order():
    first_name = input('What is your first name?')
    last_name = input('What is your last name?')
    print("%s %s" % (last_name, first_name))


"""Warmup #2
Write a function called "happy_bday" 
that "sings" (prints)
the Happy Birthday song

It must take one parameter called "name"
"""

def happy_bday(name):
    print("Happy birthday to you")
    print("Happy birthday to you.")
    print("Happy birthday dear " % name)
    print("Happy birthday to you!")


def add_py(name):
    print("%s .py % name")  # Solution 1
    print(name + ".py")  # Solution 2


def add(num1, num2, num3):
    print(num1, + num2 + num3)


# add(90, 900, 9000)


def repeat(string):
    print(string)
    print(string)
    print(string)

    for x in range(3):
        print(string)


