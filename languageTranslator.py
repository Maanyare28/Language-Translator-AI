

from google import genai
import tkinter as tk
from tkinter import ttk





def get_TranslateToBox():
    content = "Translate this text: " + textToTranslateBox.get("1.0", tk.END).strip()
    translateFromDropdown = "From this language: " + translateFrom.get()
    translateToDropdown = "To this language: " + translateTo.get()
    findtuner = ("Only give me the translation nothing else.")
    missingStuff = ("If you see that the text or languages were not selected or are missing say so.")
    client = genai.Client(api_key="AIzaSyDS-_EK2JF3DmpJIhJ4xI89b3l1zHWECso")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=content+translateToDropdown+translateFromDropdown+findtuner+missingStuff
    )
    textTranslatedBox.delete("1.0", tk.END)
    textTranslatedBox.insert(tk.END,response.text)


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






root.mainloop()





























#Bonus: being able to take an image and then converting it to text, then after that translating that text into another language.
