def count_vowels(str):
    vowels="aeiouAEIOU"
    count=0
    for char in input_string:
        if char in vowels:
            count+=1
    return count
input_string=input("Enter a String")

print(f"Number of Vowel in the given string:{input_string}",count_vowels(input_string))



    