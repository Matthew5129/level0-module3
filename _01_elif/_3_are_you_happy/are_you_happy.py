from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    window = Tk()
    user = simpledialog.askstring(title="user", prompt="HELLO, MISTER! I AM THE HAPPY SCREAMING MAN! ARE YOU HAPPY?")
    if user == "Yes":
        messagebox.showinfo(title="user", message="GOOD JOB BEING A HAPPY MAN, MISTER!")
    if user == "No":
        simpledialog.askstring(title="user", prompt="DO YOU WANT TO BE HAPPY?")
    if user == "No":
        messagebox.showinfo(title="user", message="OK...NOW I'M SAD.")
    pass
