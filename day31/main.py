from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
card={}
to_learn={}
try:
    data=pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original=pandas.read_csv('data/french_words.csv')
    to_learn=original.to_dict(orient='records')
else:
    to_learn=data.to_dict(orient='records')


def next_card():
    global card,display
    windows.after_cancel(display)
    card=random.choice(to_learn)
    canvas.itemconfig(language,text='French',fill='black')
    canvas.itemconfig(word,text=card['French'],fill='black')
    canvas.itemconfig(font_image,image=image)
    display=windows.after(3000,flip)
def flip():
    canvas.itemconfig(language, text='English',fill='yellow')
    canvas.itemconfig(word, text=card['English'],fill='black')
    canvas.itemconfig(font_image, image=background_image)
def know():
    to_learn.remove(card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
windows=Tk()
windows.title('flash cards')
windows.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
display=windows.after(3000,func=flip)
#keys
background_image=PhotoImage(file='images/card_back.png')
image=PhotoImage(file='images/card_front.png')
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
font_image=canvas.create_image(400,263,image=image)
language=canvas.create_text(400,154,text='Tittle',font=('Arail',40,'italic'))
word=canvas.create_text(400,300,text='word',font=('Arial',40,'bold'))
canvas.grid(column=0,row=0,columnspan=2)
#buttons
right_image=PhotoImage(file='images/right.png')
right=Button(image=right_image,highlightthickness=0,command=know)
right.grid(column=1,row=2)

wrong_image=PhotoImage(file='images/wrong.png')
wrong=Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong.grid(column=0,row=2)
next_card()

windows.mainloop()