from google import genai
import tkinter as tk
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

#Dropdown options
options = ["English", "Spanish", "German", "French", "Italian", "Portuguese", "Russian", "Japanese", "Korean", "Chinese", "Arabic", "Hindi", "Turkish"]






root.mainloop()

#Dropdown box to pick






















#Bonus: being able to take an image and then converting it to text, then after that translating that text into another language.
