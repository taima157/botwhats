from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# teste git

contacts = []
messages = []
files = []

def addContact(contact):
  if contact != "":
    contacts.append(contact)
    print(contacts)
  else:
    print("input vazio")

def addMessage(message):
  messages.append(message)

def addFiles(midia):
  files.append(midia)

def removeSpecificContact(contact):
  contacts.remove(contact)

def removeSpecificMessage(message):
  messages.remove(message)

def removeSpecificFiles(file):
  files.remove(file)

def removeAllContacts():
  contacts.clear()

def removeAllMessages():
  messages.clear()

def removeAllFiles():
  files.clear()

def clearBot():
  removeAllContacts()
  removeAllMessages()
  removeAllFiles()

def startConection():
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.get("https://web.whatsapp.com")
  WebDriverWait(driver, timeout=3600).until(EC.presence_of_element_located((By.ID, 'pane-side')))
  time.sleep(2)
  return driver

def searchContact(driver, contact):
  inputSearchContact = driver.find_element(By.XPATH, '//div[contains(@class, "copyable-text selectable-text")]')
  time.sleep(2)
  inputSearchContact.click()
  inputSearchContact.send_keys(contact)
  inputSearchContact.send_keys(Keys.ENTER)
  time.sleep(1)

def writeMessage(driver, messages):
  for message in messages:
    formattedMessage = message.split("\n")

    inputSendMessage = driver.find_element(By.XPATH, '//p[contains(@class, "selectable-text copyable-text")]')
    inputSendMessage.click()

    for eachLineBreakMessage in formattedMessage:
        inputSendMessage.send_keys(eachLineBreakMessage)
        inputSendMessage.send_keys(Keys.SHIFT, Keys.ENTER)

    inputSendMessage.send_keys(Keys.ENTER)
    time.sleep(1)

def definingFiles(driver, files):
  for file in files:
    clip = driver.find_element(By.CSS_SELECTOR, 'span[data-icon="clip"]')
    clip.click()

    if '.png' in file and '.jpg' in file and '.jpeg' in file:
      fileInput = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input')
    else:
      fileInput = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input')

    fileInput.send_keys(file)
    time.sleep(1)
    sendButton = driver.find_element(By.XPATH, '//div[contains(@class, "_165_h _2HL9j")]')
    sendButton.click()
    time.sleep(1)

def sendMessages():
  driver = startConection()
  for contact in contacts:
    searchContact(driver, contact)
    writeMessage(driver, messages)
    definingFiles(driver, files)
    time.sleep(1)