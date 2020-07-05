# **Programming Assignment for CSPC**

# Question Assigned : Q1. a)

# Problem Statement : Write a program to show how basic set operations such as union and intersection can be implemented when set is represented as bit-string.

# **Programming Language Used** : ***Python Version 3.8***

# **3rd Party Function Used** : **bitset()** function from **bitsets** module in order to create a Universal Set Class and to represent sets as bitstrings.

# **Kindly note that the module was only used for storing the sets as bit-strings and creating a Universal Set class. In-built functions for set operations have not being used.**

# ---

# **How the program has been implemented ?**



# *   As mentioned above, the bitset function from bitsets was used to create a UniversalSet class.
# *   The user is asked to input a Universal Set where elements taken as a string with space separating the elements.
# *   In order to ask input of sets which belong to the Universal Set, the function set_input is defined which takes elements in string format for the Universal Set and in set form for sets to be operated.
# *   In the set_union(), set_intersect() and set_complement() functions, the UniversalSet(argument set).bits() function is called to get the bitstring of the argument sets. The bitstrings are stored in list variables x and y where each element corresponds to bit position and is either '0' or '1' (in string form). We create another list z in which we store the results of the bitwise operations of the elements in X and Y. The list z is passed on to list_as_set() function to get set corresponding to the bitstring in z, and a set is returned.
# *   The set_diff() and set_symdif() functions are defined to find the set difference and symmetric differences of the argument sets. Implementation makes use of the previously defined set operation functions.
# *   The set_as_bitstring function is defined to show the bitstring representation of any set that is part of the UniversalSet class. This function also makes use of the bits() function of the UniversalSet class.

# ---
# The program is as follows, kindly implement all code blocks to get proper results.

# Remarks : bitsets module is to be installed if the code is to be implemented in local IDE.









!pip install bitsets
# Program to implement set operations on sets represented by bit-strings

# Importing bitset to create universal set class and implement bitset representation
from bitsets import bitset 

# Function to take input of set in set notation 
def set_input(x):
        try:
          y = list(x.split())
        except:
          y = list(x)
        return y

print("Enter Sets sequentially as a string with "" to separate elements- ")
x = input("Enter Universal Set as string- ")
U = tuple(set_input(x))
# Creating UniversalSet Class with the help of bitset() function
UniversalSet = bitset('UniversalSet', U)

# Function for user to get bitstring representation of any set that is a subset of the universal set U
def set_as_bitstring(A):
    return UniversalSet(A).bits()


# Function to convert bitstring stored as list to standard set form
def list_to_set (A):
    str1 = ""
    for item in A:
        str1 += item
    return list(UniversalSet.frombits(str1))


# Function that shows the working of set intersect operation with sets as bitstrings
def set_intersect (A, B):
    x = list(UniversalSet(A).bits())
    y = list(UniversalSet(B).bits())
    # z is the list that stores the elements of the bit string as it's elements
    z = ['1' for i in range(len(U))]
    # The following loop implements Bitwise And on string elements that are stored as '1' and '0'
    for i in range(len(U)):
        if(x[i] == '1' and y[i] == '1'):
            z[i] = '1'
        else:
            z[i] = '0'
    # The list_to_set() function is called to convert the list z to standard set form
    Z = list_to_set(z)
    return Z 

# Function that shows the working of set union operation with sets as bitstrings
def set_union (A,B):
    x = list(UniversalSet(A).bits())
    y = list(UniversalSet(B).bits())
    # z is the list that stores the elements of the bit string as it's elements
    z = ['1' for i in range(len(U))]
    # The following loop implements Bitwise Or on string elements that are stored as '1' and '0'
    for i in range(len(U)):
        if(x[i] == '0' and y[i] == '0'):
            z[i] = '0'
        else:
            z[i] = '1'
            
    # The list_to_set() function is called to convert the list z to standard set form
    Z = list_to_set(z)
    return set(Z)    

# Function that shows the working of set complement operation with sets as bitstrings
def set_complement (A):
    x = list(UniversalSet(A).bits())
    # z is the list that stores the elements of the bit string as it's elements
    z = ['1' for i in range(len(U))]
    # The following loop implements Bitwise Not on string elements that are stored as '1' and '0'
    for i in range(len(U)):
        if(x[i] == '0'):
            z[i] = '1'
        else:
            z[i] = '0'
    # The list_to_set() function is called to convert the list z to standard set form
    Z = list_to_set(z)
    return set(Z) 

# Function that shows the working of set difference operation with sets as bitstrings            
def set_diff(A,B):
    Z = set_intersect(A, list(set_complement(B)))
    return set(Z)

# Function that shows the working of set symmetric difference operation with sets as bitstrings
def set_symdif(A,B):
    return set_union(list(set_diff(A,B)), list(set_diff(B,A)))


print("In order to create new sets and perform operations, do the following. \n Ex: declare A = set_input(x) where x is a set containing the elements\n For union - set_union\n intersection- set_intersect \n complement - set_complement \n set difference - set_diff \n symmetric difference - set_symdif \n set as bitstring - set_as_bitstring")
print("The universal set is-", U, "and it's bitstring representation is-", UniversalSet(U).bits())


