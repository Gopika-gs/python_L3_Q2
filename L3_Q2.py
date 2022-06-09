from importlib.resources import contents


with open('readme.txt') as f:
    number_of_line = 3
    for i in range(number_of_line):
        content = f.readline()
        print(content)