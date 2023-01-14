import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Tic-Tac-Toe")
root.configure(background="black")
root.geometry("588x588")

player = True

empty = tk.PhotoImage(file="images/empty.png")
player_1 = tk.PhotoImage(file='images/user_1.png')
player_2 = tk.PhotoImage(file='images/user_2.png')

tiles = []

def set_image(button):
    global player, player_1, player_2, tiles
    
    if player:
        img, color, user = player_1, "#0086f4", 'player 1'
    else:
        img, color, user = player_2, "#e94141", 'player 2'
    
    if tiles[button.x][button.y]: return print('change not allowed.')
    
    tiles[button.x][button.y] = user
    
    button['image']=img
    button.config(bg=color)
    
    player = not player
    
    game_over = False
    
    if result := is_players_win(user):
        if result == 'WIN':
            messagebox.showinfo(title='Game Over!', message=f"{user} is winner.")
            game_over=True
        if result == 'DRAW':
            game_over=True
            messagebox.showinfo(title='Game Over!', message="Draw")
    
        if game_over:
            if messagebox.askyesno(title='Game Over!', message='Retry'):
                draw_map()
            else:
                root.destroy()
            
        

def is_players_win(user):
    global tiles
    
    # Row
    for tile in tiles:
        if len(list(filter(lambda til: til == user, tile))) == 3:
            return 'WIN'
    
    # Column
    for i in range(3):
        _tiles = [tiles[n][i] for n in range(3)]
        if len(list(filter(lambda til: til == user, _tiles))) == 3:
            return 'WIN'

    if len(list(filter(lambda til: til == user, [tiles[i][i] for i in range(3)]))) == 3:
        return 'WIN'
    
    if len(list(filter(lambda til: til == user, [tiles[i][2-i] for i in range(3)]))) == 3:
        return 'WIN'

    if not list(filter(lambda tile: 0 in tile, tiles)):
        return 'DRAW'

def draw_map():
    global tiles
    
    tiles = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    
    for x in range(3):
        for y in range(3):
            button = tk.Button(master=root, image=empty, bg="black", borderwidth=1)
            button.x, button.y = x, y
            button['command'] = lambda arg=button: set_image(arg)
            button.grid(row=x, column=y)
        
    

draw_map()
root.mainloop()