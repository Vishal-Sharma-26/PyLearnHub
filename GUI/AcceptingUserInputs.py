from tkinter import *

from sqlalchemy import column

root = Tk()
root.geometry("600x400")
root.title("My Travels")

# Creating getvals function to store values entered by user in records.text file
def getvals():
    print("Thanks for submitting form!")

    with open("records.txt", "a") as f:
        f.write(f"The name of the person is {name_value.get()}, | the phone number is {phone_value.get()}, | the email address is {email_value.get()}, | the gender is {gender_value.get()}, | the payment mode is {payment_mode_value.get()}, | and the food services are {food_services_value.get()}\n")



# Creating a label widget
Label(root, text="Welcome to My Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

# Creating a button widget
name = Label(root, text="Name")
phone = Label(root, text="Phone")
email = Label(root, text="Email")
gender = Label(root, text="Gender")
payment_mode = Label(root, text="Payment Mode")

# Pack is used to show the widgets on screen
name.grid(row= 1, column=2)
phone.grid(row= 2, column=2)
email.grid(row= 3, column=2)
gender.grid(row= 4, column=2)
payment_mode.grid(row= 5, column=2)

# Variable classes in tkinter
name_value = StringVar()    # This is a string type variable class
phone_value = StringVar()
email_value = StringVar()
gender_value = StringVar()
payment_mode_value = StringVar()
food_services_value = IntVar()   # This is an integer type variable class

# Creating entry field widgets
name_entry = Entry(root, textvariable=name_value)
phone_entry = Entry(root, textvariable=phone_value)
email_entry = Entry(root, textvariable=email_value)
gender_entry = Entry(root, textvariable=gender_value)
payment_mode_entry = Entry(root, textvariable=payment_mode_value)

# Packing the entries
name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
email_entry.grid(row=3, column=3)
gender_entry.grid(row=4, column=3)
payment_mode_entry.grid(row=5, column=3)

# Checkbox and Radio Button
food_service = Checkbutton(text="Want to prebook your meals?", variable=food_services_value)   # The value of the checkbox is stored in the variable food_services_value which is an integer. If the checkbox is checked then the value will be 1 else 0 respectively
food_service.grid(row=6, column=3)

# Submit button
Button(text="Submit", command=getvals).grid(row=7, column=3)     # Lambda function is used to pass arguments to function without calling it.


root.mainloop()