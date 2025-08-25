import tkinter as tk
#create the main Application window
root = tk.Tk()
# Set the title of the window
root.title("My Application")
# Set the size of the window
root.geometry("400x100")
#function to print"Hello World!" in the console
def say_hello():
    print('Hello World!')
    print('goodbye')
    
#create a button that triggers the say_hello function
hello_button = tk.Button(root, text="Click me", command=say_hello)
#pack the button into the window
hello_button.pack(pady=20) 
#start the tkinter event loop
root.mainloop()   