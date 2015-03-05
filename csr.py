#small python program to create an csr for a sll certificate


from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import Spinbox
from os.path import expanduser
import os


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


root = Tk()
root.title("Create CSR")
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