#code a new random Password Generator
#Description: Create a script that generates random secure passwords based on user preferences (e.g., length, inclusion of special characters).

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


def new_password(password):

    #check if password contains uppercase, lowercase, at least one special character and length as long as the API
    if (any(letter.isupper() for letter in password) and
            any(letter.islower() for letter in password) and
            any(symbol in Rand_char for symbol in password) and
            any(number in Ran_number for number in password) and
            len(password) >= password_length):
        return 'Valid Password'
    else:
        return 'Weak Password'

#generate random passwords
#prompt user for their choice
print('would to like to select your own password yes/no:')

choice = input('yes/no? :')
if choice == 'yes' :
    user_password= input('enter your password:')
    result = new_password(user_password)
    if result == new_password(password):
        print ('Valid Password')
    else:
        print ('Weak Password')
        print('user password :',user_password )

# generate random passwords
elif choice == 'no':
    generated_password = ''.join(random.choices(password_list[0] + Rand_char + ''.join(Ran_number), k=14))


print("Generated Password:", generated_password)


file=open('/Users/debrakamanya/Desktop/cfg_python/CFG-Assignments/Assignment2/final_results.txt' ,'w')

content = file.write('I have generated a code which helps a user to select a strong password\n' 
"using the API,this provided length and special key constraints\n"
'the password also need to contain uppercase lowercase, and numbers to ensure security\n'
'splicing was also used to ensure the password was not too long\n'
'the code will select a password till a valid answer was achieved.\n ')
All_results= file.write (f"Generated Password: {generated_password }, user password :{new_password} \n")

print(content)
