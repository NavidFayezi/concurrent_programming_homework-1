import random


def file_initializer():
    name_string = "file"
    for i in range(10):
        file_name = name_string + str(i) + ".txt"
        my_file = open(file_name, 'w')
        for j in range(100):
            my_file.write(str(random.randint(0, 100)) + '\n')


def read(filename):
    numbers = []
    file = open(filename)
    for lines in file:
        numbers.append(int(file.readline()))
    return numbers

if __name__ == "__main__":
    #file_initializer()
    print(read("file0.txt"))

