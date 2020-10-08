from tkinter import *

main_window = Tk()
main_window.title("Employee Entry")
main_window.geometry("500x500")
main_window.configure(background='black')
#test

def submit_1():
    print("active call back")

def submit_2():
    print("active call back 2 ")

label_info = Label(main_window, text="Update the fields above", fg="green", bg="black").grid(row=6, columnspan=5, padx=10, pady=10)


frame_name = Frame(main_window)
frame_address = Frame(main_window)

#Define Functions for submit buttons/ side

label_first = Label(frame_name, text="First Name: ", padx=10, pady=10)
label_middle = Label(frame_name, text="Middle Name: ", padx=10, pady=10)
label_surname = Label(frame_name, text="Surname: ", padx=10, pady=10)

label_staff_number = Label(frame_address, text="Staff-Number", padx=10, pady=10)
label_location = Label(frame_address, text="Location", padx=10, pady=10)
label_query = Label(frame_address, text="Query", padx=10, pady=10)

entry_first = Entry(frame_name)
entry_middle = Entry(frame_name)
entry_surname = Entry(frame_name)

entry_staff_number = Entry(frame_address)
entry_location = Entry(frame_address)
entry_query = Entry(frame_address)

button_submit_name = Button(frame_name, text="     Submit    ", command=submit_1, padx=10, pady=10)
button_submit_address = Button(frame_address, text="     Submit      ", command=submit_2, padx=10, pady=10)


label_first.grid(row=0, column=0)
label_middle.grid(row=1, column=0)
label_surname.grid(row=2, column=0)

label_staff_number.grid(row=0, column=0)
label_location.grid(row=1, column=0)
label_query.grid(row=2, column=0)


entry_first.grid(row=0, column=1)
entry_middle.grid(row=1, column=1)
entry_surname.grid(row=2, column=1)


entry_staff_number.grid(row=0, column=1)
entry_location.grid(row=1, column=1)
entry_query.grid(row=2, column=1)


button_submit_name.grid(row=3, columnspan=2)
button_submit_address.grid(row=3, columnspan=2)

frame_name.grid(row=0, column=0)
frame_address.grid(row=0,column=1)


main_window.mainloop()
