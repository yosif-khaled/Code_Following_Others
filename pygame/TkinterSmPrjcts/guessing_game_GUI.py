import tkinter
import random


computer_guess = random.randint(1,10)

def check():
	#get value from txt_guess
	user_guess = int(txt_guess.get())
	
	
	#determine if the user guess higher, lower or right on spot
	if user_guess < computer_guess:
		msg = "Higher"
	elif user_guess > computer_guess:
		msg = "Lower"
	elif user_guess == computer_guess:
		msg = "Correct"
	else:
		msg = "something went wrong"
		
	#show result
	lbl_result["text"] = msg
	#clear msg
	txt_guess.delete(0, 5)

def reset():
	global computer_guess
	#check what global means
	computer_guess = random.randint(1, 10)
	#change lbl_result
	lbl_result["text"] = "Guess Again!!"

#create root window
# he used root instead of tk got me confused but now I am enlightened
# I can use any name :)
tk = tkinter.Tk()
tk.title("Guessing Game")

#if you want to change background color
#add bg = "color name"
#tk.configure(bg = "color name")

#to change window size

tk.geometry("300x150")

#create widgets
##what is a widget by the way?!!

lbl_title = tkinter.Label(tk, text = "Welcome to the Guessing Game!")
lbl_title.pack()

lbl_result = tkinter.Label(tk, text = "Good Luck!")
lbl_result.pack()

btn_check = tkinter.Button(tk, text = "Check", fg = "green", command = check)
btn_check.pack(side = "left")

btn_reset = tkinter.Button(tk, text = "Reset", fg = "blue", command = reset)
btn_reset.pack(side = "right")

btn_quit = tkinter.Button(tk, text = "Quit", fg = "red", command = tk.quit)
btn_quit.pack()

txt_guess = tkinter.Entry(tk, width = 3)
txt_guess.pack()





#start the main events loop
tk.mainloop()
tk.destroy()
