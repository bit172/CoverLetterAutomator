from tkinter import *
from tkinter import messagebox
from doc_manipulator import *
from datetime import datetime


def center(toplevel):
    toplevel.update_idletasks()

    # Tkinter way to find the screen resolution
    screen_width = toplevel.winfo_screenwidth()
    screen_height = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width / 2 - size[0] / 2
    y = screen_height / 2 - size[1] / 2

    toplevel.geometry("+%d+%d" % (x, y))


def generate_letter():
    if name_text.get() == '' \
            or company_text.get() == '' \
            or address_text.get() == '' \
            or city_postal_text.get() == '' \
            or subject_text.get() == '' \
            or position_title_text.get() == '' \
            or gender_text.get() == '' \
            or fileName_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    letter = DocManipulator("Cover Letter.docx")
    new_info = {
        "date": datetime.today().strftime('%B %d, %Y'),
        "name": name_text.get(),
        "company": company_text.get(),
        "address": address_text.get(),
        "city_postal": city_postal_text.get(),
        "subject": subject_text.get(),
        "position_title": position_title_text.get(),
        "gender": gender_text.get(),
        "fileName": fileName_text.get()
    }
    try:
        letter.replace_info(new_info)
        messagebox.showinfo("Cover Letter Generated", "Your Cover Letter has been successfully generated.")
    except Exception:
        messagebox.showerror('Error', 'Error while generating cover letter. Please check your fields.')
        pass


root = Tk()
root.geometry("350x360")
root.title("Cover Letter Automator")
root.resizable(False, False)
center(root)

# Name
name_text = StringVar()
name_label = Label(root, text='Name', padx=20, pady=10)
name_label.grid(row=0, column=0, sticky=W)
name_entry = Entry(root, textvariable=name_text, width=35)
name_entry.grid(row=0, column=1, columnspan=3)

# Company
company_text = StringVar()
company_label = Label(root, text='Company', padx=20, pady=10)
company_label.grid(row=1, column=0, sticky=W)
company_entry = Entry(root, textvariable=company_text, width=35)
company_entry.grid(row=1, column=1, columnspan=3)

# Address
address_text = StringVar()
address_label = Label(root, text='Address', padx=20, pady=10)
address_label.grid(row=2, column=0, sticky=W)
address_entry = Entry(root, textvariable=address_text, width=35)
address_entry.grid(row=2, column=1, columnspan=3)

# City Postal
city_postal_text = StringVar()
city_postal_label = Label(root, text='City Postal', padx=20, pady=10)
city_postal_label.grid(row=3, column=0, sticky=W)
city_postal_entry = Entry(root, textvariable=city_postal_text, width=35)
city_postal_entry.grid(row=3, column=1, columnspan=3)

# Subject
subject_text = StringVar()
subject_label = Label(root, text='Subject', padx=20, pady=10)
subject_label.grid(row=4, column=0, sticky=W)
subject_entry = Entry(root, textvariable=subject_text, width=35)
subject_entry.grid(row=4, column=1, columnspan=3)

# Position Title
position_title_text = StringVar()
position_title_label = Label(root, text='Position Title', padx=20, pady=10)
position_title_label.grid(row=5, column=0, sticky=W)
position_title_entry = Entry(root, textvariable=position_title_text, width=35)
position_title_entry.grid(row=5, column=1, columnspan=3)

# Gender
gender_text = StringVar(value="Mr.")
gender_label = Label(root, text='Gender', padx=20, pady=10)
gender_label.grid(row=6, column=0, sticky=W)
gender_radio1 = Radiobutton(root, text="Mr.", variable=gender_text, value="Mr.")
gender_radio2 = Radiobutton(root, text="Ms.", variable=gender_text, value="Ms.")
gender_radio1.grid(row=6, column=1, sticky=W)
gender_radio2.grid(row=6, column=2, sticky=W)

# File Name
fileName_text = StringVar()
fileName_label = Label(root, text='File Name', padx=20, pady=10)
fileName_label.grid(row=7, column=0, sticky=W)
fileName_entry = Entry(root, textvariable=fileName_text, width=35)
fileName_entry.insert(0, "Cover Letter1.docx")
fileName_entry.grid(row=7, column=1, columnspan=3)

# Generate Button
generate_button = Button(root, text='Generate', command=generate_letter, padx=10, pady=5)
generate_button.grid(row=8, column=2, sticky=E)

# Quit Button
quit_button = Button(root, text='Quit', command=root.quit, padx=10, pady=5)
quit_button.grid(row=8, column=3)

# Start Program
root.mainloop()
