# importing the requests library
import requests
import sys

# importing the Tkinter GUI 
from Tkinter import *

# defining the api-endpoint 
API_ENDPOINT = "endpoint_displaytext.py"


def show_entry_fields():
   sys.stdout.write("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )

# data to be sent to api
data = {'First Name':e1,
        'Last Name': e2}
 
#sending data using POST to the endpoint
r = requests.post(url = API_ENDPOINT, data = data)