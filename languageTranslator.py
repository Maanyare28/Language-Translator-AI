from google import genai

textWeWantTranslated = input("Enter text you want to translate, in what language")

client = genai.Client(api_key="AIzaSyDS-_EK2JF3DmpJIhJ4xI89b3l1zHWECso")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents=textWeWantTranslated
)
print(response.text)



#logic

# Create a python window


#Customize python window so it can look the way I want it to look

# Have 2 sections one for the language you want to translate from and the other the lagnauge u want translated

# Add a dropdown of all the languages for both

#Have a translate button to translate it 

#Actual Translator

#We gonna make it iterate first before doing design

# textWantedTranslated = input("What do you want translated? ")

#When we get the translated text, we put it into gemini
#First we ask what language do you want to translate from?
#Secon we ask what language do you want to translate to?
#Then we enter the text that we want translated


#lets get gemini in here
#gemini API endpoint

























#Bonus: being able to take an image and then converting it to text, then after that translating that text into another language.
