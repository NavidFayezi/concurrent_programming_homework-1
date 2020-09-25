import random
import threading


def file_initializer():                 # creates 10 file each containing 100 random integers
    name_string = "file"
    for i in range(10):
        file_name = name_string + str(i) + ".txt"
        my_file = open(file_name, 'w')
        for j in range(100):
            my_file.write(str(random.randint(0, 100)) + '\n')
        my_file.close()


def read(filename):                     # reads the numbers in a file and stores them in a list
    numbers = []
    file = open(filename)
    for lines in file:
        numbers.append(int(file.readline()))
    file.close()
    return numbers


def sortnwrite(filename):               # writes the sorted numbers back to the file
    numbers = read(filename)
    numbers.sort()
    my_file = open(filename, 'w')
    for number in numbers:
        my_file.write(str(number)+'\n')
    my_file.close()


if __name__ == "__main__":
    # file_initializer()
    threads = []
    for i in range(10):
        my_thread = threading.Thread(target=sortnwrite, args=("file"+str(i)+".txt",))
        my_thread.start()
        threads.append(my_thread)
    for i in range(10):
        threads[i].join()

