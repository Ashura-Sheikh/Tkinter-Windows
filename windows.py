from tkinter import *

main_window = Tk()
main_window.geometry("500x500")
#test 
label_info = Label(main_window, text="Update the fields above").grid(row=6, columnspan=5)


frame_name = Frame(main_window)
frame_address = Frame(main_window)

label_first = Label(frame_name, text="First Name: ")
label_middle = Label(frame_name, text="Middle Name: ")
label_surname = Label(frame_name, text="Surname: ")

label_first_line = Label(frame_address, text="First Line")
label_town = Label(frame_address, text="Town")
label_county = Label(frame_address, text="County")

entry_first = Entry(frame_name)
entry_middle = Entry(frame_name)
entry_surname = Entry(frame_name)

entry_first_line = Entry(frame_address)
entry_town = Entry(frame_address)
entry_county = Entry(frame_address)

button_submit_name = Button(frame_name, text="     Submit    ")
button_submit_address = Button(frame_address, text="     Submit      ")


label_first.grid(row=0, column=0)
label_middle.grid(row=1, column=0)
label_surname.grid(row=2, column=0)

label_first_line.grid(row=0, column=0)
label_town.grid(row=1, column=0)
label_county.grid(row=2, column=0)


entry_first.grid(row=0, column=1)
entry_middle.grid(row=1, column=1)
entry_surname.grid(row=2, column=1)


entry_first_line.grid(row=0, column=1)
entry_town.grid(row=1, column=1)
entry_county.grid(row=2, column=1)


button_submit_name.grid(row=3, columnspan=2)
button_submit_address.grid(row=3, columnspan=2)

frame_name.grid(row=0, column=0)
frame_address.grid(row=0,column=1)


main_window.mainloop()
