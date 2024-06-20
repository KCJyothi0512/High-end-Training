'''i/p: aaabbaaaaddd i,i+1,-1
o/p: a3b2a4d3'''
a="aaabbaaaadddb"
c=1
b=''
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        c=c+1
    else:
        b=b+a[i]+str(c)
        c=1
b=b+a[-1]+str(c) #i+1 ,-1 #i will not take last when the string is aaabbaaaadddb
print(b)
    
'''def print_duplicates(string):
    # Convert string to lowercase to treat uppercase and lowercase letters as the same
    string = string.lower()
    
    # Dictionary to store character counts
    char_count = {}
    
    # Iterate through the string to count characters
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Flag to track if any duplicates are found
    found_duplicates = False
    
    # Iterate over the dictionary to print duplicate characters and their counts
    for char, count in char_count.items():
        if count > 1:
            print(char, count)
            found_duplicates = True
    
    # If no duplicates are found, print -1
    if not found_duplicates:
        print("-1")

# Take input from the user
input_string = input()

# Call the function to print duplicates
print_duplicates(input_string)'''
