'''
# playing with python lists and scopes
p1 = ["2", 2, "three"]
# the square braces takes in an index number
print(p1[2])
# the index() method returns the first occurence of an element on a list
print(p1.index(2))
# assigning an index replaces the element of a list in that index
p1[1] = 4
print(p1[1])
# cannot assign an object to a non-declared index
p2 = []
# p2[4]="this is a string"
# print(p2)
# p2[3].append("this is a second try")
p2.append("appended a string in the next index")
print(p2)
# functions have to be defined before it is called (unlike javascript)
def camel():
    #p1 is a global list
    p1.append("I'm a camel")
    print(p1)
camel()
def same_name():
    p1[1] = 'another string changed'
    print(p1)
same_name()
# positional arguments vs keyword arguments
def test_positiional(a,b,c):
    a = b+c
    b = a-c
    c = c*a
    print(a,b,c)
test_positiional(5,6,4)
def test_keyword(a=6,c=2,b=5):
    b = b+a
    c = c+b
    a*=a
    print(a,b,c)
test_keyword() # without parameter inputs, it will use the keywords, that is the value assigned to each variable
test_keyword(5,6,7) # with paramenter inputs, each variable name will be assigned the new input values respectively before executing the rest of function
test_keyword(10,11) # not all parameters have to be filled, those that are filled in the respective positions replaces the initially assigned value in the function definition
'''
# python dictionaries, key-value pairs and square brackets to fetch the property
definedVar = []
def a_foo():
    print("unlike JS, a method cannot be defined in the dictionary")
def some_foo():
    print("this won't be triggered")
a_list = ["only immutable data types can be stored in keys", "that is const type"]
my_dict = {
    "a_fine_day": "keys  must be in quotes unless it is a defined variable that exists",  
    "b_foo": a_foo,
    "c_foo": some_foo,
    a_foo: print("this print function is called in the dictionary 'cuz parenthesis"),
    "anotherList": ["list is in","a dictionary"]
}
# calling a function that is a value in a key in a dict
#parenthesis will call the function regardless if it's in the dict, but it will also return a keyError
my_dict["b_foo"] #gets b_foo's value which calls a_foo the global function defined outside
a_foo() #the global variable a_foo is unchanged
my_dict[a_foo] #this line doesn't do anything, a_foo in my_dict is a function with no output
my_dict["this_doesn't_exist"] = "something soon" #appends key-value to my_dict 
print(my_dict["this_doesn't_exist"])
my_dict["appendedKey"] = a_list # adding a list of items to my_dict
my_dict["appendedKey"].append("this item was appended")
my_dict["appendedKey"][1] = "this item was changed" # changing a key's value
print(my_dict["appendedKey"])

# my_dict = {}
# print(my_dict) # clear dictionary

# similar to foreach in JS and the "." key,
for key in my_dict:
    print(key)
    print(my_dict[key]) # global functions stored as value will not be called, instead the address of that function is returned. does it use pointers like in C?