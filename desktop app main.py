from tkinter import *
from tkinter import ttk
import pymysql

class Emp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("800x600+310+100")
        self.root.resizable(False, False)
        self.root.config(bg="silver")

        # Title Label
        title = Label(self.root, text="Employee Management System", font=("monospace", 20, "bold"), bg="#7f2ce3")
        title.pack(fill=X)

        # Details Frame
        Details_frame = Frame(self.root)
        Details_frame.place(x=1, y=38, width=800, height=520)

        # Scrollbars
        scroll_x = Scrollbar(Details_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Details_frame, orient=VERTICAL)

        # Employee Table
        self.emp_table = ttk.Treeview(Details_frame, columns=("username", "work", "phone", "country", "gender"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.emp_table.place(x=18, y=1, width=760, height=498)

        # Configure Scrollbars
        scroll_x.config(command=self.emp_table.xview)
        scroll_y.config(command=self.emp_table.yview)

        # Pack Scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Add columns to the Treeview table
        self.emp_table['show'] = 'headings'
        self.emp_table.heading('username', text='Username')
        self.emp_table.heading('work', text='Work')
        self.emp_table.heading('phone', text='Phone')
        self.emp_table.heading('country', text='Country')
        self.emp_table.heading('gender', text='Gender')

        # Set column width for better visualization
        self.emp_table.column('username', width=100)
        self.emp_table.column('work', width=100)
        self.emp_table.column('phone', width=100)
        self.emp_table.column('country', width=100)
        self.emp_table.column('gender', width=100)

        # self.dell = StringVar()
        # Ent1 = Entry(root,width = 25, textvariable=self.dell)
        # Ent1.place(x=140, y=560)
        
        btn1 = Button(root, text="Delete Emp",bg="#FF6B6B", font=("monospace", 12, "bold"),command=self.delete, relief=FLAT, bd = 0)
        btn1.place(x=95, y=565)

        btn2 = Button(root, text="refresh",bg="#4CAF50", font=("monospace", 12, "bold"), command=self.update, relief=FLAT, bd = 0)
        btn2.place(x=250, y=565)

        btn3 = Button(root, text="edit",bg="#FFD54F", font=("monospace", 12, "bold"), command=self.edit_window, relief=FLAT, bd = 0)
        btn3.place(x=405, y=565)

        btn4 = Button(root, text="Exit",bg="#FF4C4C", font=("monospace", 12, "bold"), command=self.exit_window, relief=FLAT, bd = 0)
        btn4.place(x=650, y=565)

        self.fetch_data()

    
    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="kevo")
        cur = con.cursor()
        cur.execute("select * from users")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.emp_table.delete(*self.emp_table.get_children())
            for row in rows:
                self.emp_table.insert('', END, values=row)
            con.commit()
        con.close()

    def delete(self):
        cur_item = self.emp_table.focus()
        con = pymysql.connect(host="localhost", user="root", password="", database="kevo")
        cur = con.cursor()
        if cur_item:
            cur.execute("delete from users where username = %s", (self.emp_table.item(cur_item)['values'][0],))
        else:
            self.dell.set("")
        con.commit()
        self.fetch_data()
        con.close()

    def edit_window(self):
        self.edit_root = Toplevel(self.root)
        self.edit_root.title("Edit Employee")
        self.edit_root.geometry("400x250+310+100")
        self.edit_root.resizable(False, False)
        self.edit_root.config(bg="silver")

        self.edit_username = StringVar()
        self.edit_work = StringVar()
        self.edit_phone = StringVar()
        self.edit_country = StringVar()
        self.edit_gender = StringVar()

        Label(self.edit_root, text="Username", font=("monospace", 10, "bold"), bg="silver").place(x=10, y=10)
        Ent1 = Entry(self.edit_root, width=25, textvariable=self.edit_username)
        Ent1.place(x=150, y=10)

        Label(self.edit_root, text="Work", font=("monospace", 10, "bold"), bg="silver").place(x=10, y=50)
        Ent2 = Entry(self.edit_root, width=25, textvariable=self.edit_work)
        Ent2.place(x=150, y=50)

        Label(self.edit_root, text="Phone", font=("monospace", 10, "bold"), bg="silver").place(x=10, y=90)
        Ent3 = Entry(self.edit_root, width=25, textvariable=self.edit_phone)
        Ent3.place(x=150, y=90)

        Label(self.edit_root, text="Country", font=("monospace", 10, "bold"), bg="silver").place(x=10, y=130)
        Ent4 = Entry(self.edit_root, width=25, textvariable=self.edit_country)
        Ent4.place(x=150, y=130)

        Label(self.edit_root, text="Gender", font=("monospace", 10, "bold"), bg="silver").place(x=10, y=170)
        Ent5 = Entry(self.edit_root, width=25, textvariable=self.edit_gender)
        Ent5.place(x=150, y=170)

        btn = Button(self.edit_root, text="Edit", command=self.edit,bg="#FFD54F", font=("monospace", 12, "bold"), relief=FLAT, bd = 0)
        btn.place(x=180, y=210)

        self.edit_root.mainloop()

    def edit(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="kevo")
        cur = con.cursor()
        cur.execute("update users set work = %s, phone = %s, country = %s, gender = %s where username = %s"
                    , (self.edit_work.get(), self.edit_phone.get(), self.edit_country.get(),
                       self.edit_gender.get(), self.edit_username.get()))
        con.commit()
        self.fetch_data()
        con.close()
        self.edit_root.destroy()

    def update(self):
        self.fetch_data()

    def exit_window(self):
        self.root.destroy()

root = Tk()
ob = Emp(root)
root.mainloop()


