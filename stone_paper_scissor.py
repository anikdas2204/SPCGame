import random
import tkinter
import tkinter.font as font

stats = []
option = [1,2,3]


def get_winner(call):
    o = random.choice(option)
    if o == 1:
        throw = "ROCK"
    elif o == 2:
        throw = "SCISSORS"
    else:
        throw = "PAPER"

    if (throw == "ROCK" and call == "PAPER") or (throw == "PAPER" and call == "SCISSORS") or (throw == "SCISSORS" and call == "ROCK"):
        stats.append("WON")
        result = " YOU WON !!! "
    elif throw == call:
        stats.append("DRAW")
        result = " DRAWN !!! "
    else:
        stats.append("LOST")
        result = " YOU LOST !!! "

    global output
    output.config(text="COMPUTER THREW: " + throw + "\n" + result)


def pass_s():
    get_winner("SCISSORS")


def pass_r():
    get_winner("ROCK")


def pass_p():
    get_winner("PAPER")


window = tkinter.Tk(className=" STONE PAPER SCISSOR")
window.geometry("700x120")

myFont1 = font.Font(family='jokerman')
myFont2 = font.Font(family='Algerian')
myFont3 = font.Font(family='Algerian')
myFont4 = font.Font(family='Times New Roman')

first = tkinter.Label(window, width=5, height=2, fg="#ffffff")
SCISSORS = tkinter.Button(window, text="SCISSORS", bg="#ed5050", padx=10, pady=5, command=pass_s, width=10, height=2, activebackground='#e7b1b1')
ROCK = tkinter.Button(window, text="ROCK", bg="#3bf73b", padx=10, pady=5, command=pass_r, width=10, height=2, activebackground='#a0de7c')
PAPER = tkinter.Button(window, text="PAPER", bg="#208cf8", padx=10, pady=5, command=pass_p, width=10, height=2, activebackground='#8cd0ee')
output = tkinter.Label(window, width=30, height=2, fg="#c90808", text="SELECT YOUR CALL")

SCISSORS['font']=myFont1
ROCK['font']=myFont1
PAPER['font']=myFont1
output['font']=myFont4

first.pack(side="left")
SCISSORS.pack(side="left")
ROCK.pack(side="left")
PAPER.pack(side="left")
output.pack(side="right")

window.mainloop()

for i in stats: print(i, end=" ")
if stats.count("LOST") > stats.count("WON"):
    result = "\nYou lost the series."
elif stats.count("LOST") == stats.count("WON"):
    result = "\nSeries ended in a draw."
else:
    result = "\nYou won the series."

print(result)