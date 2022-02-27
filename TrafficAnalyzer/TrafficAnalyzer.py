# App's Layout
# Maybe main file

# ===== LIBRARIES
from tkinter import *
from tkinter import messagebox
import numpy as np
import time

from numpy.lib.function_base import delete



# ===== NEEDED CLASSES
from Gauss import Gauss


# ================================================== GUI LAYOUT ===========================================================

root = Tk()
root.geometry("500x700") # App dimensons
root.title("Traffic Analyzer")
root.configure(bg = 'lavenderblush3')

tops = Frame(root, width = 500, height = 50, bg = 'lavenderblush3')
tops.pack(side = TOP)

fr1 = Frame(root, width = 500, height = 100, bg = 'lavenderblush3')
fr1.pack(side = TOP, pady = (16,0))

fr2 = Frame(root, width = 500, height = 100, bg = 'lavenderblush3')
fr2.pack(side = TOP, pady = (32,0))

fr3 = Frame(root, width = 500, height = 100, bg = 'lavenderblush3')
fr3.pack(side = TOP, pady = (32,0))

# ================================================== TOP LAYOUT ===========================================================

localtime = time.asctime(time.localtime(time.time())) # Local time set up function

title = Label(tops, font = ('calibri', '12', 'bold'), text = 'Traffic Analyzer\n UNAM ENES-J\n Computacion II - Valdelamar, Palacios, Montoya, Omar', bg = 'lavenderblush3', fg = 'white')
title.grid(row = 0, column = 0, pady = (8, 0))

date = Label(tops, text = localtime, bg = 'lavenderblush3', fg = 'grey')
date.grid(row = 1, column = 0, pady = (0, 8)) # Localtime when oppening app

# ================================================ GUI FUNCTIONS ==========================================================
def Generate():
    try:
        # ==== state button set-up ===
        generate["state"] = DISABLED; save["state"] = NORMAL
        destroy["state"] = NORMAL

        # ==== global variables declaration ==
        global m; global R
        m = int(en_rZ.get()) # number of rows

        # ==== matrix 'Z': label & position
        titleZ = Label(fr3, font = ('calibri', '12', 'bold'), text = 'Traffic flow matrix', bg = 'lavenderblush3', fg = 'grey')
        titleZ.grid(row = 0, column = 0, columnspan = m + 1)

        # ==== user input => matrix Z
        R = []
        for i in range(m):
            cols = []
            for j in range(m + 1):
                entry = Entry(fr3, width = 5, justify = 'center')
                entry.grid(row = i + 1, column = j)
                cols.append(entry)
            R.append(cols)

    except:
        # ==== state button set-up
        generate['state'] = NORMAL; save['state'] = DISABLED
        destroy['state'] = DISABLED

        # ==== error message
        messagebox.showinfo(title = 'Information', message = 'Please input data correctly')


def Destroy():
    # ==== state button set-up
    save['state'] = DISABLED; destroy['state'] = DISABLED;
    delete['state'] = DISABLED; generate['state'] = NORMAL

    # ==== restore widgets in frame 1
    for widget in fr1.winfo_children():
        if isinstance(widget, Entry):
            widget.delete(0, 'end')

    # ==== fill rows & cols with 0
    en_rZ.insert(0, 0)

    # ==== restore widgets in frame 3
    for widget in fr3.winfo_children():
        widget.destroy()


def Save():
    try:
        # ==== state buttons set-up
        save['state'] = DISABLED; delete['state'] = NORMAL

        # ==== Savt to Gauss
        if (m > 0):
            calculate['state'] = NORMAL
        
        # global variables declaration
        global Z
        
        # ==== list: entriesZ => matrix Z
        entriesZ = []

        # ==== cols values to list 'entriesZ'
        for row in R:
            for col in R:
                entriesZ.append(int(col.get()))

        # ==== list 'entriesZ' => reshape to matrix Z (m x m+1)
        Z = np.array(entriesZ).reshape(m, m+1)

    except:
            
        # ==== state button set-up
        save["state"] = NORMAL; delete["state"] = DISABLED
            
        # ==== error message
        messagebox.showinfo(title = "Information", message = "Empty matrix" )

def Delete():

    # ==== state button set-up
    delete['state'] = DISABLED; save['state'] = NORMAL

    # ==== restore widgets in frame 3
    for widget in fr3.winfo_children():
        if isinstance(widget, Entry):
            widget.delete(0, 'end')


#================================================ FRAME 1 LAYOUT =========================================================

mZ = Label(fr1, font = ('calibri', '9', 'bold'), text = 'Traffic flow data-input', bg = 'lavenderblush3', fg = 'white')
mZ.grid(row = 0, column = 0, columnspan = 2, pady = 4)

rZ = Label(fr1, text = 'Intersections ', bg = 'lavenderblush3', fg = 'white')
rZ.grid(row = 1, column = 0)

en_rZ = Entry(fr1, width = 5, justify = "center", relief = SUNKEN, bd = 3)
en_rZ.grid(row = 1, column = 1)

generate = Button(fr1, text = "Generate", command = Generate, width = 8, relief = GROOVE, bg = 'lavenderblush3', fg = "#FFFFFF")
generate.grid(row = 1, column = 6, padx = (40, 0))

destroy = Button(fr1, text = "Destroy", command = Destroy, width = 8, relief = GROOVE, bg = 'violet', fg = 'white', state = DISABLED)
destroy.grid(row = 2, column = 6, padx = (40, 0), pady = (4, 0))

en_rZ.insert(0, 0); # Fills rows and cols boxes with 0
# ================================================ FRAME 2 LAYOUT =========================================================

# ==== save button
save = Button(fr2, text = 'Save', width = 12, height = 1, command = Save, relief = GROOVE, bg = 'lavenderblush3', fg = "#FFFFFF", state = DISABLED)
save.grid(row = 0, column = 0)

# ==== delete button
delete = Button(fr2, text = 'Delete', width = 12, height = 1, command = Delete, relief = GROOVE, bg = 'violet', fg = 'white', state = DISABLED)
delete.grid(row = 1, column = 0, pady = (4,0), columnspan = 2)

# ==== calculate button
calculate = Button(fr2, text = 'Calculate', width = 12, height = 1, command = Gauss, relief = GROOVE, bg = 'lavenderblush3', fg = '#FFFFFF', state = DISABLED)
delete.grid(row = 1, column = 0, pady = (4,0), columnspan = 2)



# ==========
root.mainloop()