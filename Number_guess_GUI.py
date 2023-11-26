from tkinter import *
import random

window = Tk()
window.title("Number Guessing Game")
window.geometry("500x300")

Secret_Number = None


def startGame():
    global Secret_Number

    for button in button_list:
        randomNumber= random.randint(0,1000)
        button.config(text= str(randomNumber))
    
    randomButton = random.choice(button_list)

    Secret_Number = randomButton.cget("text")

    print("Secret Number is: ", Secret_Number)

def onClick(event):
    btn = event.widget
    buttonText = btn.cget("text")

    if Secret_Number == buttonText:
        message = "You nailed it! The number was " + str(Secret_Number)        
    else:
        message = "Sorry, the number was " + str(Secret_Number)
    answer_label.config(text= message)
    startGame()

title_label= Label(window, text="Guess the Secret Number", font=("Ubuntu"), pady= 8, justify="center")
button_one = Button(window, text="00", font=("Helvetical 15"), width=6, pady=15, bg="lightgreen")
button_two = Button(window, text="00", font=("Helvetical 15"), width=6, pady=15, bg="skyblue")
button_three = Button(window, text="00", font=("Helvetical 15"), width=6, pady=15, bg="coral")

answer_label = Label(window, text= "Answer", font=("Ubuntu"), pady=9, fg= "purple", justify="center")

button_list = [button_one, button_two, button_three]

title_label.pack()

button_one.pack()
button_two.pack()
button_three.pack()
answer_label.pack()

button_one.bind("<Button-1>", onClick)
button_two.bind("<Button-1>", onClick)
button_three.bind("<Button-1>", onClick)

# if __name__ == "__main__":
startGame()

window.mainloop()