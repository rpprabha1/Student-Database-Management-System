from tkinter import *
import pymysql

window = Tk()

window.geomerty  = ('700x600')

def myButtonClick(selection):
    id = E.get()
    name = E1.get()
    address = E2.get()
    print('Student id is:', id)
    print('Student name is:', name)
    print('Student address is:', address)

    if selection in ('Insert'):
        #connect to mysql
        con = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='prabha')
        cur = con.cursor()
        '''cur.execute("select version()")
        data = cur.fetchone()
        print("The version is", data)'''

        query= '''create table if not exists student (id int,
            name varchar(20), address varchar(50), primary key(id))'''

       
        cur.execute(query)
        con.commit()
       
        InsQuery = '''INSERT INTO student \
            VALUES('%s', '%s' , '%s')'''%(id, name, address)
        try:
            cur.execute(InsQuery)
            con.commit()
            con.close()
            print("Student saved to db successfully id:", id, 'name:', name, 'address:', address)
        except:
            print("Error occured during insertion into database")
            con.rollback()
            con.close()
    elif selection in ('Update'):
        try:
            UpQuery = '''UPDATE student SET name = '%s',
                    address = '%s' where id = '%s' '''%(name, address, id)
        
            con = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='prabha')
            cur = con.cursor()
            cur.execute(UpQuery)
            con.commit()
            con.close()
            print("Student updated to db successfully id:", id, 'name:', name, 'address:', address)
        except Error as e:
            print("Error occured during updation")
            con.rollback()
            con.close()
    elif selection in ('Delete'):   
        try:
            DeQuery = '''DELETE FROM student WHERE id = '%s' '''%(id)
        
            con = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='prabha')
            cur = con.cursor()
            cur.execute(DeQuery)
            con.commit()
            con.close()
            print("Student deleted successfully")
        except Error as e:
            print("Error occured during deletion")
            con.rollback()
            con.close()
    elif selection in ('Select'):   
        try:
            SeQuery = "SELECT * FROM student WHERE id = '%s' "%(id)
        
            con = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='prabha')
            cur = con.cursor()
            cur.execute(SeQuery)
            rows = cur.fetchall()
            id1 = ''
            name1 = ''
            address1 = ''
            for row in rows:
                id1 = row[0]
                name1 = row[1]
                address1 = row[2]
            E1.delete(0, END)
            E2.delete(0, END)
            E1.insert(0, name1)
            E2.insert(0, address1)
            
            con.close()
            print("Student id:", id1, " name:", name1, " address", address1)
        except Error as e:
            print("Error occured during Selection")
            con.close()
            
#id block 
L = Label(window, text = "Enter student id:",
          font = ('arial', 30), fg = 'blue')
L.grid(row =0, column = 0)
E = Entry(window, bd = 5, width = 50)
E.grid(row = 0, column = 1)
#name block
L1 = Label(window, text = "Enter student name:",
           font=('arial', 30), fg= 'blue')
L1.grid(row = 1, column = 0)
E1 = Entry(window, width= 50, bd = 5)
E1.grid(row = 1, column = 1)
#Address block
L2 = Label(window, text = "Enter student Address:",
           font=('arial', 30), fg= 'blue')
L2.grid(row = 2, column = 0)
E2 = Entry(window, width= 50, bd = 5)
E2.grid(row = 2, column = 1)
#Insert button
BInsert = Button(text = "Insert", fg = 'black',
            bg = 'green', font = ('arial', 25,'bold'),
                 width = 30, command = lambda:myButtonClick('Insert'))
    
BInsert.grid(row =  5)
#Update button
BUpdate = Button(text = "Update", fg = 'black',
            bg = 'orange', font = ('arial',25, 'bold'),
                 width = 30, command = lambda:myButtonClick('Update'))
    
BUpdate.grid(row =  6, column = 0)
#Delete button
BUpdate = Button(text = "Delete", fg = 'black',
            bg = 'red', font = ('arial',25, 'bold'),
                 width = 30, command = lambda:myButtonClick('Delete'))
    
BUpdate.grid(row =  7, column = 0)
#Select button
BUpdate = Button(text = "Select", fg = 'black',
            bg = 'blue', font = ('arial',25, 'bold'),
                 width = 30, command = lambda:myButtonClick('Select'))
    
BUpdate.grid(row =  8, column = 0)


mainloop()















                 
