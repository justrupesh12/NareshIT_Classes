from tkinter import *
import random # this is used to generate random characters
import string #imported the Access various character sets(uppercase, lowercase, digits, punctuation)
import pyperclip # this is used to copy the generated password to clipboard

# creating a main application  window 

root=Tk() # initializing the Tkinter window

root.title("PYTHON PROJECT  - PASSWORD GENERATOR")# setting the title of the window
root.geometry("400x400")# setting the size of the window  and correct method to write small x to seperate width and height
root.resizable(0,0) # this is used to make the window not resizable
root.config(bg="green")# setting the background color of the window

# creating a label to display the title
'''
Label(root, ...) → Creates a label inside the root window.

text="Password Generator" → Sets the label’s displayed text.

font='arial 20 bold' → Defines the font style, size (20 pixels), and makes it bold. or we can write font=("arial",20,"bold")

bg="black" → Sets the background color to black.

fg="white" → Sets the text color to white.

.pack() → Arranges the label in the window using Tkinter’s geometry manager, ensuring it appears on the interface.

.pack(pady=10) → Packs the label into the window and adds 10 pixels of vertical padding.
'''
#Label(root,text="Password Generator",font='arial 20 bold',bg="black",fg="white").pack(pady=10)
Label(root, text='PASSWORD GENERATOR', font='arial 15 bold',background="Gray").pack()
#this is used to create a label in the window with the text "PASSWORD GENERATOR" and font style 'arial 15 bold'

Label(root,text="PythonProjects",font='arial 10 bold',bg="Gray").pack(side=BOTTOM)
#this is used to create a label in the window with the text "PythonProjects" and font style 'arial 10 bold' and it will be placed at the bottom of the window

pass_label=Label(root,text="PASSWORD LENGTH",font='arial 10 bold',bg="black",fg="white").pack()
pass_len=IntVar()  # IntVar is used to store integer values
length=Spinbox(root,from_=8,to_=32,textvariable=pass_len,width=15).pack()
pass_str=StringVar()  # StringVar is used to store string values

def Generator():
    password=[]
    # this is used to generate the password
    if pass_len.get()>=4:
        password.append(random.choice(string.ascii_uppercase))  # adding a random uppercase letter
        password.append(random.choice(string.ascii_lowercase))  # adding a random lowercase letter
        password.append(random.choice(string.digits))  # adding a random digit
        password.append(random.choice(string.punctuation))  # adding a random punctuation character
        
        # filling the rest of the password with random characters
        for _ in range(pass_len.get()-4):
            password.append(random.choice(string.ascii_uppercase+string.ascii_lowercase+ string.digits + string.punctuation))
            
            # shuffling the password to make it more random
        random.shuffle(password)
        
    else:
        # if the length is less than 4, just fill the required length with random characters
        for _ in range(pass_len.get()):
            password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))
            
            
            
     #converting the list to a string
    pass_str.set("".join(password))  # joining the list to form a string
    
def Copy_password():
    # this function is used to copy the generated password to clipboard
    pyperclip.copy(pass_str.get())
    
       
Button(root,text="Generated Password",command=Generator).pack(pady=5)  # creating a button to generate the password
# this is used to create a button in the window with the text "Generate Password" and it will call the Generator function when clicked  

Entry(root,textvariable=pass_str).pack()

Button(root,text="Copy to clipboard",command=Copy_password).pack(pady=5)  # creating a button to copy the password to clipboard
# this is used to create a button in the window with the text "Copy to clipboard" and it will call the Copy_password_to_clipboard function when clicked 


root.mainloop()  # this is used to run the main loop of the Tkinter window
# this is used to run the main loop of the Tkinter window





