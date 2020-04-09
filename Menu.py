
from tkinter import *
import random
import button_profile
from PIL import Image, ImageTk

default_color = '#d1fcf1'
turn_highlighter = '#b4c481'
#GUI STARTS
root = Tk()
root.title("TicTacToe")
#menu_frame.geometry('1300x590')
root.configure(background = default_color)

#----------------------------------MAIN MENU SECTION STARTS---------------------------------------------------
def mode_selector(mode):
	turn = random.sample(range(1,3), 1)
	menu_frame.forget()
	print("IM MODE SELECTOR OUT")
	if mode == 1:
		button_profile.game_mode.update({1:['Human vs Beatable Bot',1]})
	elif mode == 2:
		button_profile.game_mode.update({1:['Human vs UnBeatable Bot',2]})
	else:
		button_profile.game_mode.update({1:['Human vs Human',3]})
		print("IN MODE INSIDE MODE 3")
		import test

menu_frame = LabelFrame(root, bg = default_color)

#load images
hvb = ImageTk.PhotoImage(Image.open('humanvsbot.png'))
hvh = ImageTk.PhotoImage(Image.open('humanvshuman.gif'))
hvbu = ImageTk.PhotoImage(Image.open('hvbu.png'))
circle_img = ImageTk.PhotoImage(Image.open('circle.png'))
cross_img = ImageTk.PhotoImage(Image.open('cross.png'))


# #defining frames
mode_frame = LabelFrame(menu_frame, bg = default_color, border = 0)
# menu_frame = LabelFrame(menu_frame, height = 40, width = 500)

#defining buttons
bot_button = Button(mode_frame, text = 'Bot vs Human', bg = '#8fe9df', command = lambda: mode_selector(1))
unb_bot_button = Button(mode_frame, text = 'Try with Unbeatable Bot', bg = '#8fe9df', command = lambda: mode_selector(2))
human_button = Button(mode_frame, text = 'Human vs Human', bg = '#8fe9df', command = lambda: mode_selector(3))
back_button = Button(menu_frame, height = 2,width = 20, text = "Go back", bg = '#ff7fbf', fg = 'black')
exit_button = Button(menu_frame, height = 2,width = 35, text = "Exit Game", bg = '#ff7fbf', command = root.destroy)
how_to_play_button = Button(menu_frame, height = 2,width = 25, text = "How to Play?", bg = '#ff7fbf')
developer_button = Button(menu_frame, height = 2,width = 30, text = "About Developer", bg = '#ff7fbf')

#defining labels
image_label_1 = Label(mode_frame, image = hvb, bg = default_color)
image_label_2 = Label(mode_frame, image = hvh, bg = default_color)
image_label_3 = Label(mode_frame, image = hvbu, bg = default_color)
heading_label = Label(menu_frame, height = 2, width = 130, text = "Tic Tac Toe", bg = '#444c54', fg = 'white')
mode_label = Label(menu_frame, height = 2,width = 50, text = "Select Mode", bg = '#ff7fbf', fg = 'black')

#placing labels
image_label_1.grid(row = 0, column = 1)
image_label_3.grid(row = 0, column = 2)
image_label_2.grid(row = 0, column = 3)
heading_label.grid(row = 1, columnspan = 4, sticky = E+W)
mode_label.grid(row = 2, column = 0, sticky = W+N, columnspan = 2, rowspan = 1, pady = 15)

#placing buttons
back_button.grid( row = 6, column = 0, sticky = W, columnspan = 2)
developer_button.grid(row = 5, column = 1,pady = 2, sticky = E, columnspan = 2)
how_to_play_button.grid(row = 4, column = 1, padx = 2, sticky = E, columnspan = 2)
exit_button.grid(row = 6, column = 1, pady = 2, sticky = E, columnspan = 2)
bot_button.grid(row=1, column=1, padx=5, pady=12)
unb_bot_button.grid(row=1, column=2, padx=5, pady=1)
human_button.grid(row=1, column=3, padx=5, pady=12)

# #placing frames
menu_frame.pack()
mode_frame.grid(row = 3, column = 1, columnspan = 2, padx = 10,pady = 10)
root.mainloop()
#-----------------------------MAIN MENU SECTION ENDS-------------------------------------------------------------
