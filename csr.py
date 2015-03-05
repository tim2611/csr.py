#small python program to create an csr for a sll certificate


from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import Spinbox
from os.path import expanduser
import os, sys

program_directory=sys.path[0]

def generate_csr(*args):
    try:
        fqdn = certname.get()
        path = tkfd.get()
        os.system("xterm -e 'openssl req -new -key " + path + fqdn + ".key -out " + path + "/" + fqdn + ".csr -sha512'")
        btnGenerate.config(state='disabled')
    except ValueError:
        pass


def generate_key(*args):
    try:
        fqdn = certname.get()
        path = tkfd.get()
        if not path:
            path = home
        path = path + "/"
        bits = spbbits.get()
        tkfd.set(path)
        os.system("xterm -e openssl genrsa -out " + path + fqdn + ".key " +bits)
        btnGenerate.config(state='enabled')
    except ValueError:
        pass


def dir():
    fd = filedialog.askdirectory(title="Choose folder to save", initialdir=home)
    tkfd.set(fd)


logo = ''' \
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABGdBTUEAALGPC/xhBQAAAAlwSFlz
AAAOwwAADsMBx2+oZAAAAAd0SU1FB94DBhIHG1yt2sYAAAPzSURBVFhH7VZraNZlFB8UgRAVFISI
Zl9a34Lujb4Y+iksKwz6IhVZ0UUEISjo4i2stSIzvExd2NaUzTUvZO11iqkt5hWz6TaLbdl8R7rZ
fG173+ec3/H8z/Pf5nz/7y1fkKAf/HnOOf/n8nvOec55nhJcY5TINcb/BP7bBBB+fJlcKAomECxC
8UNCrcuEtz8rvLFMqPpe4dqHhbc+LdSySOjP/XmTKSgNuSsGqp8B/rgEvFiHlmv75U3gVbdrewvw
ibfzshJQbRmosyEcmRl5eYCTF4Sa5opObB/VTxc6tkb4r18EyUEBkyB1Ubi/Xahtg1DjE6IkhZdq
322zhRNnwpnSkZMAJ3qFah4ULNTJqu8T6oqNutfinogL+k8KBrvHuZ17fxaqe0ywSMetnarzxMM/
45E1BJwchKt5ADoJKPayGpy3D3TCxV4BrS8FrZkEWjtF28mgyjvgvp0J7o5ZvwC0601gxxzADYWW
8chKgJpegO4ctPO10KK2fe/BLb8ZruFxcMdmINGrxmFgaAD8xx7t+yrciluVyCz9dyYclRkZQ0Bd
TcIfqvtqHxHds7nXbX1GaNVk4dN7rU9g47Ntwj27heMH7CwECGLuNk0Tt2XWWFigUvBdgUgCSkxo
U5kgOEjxVrPRngXiVk8SDPd7vaNeUs1viGtZLHR0pbiD5ZLaNV/bilHCuHDa+mZDZAiot8Wn0ran
TOe+w3Cf3wA+12a6a/0I7qf3gX/Omj4GAv26Ae7Ht1RMhrbsiPQA7XtHeInu/tQWrzfOFIrN9XLH
Zt31QpMzIcgMoWSoZUcaAYtr3TTh5RMEQ/2W5271RI31cY2xUzfP05xP+M65EBHzK5FOgFNC6+4U
/upuT0YPnFt/l5f7DluM84Iurh4OlcxIPwPDf4NX3gb+5iFTub0OWoi8/Nt28Ikak4uFNA8EZVdr
u3DN/X7XnQ1aAUNZU5OOV1m/YiEiBCxcVSq8buqY2zUkoJSW2x5x+9/1HYuEyDTkxifBFdeDB3tU
cXCVU7S8Nts/t/dtS8tiIboOHKyw+s/HKr3e/Lpew9NNxvnfkfr+ebsPioHIOsADHaIe0EeG3oKB
frFP3Bc3Cmv1s/9aHd2RFSZfLSIJBIvSd88JtBhR+0az8YlqcZ9dJ9y90/TLEdQH3YyXbXT+yHgb
8rmT4E8naEpOhL4JzEYHykFVpZqq500fA4dt4Yj0wAjokF4s+qDg2keFhwfMpvXfWkMehSYXshKw
UDS9JPhAQ/H1PVqaPYliIiuBAEZixxzBDy9qLQgumHx2rX3y9E5OAgGCqXJOFyyo74BCkReBKOj5
8YuO0BvVC8NVENDdjiz6Lxb2ELkE/z5JQ/LVOu8AAAAASUVORK5CYII=
'''

root = Tk()
root.title("Create CSR")
#root.iconbitmap('@'+'Kreise.xbm')
logo1 = PhotoImage(data=logo)
root.iconphoto(True, logo1)
root.geometry('+280+250')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

certname = StringVar()
tkfd = StringVar()
home = expanduser("~")

#placing widgets on mainframe
certname_entry = ttk.Entry(mainframe, width=7, textvariable=certname)
certname_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Generate Key", command=generate_key).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="Set Dir", command=dir).grid(column=1, row=1, sticky=W)
btnGenerate = ttk.Button(mainframe, text="Generate CSR", state='disabled', command=generate_csr)
btnGenerate.grid(column=2, row=3, sticky=W)
spbbits = Spinbox(mainframe, values=(4096, 2048, 1024))
spbbits.grid(column=3, row=2, sticky=E)
ttk.Button(mainframe, text="Cancel", command=exit).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="FQDN Name:").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

certname_entry.focus()
root.bind('<Return>', generate_key)

root.mainloop()