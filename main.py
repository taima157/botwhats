import bot
from tkinter import *

def viewContacts():
  def removeSpecificContact():
    if len(bot.contacts) != 0:
      bot.removeSpecificContact(listContacts.get(ACTIVE))
      updateListContacts()
    else:
      contactsModal.destroy()

  def removeAllContacts():
    if len(bot.contacts) != 0:
      bot.removeAllContacts()
      updateListContacts()
      contactsModal.destroy()
    else:
      contactsModal.destroy()

  def updateListContacts():
    listContacts.delete(0, "end")
    for contact in bot.contacts:
      listContacts.insert(END, contact)

  if len(bot.contacts) != 0:

    contactsModal = Toplevel(mainWindow)
    contactsModal.title("Bot WhatsApp")
    contactsModal.configure(bg="gray10")
    contactsModal.focus_set()
    contactsModal.grab_set()

    width = 400
    height = 500

    sreen_width = contactsModal.winfo_screenwidth()
    sreen_height = contactsModal.winfo_screenheight()

    posix = sreen_width / 2 - width / 2
    posiy = sreen_height / 2 - height / 2

    contactsModal.geometry(f"{width}x{height}+{int(posix)}+{int(posiy)}")
    contactsModal.resizable(width=False, height=False)

    titleModalContacts = Label(contactsModal, text="LISTA DE CONTATOS/GRUPOS")
    titleModalContacts.pack()
    titleModalContacts.configure(font=("Poppins", 25, "bold"), bg="gray10", fg="green3")

    subTitleModalContacts = Label(contactsModal, text="Selecione o contato que deseja remover:")
    subTitleModalContacts.place(x=10, y=50)
    subTitleModalContacts.configure(font=("Poppins", 16, "bold"), bg="gray10", fg="#eee")

    listContacts = Listbox(contactsModal)

    updateListContacts()

    listContacts.place(x=12, y=90)
    listContacts.configure(bg="grey5", fg="grey", width=34, height=15, font=("Poppins", 16, "bold"), selectbackground="green4", highlightcolor="#fff", border=0, borderwidth=0, bd=0)

    buttonRemoveSpecific = Button(contactsModal, text="Remover selecionado")
    buttonRemoveSpecific.place(x=15, y=440, width=170, height=35)
    buttonRemoveSpecific.configure(font=("Poppins", 16), bg="gray10", command=removeSpecificContact, border="0", borderwidth="0")

    buttonRemoveAll = Button(contactsModal, text="Remover todos")
    buttonRemoveAll.place(x=215, y=440, width=170, height=35)
    buttonRemoveAll.configure(font=("Poppins", 16), bg="gray10", command=removeAllContacts, border="0", borderwidth="0")

  else:
    print("Não há nenhum contato adicionado!")

def addContact():
  bot.addContact(inputContact.get())
  inputContact.delete(0, 'end')




mainWindow = Tk()
mainWindow.title("Bot WhatsApp")
mainWindow.configure(bg="gray10")

width = 1080
height = 720

sreen_width = mainWindow.winfo_screenwidth()
sreen_height = mainWindow.winfo_screenheight()

posix = sreen_width / 2 - width / 2
posiy = sreen_height / 2 - height / 2

mainWindow.geometry(f"{width}x{height}+{int(posix)}+{int(posiy)}")
mainWindow.resizable(width=False, height=False)

title = Label(mainWindow, text="BOT WHATSAPP")
title.place(x=10, y=10)
title.configure(font=("Poppins", 40, "bold"), bg="gray10", fg="green3")

labelContact = Label(mainWindow, text="Informe o nome do contato ou grupo:")
labelContact.place(x=10, y=100)
labelContact.configure(font=("Poppins", 16, "bold"), bg="gray10", fg="#dee")

inputContact = Entry(mainWindow)
inputContact.place(x=10, y=135, width=290, height=35)
inputContact.configure(font=("Poppins", 16), bd=0)

buttonContact = Button(mainWindow, text="Adicionar")
buttonContact.place(x=325, y=137, height=30)
buttonContact.configure(font=("Poppins", 16), bg="gray10", command=addContact, border="0", borderwidth="0")

buttonViewContacts = Button(mainWindow, text="Ver contatos adicionados")
buttonViewContacts.place(x=850, y=137, height=30)
buttonViewContacts.configure(font=("Poppins", 16), bg="gray10", command=viewContacts, border="0", borderwidth="0")

mainWindow.mainloop()
