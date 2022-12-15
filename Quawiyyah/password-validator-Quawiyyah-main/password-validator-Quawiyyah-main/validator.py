special_characters = ['&', '#', '$', '!', '?', '"', '(', ')', '.']

alphabetic_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
                                                                                                                          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Define fixed values here
min_length = 9
max_length =12
min_special_character =3
min_alphabetic_character=5

# Write your code here
print("Please enter a password with the following criteria:")
print("Length of password must be between 9 and 12 characters")
print("Password must contain at least 3 special characters")
print("Password must also contain at least 5 alphabetic characters")

special_character_counter=0
alphabetic_character_counter=0
user_password=input("Enter your password")
if len(user_password) >= min_length and len(user_password) <=max_length :
    print("Checking password....")
    for character in user_password:
        if character in special_characters:
            special_character_counter+=1
    print("There are", special_character_counter,"special characters")
    for character in user_password:
        if character in alphabetic_characters:
            alphabetic_character_counter+=1
    print("There are",alphabetic_character_counter,"alphabetic characters")
    if special_character_counter < min_special_character:
        print ("Validation failed:You need to have at least 3 special characters")       
    elif alphabetic_character_counter < min_alphabetic_character:
        print("Validation failed:You need to have at least 5 alphabetic characters")
    else:
        print("Validation succeeded")
else:
    print("Your password should be between 9 and 12 characters")


