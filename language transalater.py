from tkinter import *
from deep_translator import GoogleTranslator

# Window setup
screen = Tk()
screen.title("Language Translator")
screen.geometry("400x300")

# Variables
input_language_choice = StringVar()
translate_language_choice = StringVar()
text_var = StringVar()
output_var = StringVar()

# Languages
language_choices = ['english', 'hindi', 'french', 'german', 'spanish','japanese','italian','arabic','bengali','kannada','korean','greek','nepali','russian']
input_language_choice.set('english')
translate_language_choice.set('hindi')

# Translation function
def translate_text():
    try:
        translated = GoogleTranslator(
            source=input_language_choice.get(),
            target=translate_language_choice.get()
        ).translate(text_var.get())
        output_var.set(translated)
    except Exception as e:
        output_var.set("Error: " + str(e))

# UI Widgets
Label(screen, text="From Language").grid(row=0, column=0)
OptionMenu(screen, input_language_choice, *language_choices).grid(row=0, column=1)

Label(screen, text="To Language").grid(row=1, column=0)
OptionMenu(screen, translate_language_choice, *language_choices).grid(row=1, column=1)

Label(screen, text="Enter Text").grid(row=2, column=0)
Entry(screen, textvariable=text_var).grid(row=2, column=1)

Button(screen, text="Translate", command=translate_text).grid(row=3, column=0)

Label(screen, text="Output").grid(row=4, column=0)
Entry(screen, textvariable=output_var).grid(row=4, column=1)

screen.mainloop()