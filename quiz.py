import tkinter as tk
import pandas as pd
import uuid
import os

def eval():
    global ix, question, v, radio_buttons, next_button, response
    global selected, score

    answer = v.get()
    selected.append(answer)
    question.destroy()
    next_button.destroy()
    for button in radio_buttons: button.destroy()

    if answer == ANSWERS[ix]:
        root.configure(bg='#028A0F')
        response = tk.Label(root, text='You got it correct, well done!', font=font, bg='#028A0F')
        response.grid(row=2)
        next_button = tk.Button(root, text='Next', font=font, height=5, width=15, command=next)
        next_button.grid(row=len(OPTIONS[ix])+1)
        score += 1
        
    else:
        root.configure(bg='#B90E0A')
        response = tk.Label(root, text='You got it wrong, better luck next time!', font=font, bg='#B90E0A')
        response.grid(row=2)
        next_button = tk.Button(root, text='Next', font=font, height=5, width=15, command=next)
        next_button.grid(row=len(OPTIONS[ix])+1)

def next():
    global ix, question, v, radio_buttons, next_button, response
    global name, email, score, selected

    root.configure(bg=default)
    response.destroy()
    next_button.destroy()
    ix += 1
    if ix < len(QUESTIONS):
        question = tk.Label(root, text=QUESTIONS[ix], font=font, wraplength=1000, justify='center')
        question.grid(row=0)
        v = tk.IntVar()
        radio_buttons = []
        for i, j in enumerate(OPTIONS[ix]):
            radio_button = tk.Radiobutton(root, text=j, variable=v, value=i, font=font, wraplength=1000, justify='center')
            radio_button.grid(row=i+1)
            radio_buttons.append(radio_button)
        next_button = tk.Button(root, text='Next', font=font, height=5, width=15, command=eval)
        next_button.grid(row=len(OPTIONS[ix])+1)
    else:
        out = {'Email Address': [email], 'Score': [score], 'Name': [name], 'Group': ['C']}
        for i, j in enumerate(selected):
            out[QUESTIONS[i]] = [OPTIONS[i][selected[i]]] 
        df = pd.DataFrame.from_dict(out)
        if not os.path.exists(os.path.join(os.getcwd(), 'results')):
            os.makedirs(os.path.join(os.getcwd(), 'results'))
        df.to_csv(os.path.join(os.getcwd(), 'results', f'{uuid.uuid4()}.csv'))
        root.destroy()

def start():
    global name, email
    global greeting, start_button
    global name_label, name_entry
    global email_label, email_entry
    global ix, question, v, radio_buttons, next_button

    # store entries and destroy
    name = name_entry.get()
    email = email_entry.get()
    greeting.destroy()
    name_label.destroy()
    name_entry.destroy()
    email_label.destroy()
    email_entry.destroy()
    start_button.destroy()

    # start qn index
    ix = 0
    question = tk.Label(root, text=QUESTIONS[ix], font=font, wraplength=1000, justify='center')
    question.grid(row=0)

    v = tk.IntVar()
    radio_buttons = []
    for i, j in enumerate(OPTIONS[ix]):
        radio_button = tk.Radiobutton(root, text=j, variable=v, value=i, font=font, wraplength=1000, justify='center')
        radio_button.grid(row=i+1)
        radio_buttons.append(radio_button)

    next_button = tk.Button(root, text='Next', font=font, height=5, width=15, command=eval)
    next_button.grid(row=len(OPTIONS[ix])+1)

    root.columnconfigure((0), weight=1)
    root.rowconfigure(list(range(1,len(OPTIONS[ix])+1)), weight=1)
    root.rowconfigure((0,len(OPTIONS[ix])+1), weight=3)

if __name__ == '__main__':
    # globals
    QUESTIONS = ['What is the moral of the video?',
                'How long ago did Ants originate?',
                'When two army ant colonies encounter each other, which of the following happens?',
                'Which of the following is true?',
                'What is the main reason army ants are so feared?',
                'How many different species are there in army ant groups?',
                'What will leafcutter ants do first to defend against army ants?',
                'What will leafcutter ants do second to defend against army ants?',
                'Army ant species Nomamyrmex Esenbeckii is the only known species that can successfully attack a mature colony of leafcutters.',
                'The war of ants only happens among different species.']
    OPTIONS = [['Some groups just don\'t get along', 'Don’t be greedy, be content with what you have', 'Death is as much part of life, as life itself', 'Where there is a will, there is a way'],
            ['160 billion years ago', '160 million years ago', '6 million years ago', '6 thousand years ago'],
            ['The colonies fight, to the death', 'The colonies pass through each other or just move away from each other', 'The colonies merge together', 'None of the above'],
            ['Army ants are so deadly that other ant species had to specialize to survive their presence', 'Many species stand their ground and fight instead of evacuating when seeing an army ant scout', 'Some ants have big square heads built to crush army ants', 'None of the above'],
            ['The fact that they come in extremely large numbers', 'Their painful bites', 'Their venomous stingers', 'Their ability to burrow'],
            ['About 2 trillion species', 'About 2 billion species', 'About 2 million species', 'About 200 species'],
            ['Kick them', 'Lock on them and try to cut through their heads', 'Block entrances to their nest with their square heads', 'Sting them to death, in a mob'],
            ['They seal of entrances to their nest', 'They run away', 'They rush in and surround their eggs', 'None of the above'],
            ['True', 'False'],
            ['True', 'False']]
    ANSWERS = [0,1,1,0,0,3,1,0,0,1]
    name = None
    email = None
    v = None
    ix = None
    question = None
    radio_buttons = None
    next_button = None
    response = None
    
    score = 0
    selected = []

    font = ('Menlo', 30)

    root = tk.Tk()
    root.geometry('1450x1000')
    root.title('Quiz')
    default = root.cget('bg')
    
    greeting = tk.Label(root, text='Enter your email and name and start the quiz, good luck!', font=font)
    greeting.grid(row=0)
    
    name_label = tk.Label(root, text='Name', font=font)
    name_label.grid(row=1)
    name_entry = tk.Entry(root)
    name_entry.grid(row=2)

    email_label = tk.Label(root, text='Email', font=font)
    email_label.grid(row=3)
    email_entry = tk.Entry(root)
    email_entry.grid(row=4)

    start_button = tk.Button(root, text='Start', font=font, height=5, width=15, command=start)
    start_button.grid(row=5)

    root.columnconfigure((0), weight=1)
    root.rowconfigure((1,2,3,4), weight=1)
    root.rowconfigure((0,5), weight=3)

    root.mainloop()