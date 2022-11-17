import socket
from threading import Thread
from tkinter import *

class GUI :
  def __init__ (self) :
    self.Window = Tk()
    self.Window.withdraw()

    self.loginscreen = Toplevel()
    self.loginscreen.title("Login")
    self.loginscreen.resizable(width = False, height = False)
    self.loginscreen.configure(width = 400, height = 300)

    self.title = Label(self.loginscreen, text = "Please Login", justify = CENTER, font = "Calibri 16 bold")
    self.title.place(relheight = 0.15, relx = 0.2, rely = 0.07)
    
    self.input = Entry(self.loginscreen, font = "Calibri 12")
    self.input.place(relwidth = 0.4, relheight = 0.12, relx = 0.35, rely = 0.2)
    self.input.focus()

    self.nickname = Button(self.loginscreen, text = "Continue", font = "Calibri 12", command = lamda: self.goahead(self.title.get()))
    self.nickname.place(relx = 0.4, rely = 0.55)

    self.Window.mainloop()
  
  def layout(self,name):		
    self.name = name
    self.Window.deiconify()
    self.Window.title("CHATROOM")
    self.Window.resizable(width = False, height = False)
    self.Window.configure(width = 470, height = 550, bg = "#17202A")
    self.labelHead = Label(self.Window,
      bg = "#17202A",
      fg = "#EAECEE",
      text = self.name,
      font = "Helvetica 13 bold",
      pady = 5)
    
    self.labelHead.place(relwidth = 1)

    self.labelBottom = Label(self.Window,
      bg = "#ABB2B9",
      height = 80)

    self.labelBottom.place(
      relwidth = 1,
      rely = 0.825)

    self.line = Label(self.Window,
      width = 450,
      bg = "#ABB2B9")
    
    self.line.place(relwidth = 1,
      rely = 0.07,
      relheight = 0.012)
    
    self.entryLabel = Entry(self.labelBottom,
      bg = "#2C3E50",
      fg = "#EAECEE",
      font = "Helvetica 13")

    self.entryLabel.place(
      relwidth = 0.74,
      relheight = 0.06,
      rely = 0.008,
      relx = 0.001)
    
    self.entryLabel.focus()
    
    self.textCons = Text(self.Window,
      width = 20,
      height = 2,
      bg = "#17202A",
      fg = "#EAECEE",
      font = "Helvetica 14",
      padx = 5,
      pady = 5)
    
    self.textCons.place(
      relheight = 0.745,
      relwidth = 1,
      rely = 0.08)
    
    self.button = Button(self.labelBottom,
      text = "send",
      font = "Helvetica 10 bold",
      width = 20,
      bg = "#ABB2B9",
      command = lambda: self.sendButton(self.entryMsg.get()))
    
    self.button.place(
      relx = 0.07,
      rely = 0.008,
      relheight = 0.06,
      relwidth = 0.022)

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

def receive() :
  while True:
    try:
      message = client.recv(2048).decode('utf-8')
      if message == 'NICKNAME':
        client.send(nickname.encode('utf-8'))
      else:
        self.show_message(message)
    except:
      print("An error occured!")
      client.close()
      break

def write() :
  while True:
    message = input('')
    client.send(message.encode('utf-8'))
    self.show_message(message)

receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()

def goahead (self, name) :
  self.loginscreen.destroy()
  self.name = name
  self.entryMsg.delete(0, END)
  thread = Thread(target = self.receive)
  thread.start()

def sendButton (self, message) :
  self.textCons.config(state = DISABLED)
  self.message = message
  self.entryMsg.delete(0, END)
  send = Thread(target = self.write)
  send.start()

def show_message () :
  self.textCons.config(state = NORMAL)
  self.textCons.insert(END, message + "\n\n")
  self.textCons.config(state = DISABLED)
  self.textCons.see(END)