import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import csv
import collections


# -- lists
f1 = []
f2 = []
f3 = []
f2l = []

def askxfile():
    xfile.set(filedialog.askopenfilename())

def askyfile():
    yfile.set(filedialog.askopenfilename())

def create_new_file():
    files = [('csv', '*.csv')]
    file = filedialog.asksaveasfile(filetypes=files, defaultextension=files)


def compare_csv():
    with open(xfile.get(), 'r') as t1, open(yfile.get(), 'r') as t2:
        fileone = csv.reader(t1)
        filetwo = csv.reader(t2)


        for i in fileone:
                r = i[xfilec.get()]
                #f1.append(int(r))
                f1.append(r)

        for c in filetwo:
                t = c[yfilec.get()]
                #f2.append(int(t))
                f2.append(t)


        for x in f2:
            if x not in f1:
                f3.append(x)

        print("First File: ")
        print(f1)
        print(len(f1))
        print("Second File: ")
        print(f2)
        print(len(f2))
        print("Duplicates: ")
        print(( len(set(f1) & set(f2))-1))
        print("Uniques: ")
        print(f3)
        MsgBox = tk.messagebox.askquestion('Check Point', 'File 1 values: '+ str(len(f1)) + '\nFile 2 value: ' + str(len(f2)) + '\nDuplicates: ' + str(len(set(f1) & set(f2))) + '\nUniques: ' + str(len(f3)),
                                           icon='info')
        if MsgBox == 'yes':
            uniques()
        else:
            tk.messagebox.showinfo('Return', 'You will now return to the application screen')


def uniques():

    with open(yfile.get(), 'r') as t3, open('output.csv', 'w', newline='') as t4:
        filewriter = csv.writer(t4)
        filetree = csv.reader(t3)
        for j in filetree:
            f2l.append(j)
        filewriter.writerow(f2l[0])

        for o in f3:
            for k in f2l:
                if k[yfilec.get()] == str(o) and k[yfilec.get()] is not None:
                    filewriter.writerow(k)
    tk.messagebox.showinfo("Success!", "Duplicates found: " + str(len(set(f1) & set(f2))-1) + "\nUnique values: " + str(len(f3)))

#---------colors
mblack = "#080808"
mwhite = "#F8F8F8"
mgray ="#696969"
#---------Window

root = tk.Tk()
root.geometry("700x250")
root.title("CSV Duplicate Checker")
root.configure(bg=mblack)
root.attributes("-alpha",0.95)


#--- CSV File1
xfile = tk.StringVar()
xfile_lbl = tk.Label(root, text="File 1 Location", bg=mblack, fg=mwhite, font=("Caladea", 10, "bold"))
xfile_lbl.place(x=80, y=50)
xfile_inp = tk.Entry(root, textvariable=xfile, width=35, bg=mgray)
xfile_inp.place(x=200, y=50)

xfile_btn = tk.Button(root, text="Browse", bg=mblack, fg=mwhite, font=("Caladea", 10, "bold"), width=9, command=askxfile)
xfile_btn.place(x=420,y=48)


xfilec_lbl = tk.Label(root, text="Column", bg=mblack, fg=mwhite, font=("Caladea", 10, "bold"))
xfilec_lbl.place(x=510, y=50)
xfilec = tk.IntVar()
xfilec_inp = tk.Entry(root, textvariable=xfilec, width=5, bg=mgray)
xfilec_inp.place(x=570, y=50)

#--- CSV File2
yfile = tk.StringVar()
yfile_lbl = tk.Label(root, text="File 2 Location", bg=mblack, fg=mwhite, font=("Caladea", 10, "bold"))
yfile_lbl.place(x=80, y=90)
yfile_inp = tk.Entry(root, textvariable=yfile, width=35, bg=mgray)
yfile_inp.place(x=200, y=90)


yfile_btn = tk.Button(root, text="Browse", bg=mblack, fg=mwhite, font=("Caladea", 10, "bold"), width=9, command=askyfile)
yfile_btn.place(x=420,y=88)

yfilec_lbl = tk.Label(root, text="Column", bg=mblack, fg=mwhite, font=("Caladea", 10, "bold"))
yfilec_lbl.place(x=510, y=90)
yfilec = tk.IntVar()
yfilec_inp = tk.Entry(root, textvariable=yfilec, width=5, bg=mgray)
yfilec_inp.place(x=570, y=90)




#--- Operating buttons
compare_btn= tk.Button(root, text="Compare", bg=mblack, fg=mwhite, font=("Caladea", 10, "bold"), width=12, height=2, command=compare_csv)
compare_btn.place(x=80,y=150)


#--- Text files

root.mainloop()