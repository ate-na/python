# Python program to create a table

from tkinter import *

lst = [(1, 'Raj', 'Mumbai', 19),
       (2, 'Aaryan', 'Pune', 18),
       (3, 'Vaishnavi', 'Mumbai', 20),
       (4, 'Rachna', 'Mumbai', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       (5, 'Shubham', 'Delhi', 21),
       ]

total_rows = len(lst)
total_columns = len(lst[0])


root = Tk()
root.geometry("500x600")
root.title("Airline")
root.config(bg="#ddd")


main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=RIGHT, fill=BOTH, expand=1)


my_scrollbar = Scrollbar(main_frame, orient=HORIZONTAL,
                         command=my_canvas.xview)

my_scrollbar.pack(side=BOTTOM, fill=Y)


my_scrollbar2 = Scrollbar(main_frame, orient=VERTICAL,
                          command=my_canvas.yview)
my_scrollbar2.pack(side=RIGHT, fill=Y)

my_canvas.configure(xscrollcommand=my_scrollbar.set,
                    yscrollcommand=my_scrollbar2.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
    scrollregion=my_canvas.bbox("all")))

second_frame = Frame(my_canvas)

my_canvas.create_window((0, 0), window=second_frame, anchor="ne")

for i in range(total_rows):
    for j in range(total_columns):
        e = Entry(second_frame, width=10, fg='black',
                  font=('roboto', 12, 'roman'), justify="center", borderwidth=1, relief="flat", bg="#eee")
        e.grid(row=i, column=j, sticky="nw",
               padx=2, pady=2, ipadx=5, ipady=10)
        e.insert(END, lst[i][j])


root.mainloop()