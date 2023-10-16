# ames = ["Albert", "Tom", "Leonardo"]
# for name in names:

#     print(f"Greetings, {name}")
# name = "Code Academy"
# for character in name :
#     print(character)

# Create a variables containing strings for username and password.
#  Start Endless loop allowing to enter username and password. 
# If credentials are correct stop endless loop and print greeting message.

# user_name_list = []
# user_password_list = []

# print("Enter five different username and password")

# for _ in range(5):
#     username = input("Add username: ")
#     password = input("Add password: ")
#     user_name_list.append(f"username='{username}'")
#     user_password_list.append(f"password='{password}'")

# while True:
#     username_input = input("Enter username: ")
#     password_input = input("Enter password: ")

#     if f"username='{username_input}'" in user_name_list and f"password='{password_input}'" in user_password_list:
#         print("Welcome")
#         break
#     else:
#         print("Wrong password. Please try again.")


        # Leiskite naudotojui įvesti 10 sveikųjų skaičių, tada spausdinkite šių įvestų skaičių sumą ir vidurkį.

# number_list = []
# print("enter 10 integers")
# for i in range(10): 
#     user_number = int(input("add number: "))
#     number_list.append(user_number)
# sum_list = sum(number_list)
# average = sum_list / len(number_list)

# print("sum: ", sum_list)
# print("average; ", average)





# all_users = ({"username": "Povilas", "password": "ptpt"})
# username = input ("enter your username: ")
# password = input ("enter your pasword: ")
# for user in all_users:
     
#      if username == user["username"] and password == user["password"]:
#         print(f"Welcom {username}")
# else:
#         print("Your login is wrong")

# Generate a dictionary of 10 keys being 1,2,3...10 each of them should store a value of random integer number from 1 to 100.

# import random
# random_dict = {i: random.randint(1, 100) for i in range(1, 11)}
# print(random_dict)


# create a pin code cracker. 
# Let's say pin code consists of 4 random digits. 
# You can store the value in variable. 
# Then create a loop going through all possible combinations until you find the one you entered.



correct_pin = "8564"

for p in range(10):
    for o in range(10):
        for v in range(10):
            for i in range(10):
                pin = f"{p}{o}{v}{i}"
                if pin == correct_pin:
                    print(f"Correct PIN found: {pin}")
                    break  

