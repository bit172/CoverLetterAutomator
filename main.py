from tkinter import *
from tkinter import ttk


def center(toplevel):
    toplevel.update_idletasks()

    # Tkinter way to find the screen resolution
    screen_width = toplevel.winfo_screenwidth()
    screen_height = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width / 2 - size[0] / 2
    y = screen_height / 2 - size[1] / 2

    toplevel.geometry("+%d+%d" % (x, y))


root = Tk()
root.geometry("450x500")
root.title("Cover Letter Automator")
center(root)

# Name
name_text = StringVar()
name_label = Label(root, text='Name', font=('bold', 12), padx=20, pady=20)
name_label.grid(row=0, column=0, sticky=W)
name_entry = Entry(root, textvariable=name_text, width=50)
name_entry.grid(row=0, column=1, columnspan=3)

# Company
company_text = StringVar()
company_label = Label(root, text='Company', font=('bold', 12), padx=20, pady=20)
company_label.grid(row=1, column=0, sticky=W)
company_entry = Entry(root, textvariable=company_text, width=50)
company_entry.grid(row=1, column=1, columnspan=3)

# Address
address_text = StringVar()
address_label = Label(root, text='Address', font=('bold', 12), padx=20, pady=20)
address_label.grid(row=2, column=0, sticky=W)
address_entry = Entry(root, textvariable=address_text, width=50)
address_entry.grid(row=2, column=1, columnspan=3)

# City Postal
cityPostal_text = StringVar()
cityPostal_label = Label(root, text='City Postal', font=('bold', 12), padx=20, pady=20)
cityPostal_label.grid(row=3, column=0, sticky=W)
cityPostal_entry = Entry(root, textvariable=cityPostal_text, width=50)
cityPostal_entry.grid(row=3, column=1, columnspan=3)

# Position Title
positionTitle_text = StringVar()
positionTitle_label = Label(root, text='Position Title', font=('bold', 12), padx=20, pady=20)
positionTitle_label.grid(row=4, column=0, sticky=W)
positionTitle_entry = Entry(root, textvariable=positionTitle_text, width=50)
positionTitle_entry.grid(row=4, column=1, columnspan=3)

# Gender
gender_text = StringVar(value="Mr.")
gender_label = Label(root, text='Gender', font=('bold', 12), padx=20, pady=20)
gender_label.grid(row=5, column=0, sticky=W)
gender_radio1 = Radiobutton(root, text="Mr.", variable=gender_text, value="Mr.")
gender_radio2 = Radiobutton(root, text="Ms.", variable=gender_text, value="Ms.")
gender_radio1.grid(row=5, column=1, sticky=W)
gender_radio2.grid(row=5, column=2, sticky=W)

# File Name
fileName_text = StringVar()
fileName_label = Label(root, text='File Name', font=('bold', 12), padx=20, pady=20)
fileName_label.grid(row=6, column=0, sticky=W)
fileName_entry = Entry(root, textvariable=fileName_text, width=50)
fileName_entry.insert(0, "Cover Letter1.docx")
fileName_entry.grid(row=6, column=1, columnspan=3)

# Generate Button
generate_button = Button(root, text='Generate', padx=10, pady=5)
generate_button.grid(row=7, column=2, sticky=E)

# Quit Button
quit_button = Button(root, text='Quit', command=root.quit, padx=10, pady=5)
quit_button.grid(row=7, column=3)

root.mainloop()
