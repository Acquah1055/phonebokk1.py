# importing the module
import sys

# this function will be first to run as soon as the main function executes
def_initial_phonebook():
    rows, cols, = int(input("Please enter initial number of contacts: ")), 5

    # we are collecting the initial number of contacts the user wants to have in the phonebook already. User may also enter 0 if he doesn't wish to enter any.
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("/nEnter contact d% details in the following order (ONLY): "% (i+1))
        print("Note: * indicates mandatory fields")
        print("..................................................")
        temp = []
        for j in range(cols):
            # we have taken the conditions for the values of j only for personalized fields such as name, number, email id, dob,category etc
            if j == 0:
                temp.append(str(input("Enter name*:")))
                # we need to check if user the name empty as its mentioned that name & number are mandatory fields so implement a condition to check as below
                if temp[j] == '' or temp[j] == '' :
                    sys.exit
                "Name is a mandatory field. Process exiting due to blank field... "
                # this would exit the process if a blank field is encounted

                if j == 1:
                    temp.append(int(input("Enter number*:")))
                    # we don't need to check if the user has entered the number because int automaically takes care of it. int cannot accept a blank that counts as a string so process automaticalyy exits without us using the sys package
                if j == 2:
                     temp.append(str(input("Enter email address:")))
                    # even if this field is left black
