# Assigning a variable for the first time. Just name and equal sign. If all caps (naming convention), it's a constant. Key value pair here is called a dictionary. Key can be a number. Square bracket and contents is called a list. Acts like an array. Values in '' are strings. Can be double quotes.
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# Instead of the word `function`, in Python, you use `def`. Template for function. a_kilobyte_is_1024_bytes=True is a keyword argument. Booleans are capitalized.
def approximate_size(size, a_kilobyte_is_1024_bytes=True):
# ''' docstring- internal documentation for function
    '''Convert a file size to human-readable form.

    Parameters:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024 if False, use multiples of 1000

    Returns: string

    '''
    # Function for returning an error. 
    if size < 0:
        raise ValueError('number must be non-negative')

# Checking if value of argument was changed. Terinary. multiple is 1024 if a_kilobyte_is_1024_bytes is true, otherwise it's 1000. line 24 is a for loop. Suffix is taco. Looping over list 1024 in SUFFIXES library. /= is the same as += but with division. If less than multiple, return string interpolation 
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
            # return f'{size:.1f} {suffix}' <--alternate way to do line 27
# line 30 is like an else in an if/else
    raise ValueError('number too large')
# If this is the main file, code below will execute. If it's imported into a different file as a module this statement won't execute. This is outside the function that starts on line 6 because of the indentation.
if __name__ == '__main__':
    print(approximate_size(16384, False))
    print(approximate_size(size=16384, a_kilobyte_is_1024_bytes=True))
    print(approximate_size(16384))

# At the top of another file: import humansizes

# Declare a var. Right side evaluated first.
sum = 2 + 2
# print(sum)

# == for comparison
print (sum == 4)

name = "Fred"
def say_name():
    global name
    name = "Bubba"
    print("internal", name)

say_name()
# print("external", name)

# if/else. Can put parenthesis or not. elif is else if
name = "Joe"
if (name == "Steve"):
    print("I feel great")
elif name == "Joe":
    print("You got the better intructor")
else: 
    print("I have a cold")

# string concatenation
# Still have dynamic typing but no implicit coercion
# print(f"My name is {2 + 2}")

# Collections
# List
junk = ["Fred", True, [1,2,3], 234]
# print(junk)

# .append takes one argument
junk.append("uh-oh")
# print(junk)

# .insert takes two arguments, first is position in list, second is the value
junk.insert(2, False)
# print(junk)

# Merges lists together
junk.extend(["One", "Two", "Three"])
# print(junk)

# seperator first, then .join then pass in what you're iterating over
names= ["Ball", "Train", "Boat"]
# print(", ".join(names))

# Dictionaries
my_pairs = {
  123: "number",
  "name": "Gabrielle"  
}

# print(my_pairs[123])
# print(my_pairs["name"])
my_pairs["last"] = "Jones"
# print(my_pairs)
my_pairs["address"] = {"number" : 123, "street" : "Cherry Tree Ln"}
# .values and .items and .keys
# print(my_pairs.items())
# print(my_pairs.keys())
# print(my_pairs.values())


# like dot notation but with brackets
street_name = my_pairs["address"]["street"]
# print(street_name)

# Sets check for identical entries and doesn't print duplicates
my_set = {"Fred", True, 123, "Jones", "Fred"}
# print(my_set)
# print(junk[5])

my_stuff = ["Fred", True, 123, "Jones", "Fred"]
# print(my_stuff)
# set turns list into set
# print(set(my_stuff))
# Using set but turning it back into a list to be able to use index positions
# print(list(set(my_stuff)))

my_set = {1, 2, 3}
my_set.add("Feed me")
# print(my_set)

# tuple
my_tup = (1, 2, 3, 3, "hello")
# print(my_tup)
# Can access index
# print(my_tup[0])

# Can change value
my_tup = ("WTF", "I'm hungry")
# print(my_tup)

# Can put comma even if only one tuple
my_little_tup = tuple("hello",)
print(isinstance(my_little_tup, tuple))

# loops
# for foo in junk:
    # print(f"Why do I still have {foo} in this drawer?")

# for foo in my_tup:
    # print(f"Why do I still have {foo} in this drawer?")

# for foo in my_set:
    # print(f"Why do I still have {foo} in this drawer?")

# for foo in my_pairs:
    # print(f"Why do I still have {my_pairs[foo]} in this drawer?")


# Slicing
my_list = [1,2,4, "hello", "monkey"]

# First number is first index position, second number is last desired index position
my_subset = my_list[0:3]
print(my_subset)