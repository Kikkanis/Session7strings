# USEFUL STRING METHODS

print(dir("hello"))

print(help("hi".capitalize))

print("i like to go to school".capitalize())
print("IS THIS SUPPOSED TO WORK?".capitalize())

print(help("hi".center))

print("hello".center(40, "x"))

# find command tells you where to find the value. If it doesnt fint anything, it will return -1
print("gmail.com".find("john"))

s = "i see a cat who likes to cat while i cat on a cat"
# find all occurrences
poz = 0
while True:
    poz = s.find("cat", poz)
    if poz == -1:
        break
    print("found at on position", poz)
    poz += 1

# join - we will come back to this later
# lower case everything:
s = "I SEE A LOT OF THINGS!"
print(s.lower())

# upper - capitalizes EVERYTHING:
s = "i see a lot of things"
print(s.upper())
# upper - capitalizes EVERYTHING: You may counter this with .capitalize:
s = "i see a lot of things"
print(s.upper().capitalize())

# replace - replaces X with Y:
s = "i see a cat who like to beat a rat. what a good cat"
print(s.replace("c", "r"))

# title - makes all words have capitalize letter in the beginning. like the title of a book
s = "i like the mountains"
print(s.title())

# split - splits all words
s = "I like to go shopping"
print(s.split())
splitted = s.split()
print("XX".join(splitted))

