from fnmatch import translate

from google import genai
import tkinter as tk
from tkinter import ttk
'''
languageWeAreTranslatingFrom = input("Enter the language you want to translate from: ")
languageWeAreTranslatingTo = input("Enter the language you to translate to: ")
textWeWantTranslated = input("Enter text you want to translated: ")

whatWeTranslatingTo = "Translate to: " + languageWeAreTranslatingTo
whatWeTranslatingFrom = "Translate from: " + languageWeAreTranslatingFrom


client = genai.Client(api_key="AIzaSyDS-_EK2JF3DmpJIhJ4xI89b3l1zHWECso")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents=languageWeAreTranslatingFrom + languageWeAreTranslatingTo + textWeWantTranslated
)
print(response.text)
'''

'''
def on_select(event):
    translateFromDropdown = translateFrom.get()
    translateToDropdown = translateTo.get()
    print(translateToDropdown)
    print(translateFromDropdown)
'''

def get_TranslateToBox():
    global content
    global translateFromDropdown
    global translateToDropdown
    content = textToTranslateBox.get("1.0", tk.END).strip()
    print(content)
    translateFromDropdown = translateFrom.get()
    translateToDropdown = translateTo.get()
    print(translateToDropdown)
    print(translateFromDropdown)
    #Gets content
    #Gets dropdown
    #translates

#copy variables out
textToTranslateBoxSaved = "Translate this text: " + content
translateFromDropdownSaved = "Translate to this language: " + translateToDropdown
translateToDropdownSaved = "Translate from this language: " + translateFromDropdown

# Create a python window
root = tk.Tk() #basically we make it so instead of always calling tk we just call root
root.title("Translater") #name of the window
root.geometry("550x600") #window size

#creating widgets
#Text to translate Box
textToTranslateBox = tk.Text(root, height=15, width=30)
textToTranslateBox.place(x=5, y=50)

#Text Translated Box
textTranslatedBox = tk.Text(root, height=15, width=30)
textTranslatedBox.place(x=300, y=50)

#Dropdown Options
options = ["English", "Spanish", "German", "French", "Italian", "Portuguese", "Russian", "Japanese", "Korean", "Chinese", "Arabic", "Hindi", "Turkish"]

#Dropdown Menu (idk why its called combo box)

#For translate from dropdown
translateFrom = ttk.Combobox(root, values=options)
translateFrom.place(x=40,y=20)
translateFrom.set("Select a Language")
translateFrom.bind("<<TranslateFromSelected>>", get_TranslateToBox)

#For translate to dropdown
translateTo = ttk.Combobox(root, values=options)
translateTo.place(x=350,y=20)
translateTo.set("Select a Language")
translateTo.bind("<<TranslateToSelected>>", get_TranslateToBox)




#Button
translateButton = tk.Button(root, text="Translate", command=get_TranslateToBox)
translateButton.place(x=235,y=320)



'''
Ok i just need to gget my thoughts out
soooo, we get the input from the text box then save it in a varaible 
that says: "text we want to translate from"
we get the selected dropdown option then save it in a variable that says "Langauge we want to translate to" 
and "language we want to translate from"
Then we concatonate it to gemini, starting with language we want to translate from, text we want to translate from,
then language we want to translate to
*I tink we need a button at some point to confirm 
then it outputs it in the textbox text translated.

Then we can work on exceptions such as if the text box is left empty, print("text box is empty enter text")
'''


root.mainloop()
























#Bonus: being able to take an image and then converting it to text, then after that translating that text into another language.
