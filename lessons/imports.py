""""The file where I import stuff"""

from lessons import my_functions

#or can say

from lessons.my_functions import add

if __name__ == "__main__":
    print(my_functions.add(4,5))

print(my_functions.my_variable)
# when you import stuff it steps into the file and veiws the name there
    # whatever function you are on has the name __main__
    #anything you are importing will NOT have that name


