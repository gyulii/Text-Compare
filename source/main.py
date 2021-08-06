import tkinter as tk
from tkinter import *


def CHECK_DIFF():
	s1 = input_1.get("1.0","end")
	s2 = input_2.get("1.0","end")

	seq_matcher = dl.SequenceMatcher(None, s1, s2)

	output = ""

	for tag, i1, i2, j1, j2 in seq_matcher.get_opcodes():
		if(tag == "equal"):
			textbox_3.insert(END,s2[j1:j2], )
		if(tag == "replace"):
			textbox_3.insert(END,s1[i1:i2], 'yellow')   
			textbox_3.insert(END,s2[j1:j2], 'green')
		if(tag == "delete"):
			textbox_3.insert(END,s1[i1:i2], 'red')  
		if(tag == "insert"):
			textbox_3.insert(END,s2[j1:j2], 'blue')  
	


def CLEAR_INPUT_AND_OUTPUT():
	input_1.delete("1.0", END)
	input_2.delete("1.0", END)
	textbox_3.delete("1.0" , END)



root = Tk()
root.title("Text compare")
root.geometry("1920x1080")


# Define objects

label_bemenet1 = Label(root, text=" Eredeti szöveg: ")
label_bemenet2 = Label(root, text=" Módosított szöveg: ")


input_1 = tk.Text(borderwidth=1, height= 25 , width= 100)
input_2 = tk.Text(borderwidth=1, height= 25 , width= 100)
empty_label_1 = Label(root,text="" , width= 10)
empty_label_2 = Label(root, text= "", width= 10)
textbox_3 = tk.Text(borderwidth=1, height= 33, width= 150)


# Define buttons
# LAMBDA !!!

check_button = Button(root, text="Különbség", command= lambda:CHECK_DIFF())
clear_button = Button(root, text="Törlés", command= lambda:CLEAR_INPUT_AND_OUTPUT())


# OUTPUT COLOR DEFINE

textbox_3.tag_config('yellow', background="yellow", foreground="black")
textbox_3.tag_config('red', background="red", foreground="black")
textbox_3.tag_config('green', background="green", foreground="black")
textbox_3.tag_config('blue', background="blue", foreground="white")



#Place objects


label_bemenet1.grid(row=0, column=3)
label_bemenet2.grid(row=0, column= 9)


input_1.grid(row=1,column=3)
empty_label_1.grid(row=1, column=4)
input_2.grid(row=1,column=9)

empty_label_2.grid(row = 2, column= 2)
textbox_3.grid(row=3,column=0,rowspan=15,columnspan=10)



#Place buttons


check_button.grid(row=2,column=4)
clear_button.grid(row=2, column=3)



root.mainloop()