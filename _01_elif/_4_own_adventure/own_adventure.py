from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
window = Tk()
user = simpledialog.askstring(title="user", prompt="Do you want to hear some story options so I can showcase a full story?")
if user == "Yes":
    simpledialog.askstring(title="user", prompt="First option. One time there was a dumb boy named Bob. He had 0 IQ and couldn't solve the equation 1+1.")
if user == "Ok":
    messagebox.showinfo(title="user", message="Option has been added to your story!")
if user == "No":
    simpledialog.askstring(title="user", prompt="Second option. One time there lived a smart boy named Bob. He had 1000 IQ and could create Minecraft traps that no one could escape.")
