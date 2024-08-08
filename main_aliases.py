import text_utils as tu

my_string = input("Please import the text that you would like changed:")
choice=input("What would you like to do? [1]Reverse the text. [2]Capitalize the text?")
if choice == "1":
    print(tu.reverse_string(my_string))
elif choice =="2":
    print(tu.capitalize_string(my_string))
else:
    print("Not a valid choice/option.")