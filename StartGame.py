from tkinter import *
import button_profile
import random
from PIL import ImageTk, Image
import ttt

#colour definitions
default_color = '#d1fcf1'
turn_highlighter = '#b4c481'


#GUI STARTS
root_child = ttt.root

#global Variables
turn = 1

def gimme_index(but_no):
	return {
		1:[0,0],
		2:[0,1],
		3:[0,2],
		4:[1,0],
		5:[1,1],
		6:[1,2],
		7:[2,0],
		8:[2,1],
		9:[2,2]
	}.get(but_no)


def catch_menu():
	parent_frame.pack_forget()
	import ttt


def play_again(parent_frame):
	print('inhere')
	#reset the board
	for i in range(0,3):
		for j in range(0,3):
			button_profile.button_stat1[i][j] = ' '
	parent_frame.pack_forget()
	ttt.mode_selector(button_profile.game_mode.get(1))

#-----main engine-----human vs human------
def update_button(ro, col, button_number, palo, buttton_name):
	global turn
	index_x, index_y = gimme_index(button_number)
	
	#update the button configurations and status
	if palo == 1:
		turn = 2
		button_profile.button_stat.update({button_number: 1})
		button_profile.button_stat1[index_x][index_y] = 'X'
		button_name = Button(main_frame, image = ttt.cross_img, bg = default_color, border = 0)
		player1_label.configure(bg = default_color)
		player2_label.configure(bg = turn_highlighter)
		button_name.grid(row = ro, column = col, rowspan = 1, columnspan = 1, padx= 0, pady = 0)
		current_turn_label.configure(text = 'Current Player:   {}'.format(button_profile.players_name.get('player2_name')))
		button_mode('disabled',button_name)
	else:
		turn = 1
		button_profile.button_stat.update({button_number: 2})
		button_profile.button_stat1[index_x][index_y] = '0'
		button_name = Button(main_frame, image = ttt.circle_img, bg = default_color,border = 0, state = DISABLED)
		button_mode('disabled',button_name)
		player2_label.configure(bg = default_color)
		player1_label.configure(bg = turn_highlighter)
		button_name.grid(row = ro, column = col, rowspan = 1, columnspan = 1)
		current_turn_label.configure(text = 'Current Player:   {}'.format(button_profile.players_name.get('player1_name')))
		button_mode('disabled',button_name)
	by, orientation = check_status()
	print(button_profile.button_stat1, by, orientation)
	
	#Check the winner if any
	if by == 'X':
		button_mode('disabled', 'all')
		go_back_button.grid(row = 4, column = 3, sticky = E+W)
		play_again_button.grid(row = 3, column = 3,  sticky = E)
		player1_label.configure(bg = 'light green')
		player2_label.configure(bg = default_color)
		current_turn_label.configure(bg = default_color, font = "15", width = 20, text = '{} is the winner'.format(button_profile.players_name.get('player1_name')))
	elif by == '0':
		button_mode('disabled','all')
		go_back_button.grid(row = 4, column = 3, sticky = E+W)
		play_again_button.grid(row = 3, column = 3,  sticky = E)
		player2_label.configure(bg =  'light green')
		player1_label.configure(bg = default_color)
		current_turn_label.configure(bg = default_color, font = " 15", width = 20, text = '{} is the winner'.format(button_profile.players_name.get('player2_name')))
	elif by == 'tied':
		button_mode('disabled','all')
		current_turn_label.configure(text = 'Game Tied....', bg = 'grey')
		play_again_button.grid(row = 3, column = 3,  sticky = E)
		go_back_button.grid(row = 4, column = 3, sticky = E+W)

	else:
		print('')

def button_mode(stat, button_name):
	global b1, b2, b3, b4, b5, b6, b7, b8, b9
	if button_name == 'all':	
		#Enable button status
		b1['state']= stat
		b2['state']= stat
		b3['state']= stat
		b4['state']= stat
		b5['state']= stat
		b6['state']= stat
		b7['state']= stat
		b8['state']= stat
		b9['state']= stat
	else:
		try:
			button_name['state'] = stat
		except NameError:
			raise 'NameError'

#start main game with player 1
def start_game():
	entry_button.destroy()
	entry_label.destroy()
	discard_name_button.destroy()
	current_turn_label.configure(text = 'Current Player:   {}'.format(button_profile.players_name.get('player1_name')), width = 70, bg = '#b4c481')
	current_turn_label.pack()
	button_mode('normal', 'all')

	
#update name accepting entrybox
def player_name(name, palo):
	global turn, player1_label, player2_label
	if palo == 1:
		entry_label.delete(0, END)
		button_profile.players_name.update({'player1_name': name})
		player1_label.configure(text = button_profile.players_name.get('player1_name'), bg = default_color)
		player2_label.configure(bg = turn_highlighter)
		entry_label.insert(0, 'Enter player 2\'s name....')
		player1_label.grid(row = 2, column = 1, padx = 30, pady =30)
		turn = 2
	elif palo == 2:
		button_profile.players_name.update({'player2_name': name})
		player2_label.configure(text = button_profile.players_name.get('player2_name'), bg = default_color)
		player2_label.grid(row = 2, column = 3, sticky = E, padx = 30, pady =30)
		player1_label.configure(bg = turn_highlighter)
		turn = random.sample(range(1,3),1)
		start_game()

#check winnig status ---Return type meaning: 'not won' , 1 or 2 with row and column according to winer= winning type,'tied' = tied game 
def check_status():
	stat = 0
	temp = 0
	temp_integer = 1
	#check horizontal
	for i in range(0,3):
		for j in range(0,2):
			if button_profile.button_stat1[i][j] == button_profile.button_stat1[i][j+1] and button_profile.button_stat1[i][j] != ' ':
				stat += 1 
				temp = button_profile.button_stat1[i][j]
		if stat == 2:
			return temp,'row'
		stat = 0

	#check vertical
	for j in range(0,3):
		for i in range(0,2):
			if button_profile.button_stat1[i][j] == button_profile.button_stat1[i+1][j] and button_profile.button_stat1[i][j] != ' ':
				stat += 1
				temp = button_profile.button_stat1[i][j]
			if stat == 2:
				return temp,'col'
		stat = 0
	
	#check diagonal
	if button_profile.button_stat1[0][0] == button_profile.button_stat1[1][1] and button_profile.button_stat1[0][0] == button_profile.button_stat1[2][2] and button_profile.button_stat1[1][1] != ' ':
		return button_profile.button_stat1[1][1],'\\'
	if button_profile.button_stat1[0][2] == button_profile.button_stat1[1][1] and button_profile.button_stat1[0][2] == button_profile.button_stat1[2][0] and button_profile.button_stat1[1][1] != ' ':
		return button_profile.button_stat1[1][1],'/'
	if not ' ' in button_profile.button_stat1:
		return 'tied',''
	else:
		return 'not won',''

#parent_frame widgets definitions
parent_frame = LabelFrame(root_child, bg = default_color, border = 0)
main_frame = LabelFrame(parent_frame, bg = default_color, border = 0)
heading_label = Label(parent_frame, height = 2, width = 60, font = 'Courier, 15', text = "Tic Tac Toe", bg = '#444c54', fg = 'white')
mode_label = Label(parent_frame, height = 2, width = 30, text = 'Game Mode:  ' + button_profile.game_mode.get(1)[0], bg = '#7fffbf', fg='black')
player1_label = Label(parent_frame, height = 2, text = button_profile.players_name.get('player1_name'), bg = turn_highlighter)
player2_label = Label(parent_frame, height = 2, text = button_profile.players_name.get('player2_name'), bg = default_color)
bottom_frame = LabelFrame(parent_frame, bg = default_color, border = 0)
entry_label = Entry(bottom_frame, width = 30, borderwidth = 5)
current_turn_label = Label(bottom_frame, width = 30, bg = default_color)

#main_frame widgets definitions
line_1_1 = Canvas(main_frame, width = 505, height = 6, bg = "black")
line_1_2 = Canvas(main_frame, width = 505, height = 6, bg = "black")
line_2_1 = Canvas(main_frame, width = 6, height = 405, bg = "black")
line_2_2 = Canvas(main_frame, width = 6, height = 405, bg = "black")

#creating canvas for lines
line_1_1.create_rectangle(0,0,5,3)
line_1_2.create_rectangle(0,0,5,3)
line_2_1.create_rectangle(0,0,0,6)
line_2_2.create_rectangle(0,0,5,2)


#button definitions
b1 = Button(main_frame,  state = DISABLED, bg = default_color, width = 21, height = 8, command = lambda: update_button(1,1,1,turn,'b1'))
b2 = Button(main_frame,  state = DISABLED, bg = default_color, width = 21, height = 8, command = lambda: update_button(1,3,2,turn,'b2'))
b3 = Button(main_frame,  state = DISABLED, bg = default_color, width = 21, height = 8, command = lambda: update_button(1,5,3,turn,'b3'))
b4 = Button(main_frame,  state = DISABLED, bg = default_color, width = 21, height = 8, command = lambda: update_button(3,1,4,turn,'b4'))
b5 = Button(main_frame,  state = DISABLED, bg = default_color, width = 21, height = 8, command = lambda: update_button(3,3,5,turn,'b5'))
b6 = Button(main_frame,  state = DISABLED, bg = default_color, width = 21, height = 8, command = lambda: update_button(3,5,6,turn,'b6'))
b7 = Button(main_frame,  state = DISABLED, bg = default_color, width = 21, height = 8, command = lambda: update_button(5,1,7,turn,'b7'))
b8 = Button(main_frame,  state = DISABLED, bg = default_color, width = 21, height = 8, command = lambda: update_button(5,3,8,turn,'b8'))
b9 = Button(main_frame,  state = DISABLED, bg = default_color, width = 21, height = 8, command = lambda: update_button(5,5,9,turn,'b9'))
entry_button = Button(bottom_frame, width = 2, height = 1, bg = 'white', text = 'OK', border = 3, command =lambda: player_name(entry_label.get(), turn))
discard_name_button = Button(bottom_frame, width = 20, height = 1, bg = 'white', text = 'Play without names', border = 3, command = start_game)
play_again_button = Button(parent_frame, text = 'Play Again..', font = 'Courier, 15',width = 20, fg = 'black', bg = '#FFC33C', command = lambda: play_again(parent_frame))
go_back_button = Button(parent_frame, text = 'Go Back', font = 'Courier, 15', fg = 'red', bg = '#FFC33C', command = catch_menu)

#placing buttons
b1.grid(row = 1, column = 1, columnspan = 1, rowspan = 1)
b4.grid(row = 3, column = 1, columnspan = 1, rowspan = 1)
b7.grid(row = 5, column = 1, columnspan = 1, rowspan = 1)
b2.grid(row = 1, column = 3, columnspan = 1, rowspan = 1)
b5.grid(row = 3, column = 3, columnspan = 1, rowspan = 1)
b8.grid(row = 5, column = 3, columnspan = 1, rowspan = 1)
b3.grid(row = 1, column = 5, columnspan = 1, rowspan = 1)
b6.grid(row = 3, column = 5, columnspan = 1, rowspan = 1)
b9.grid(row = 5, column = 5, columnspan = 1, rowspan = 1)
#placing lines
line_1_1.grid(row = 2,column = 1, columnspan = 5)
line_1_2.grid(row = 4,column = 1, columnspan = 5)
line_2_1.grid(row = 1, column = 2, rowspan = 7)
line_2_2.grid(row = 1, column = 4, rowspan = 7)

#placing parent_frame widgets
mode_label.grid(row = 1, column = 0, pady = 10, sticky = W, columnspan = 3)
player1_label.grid(row = 2, column = 1, padx = 30, pady =30)
player2_label.grid(row = 2, column = 3, sticky = E, padx = 30, pady =30)
main_frame.grid(row = 2, column = 2)
heading_label.grid(row = 0, column =  2)
entry_label.grid(row = 0, column = 0, sticky = W)
entry_label.insert(0, 'Enter player 1\'s name...')
entry_button.grid(row = 0, column = 1, padx = 15)
discard_name_button.grid(row = 0, column = 2)
bottom_frame.grid(row = 3,column = 2, padx = 5, pady = 15)
parent_frame.pack()
root_child.mainloop()