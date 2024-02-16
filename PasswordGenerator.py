import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
no_of_letters= int(input("How many letters would you like in your password?\n")) 

no_of_symbols = int(input(f"How many symbols would you like?\n"))

no_of_num = int(input(f"How many numbers would you like?\n"))

my_password1 =''
ran_letters = random.choices(letters, k=no_of_letters)
for l in ran_letters:
   my_password1 += l

my_password2 =''
ran_symbols = random.choices(symbols, k=no_of_symbols)
for s in ran_symbols:
    my_password2 += s

my_password3 = ''
ran_numbers = random.choices(numbers, k=no_of_num)
for n in ran_numbers:
    my_password3 += n

my_password = my_password1+my_password2+my_password3
my_pwd_list = list(my_password)
random.shuffle(my_pwd_list)
shuffled_password = ''.join(my_pwd_list)
print(f"Here is your password: {shuffled_password}")