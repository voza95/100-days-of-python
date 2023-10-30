name = input("What is you name?\n")
print("Hello " + name + "!!\n")
print("You have " + str(len(name)) + " characters in your name.\n")

print("Now let's switch two vaiables.")
a = input("a: ")
b = input("b: ")

print("Final output after swap:")
a, b = b, a
print("a: " + a)
print("b: " + b)