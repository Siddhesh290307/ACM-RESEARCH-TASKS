import re

def transform_text(input_text: str) -> str:
    #Replaces emails with "EMAIL"
    text = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}","EMAIL",input_text)

    #replaces Indian phone numbers
    text = re.sub(r"(?:\+91[\s-]?)?[6-9][0-9]{9}","PHONE NO",text)

    #replace "Python" with snake emoji 🐍
    text = re.sub(r"Python", "🐍", text)

    return text


s=input("Enter text:")
print("Transformed text:", transform_text(s))

#SAMPLE OUTPUT:
#Enter text: I love Python. My email is nadkarnisiddhesh2903@gmail.com and my phone no is 9769478991
#Transformed text:  I love 🐍. My email is EMAIL and my phone no is PHONE NO