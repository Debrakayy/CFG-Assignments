#code a new random Password Generator
#Description: Create a script that generates random secure passwords based on user preferences (e.g., length, inclusion of special characters).
#Key Concepts:
#String manipulation
#Random module
#Loops
#Enhancements:
#Include options to save generated passwords to a file.
#Importing relevant modules


import random # needed to generate the random passwords
from os import write
import requests #new module installed to be able to get the API

endpoint = 'https://passwordwolf.com/api/' #imported password API to review strenght and lenght of the password
response = requests.get(endpoint)
data = response.json()
print ("API Reponse:",data) #print data from API
password_data =data[0]['password']
password_length = len(password_data) # only using the first password for the length

#extracts all the special characters from the API
password_list =[]
for entry in data:
    password_list.append(entry['password'])

#constraints for password
Rand_char = "!@#$%^&*()_+[]{}|;:,.?/<>"
Ran_number = list("0123456789") # Creates a list of individual digit strings

API_special_character= set()# Extract special characters from all API-generated passwords
for password in password_list :
    for symbol in password :

        if symbol in Rand_char :
            API_special_character.add(symbol)

print(API_special_character)


if not API_special_character:
    API_special_character = set(Rand_char)

def new_password(password):

    #check if password contains uppercase, lowercase, at least one special character and length as long as the API
    if (any(letter.isupper() for letter in password) and
            any(letter.islower() for letter in password) and
            any(symbol in API_special_character for symbol in password) and
            any(number in Ran_number for number in password) and
            len(password) >= password_length):
        return 'Valid Password'
    else:
        return 'Weak Password'

#generate random passwords
Amount = 5
#list to store the generated passwords
Generated_Password =[]

for output in range(Amount) :
    password= ''.join(random.choices(password_list, k=1)) #creates 5 random passwords but picks 1 for the password by converting a list to a string
    password = password[:14]  # splicing to 14 to prevent the use of a very long password
Generated_Password.append(password)

print("Generated Password:", password, "output:", new_password(password))#calls the functions and stores the result


file=open('/Users/debrakamanya/Desktop/cfg_python/CFG-Assignments/Assignment2/final_results.txt' ,'w')

content = file.write('I have generated a code which helps a user to select a strong password\n' 
"using the API,this provided length and special key constraints\n"
'the password also need to contain uppercase lowercase, and numbers to ensure security\n'
'splicing was also used to ensure the password was not too long\n'
'the code will selecta password till a valid answer was achieved.\n ')
All_results= file.write (f"Generated Password: {password} \n")

print(content)
