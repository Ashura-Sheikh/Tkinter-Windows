from tkinter import *

main_window = Tk()
main_window.title("Employee Entry")
main_window.geometry("500x500")
main_window.configure(background='black')
#test
label_info = Label(main_window, text="Update the fields above", fg="white", bg="green").grid(row=6, columnspan=5)


frame_name = Frame(main_window)
frame_address = Frame(main_window)

label_first = Label(frame_name, text="First Name: ")
label_middle = Label(frame_name, text="Middle Name: ")
label_surname = Label(frame_name, text="Surname: ")

label_staff_number = Label(frame_address, text="Staff-Number")
label_location = Label(frame_address, text="Location")
label_query = Label(frame_address, text="Query")

entry_first = Entry(frame_name)
entry_middle = Entry(frame_name)
entry_surname = Entry(frame_name)

entry_staff_number = Entry(frame_address)
entry_location = Entry(frame_address)
entry_query = Entry(frame_address)

button_submit_name = Button(frame_name, text="     Submit    ", fg="white", bg="green")
button_submit_address = Button(frame_address, text="     Submit      ", fg="white", bg="green")


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
