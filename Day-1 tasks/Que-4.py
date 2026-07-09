# Question 4: Function to Count Vowels
# Question: Create a function that accepts a string and returns the number of vowels (a, e, i, o, u) present in it. Print the count.
# Input: Programming

def counting_vowels(text):
    count = 0
    vowels = ("a,e,i,o,u,A,E,I,O,U")

    for char in text:
        if char in vowels:
            count+=1  
    return count
        
word = input("enter a string:")

print("your vowels count in string: ", counting_vowels(word))
