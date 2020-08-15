file = open('test.txt')
# read all the contents of file.
# You can put how many bytes to read(characters)
# print(file.read(5))

#Read one single line at a time readline()
# print(file.readline())
# print(file.readline())

# Print line by line using readline method1
#line = file.readline()
#while line != "":
#    print(line)
#    line = file.readline()


#with Readlines each line will be stored in a list
# values = ["abc", "asdasd", "cat", "dog", "elephtant"]
for line in file.readlines():
    print(line)


file.close()


