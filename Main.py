#submitted April 22

from tkinter import *
import time
from random import randint
from PIL import Image, ImageTk
from threading import *
import winsound
import pygame
from pygame import mixer
import sys, os

#initialize pygame
pygame.init()

again = True

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

while again == True: 
    
    #[---------------------------------------------------Defining Functions-------------------------------------------------------]
    
    # destroy after getting player's name input
    def get_name ():
        global player_name
        #play choose_sound
        winsound.PlaySound(resource_path('choose_sound.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)
        player_name = name.get()
        root.destroy() #close first canvas


    #if the player chose fgyy
    def bg_fgyy():
        
        global root
        
        #play choose_sound
        winsound.PlaySound(resource_path('choose_sound.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)
        
        #destroy the precious canvas (choosing screen)
        root.destroy()
        
        global bg_image_choice
        #set the background as fgyy
        bg_image_choice = 1
       
        
    #if the player chose tzl
    def bg_tzl():
        
        global root
        
        #play choose_sound
        winsound.PlaySound(resource_path('choose_sound.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)
        
        #destroy the precious canvas (choosing screen)
        root.destroy()
        
        global bg_image_choice
        #set the background as tzl
        bg_image_choice = 2
            

    #if the player chose wqsy
    def bg_wqsy():
        
        global root
        
        #play choose_sound
        winsound.PlaySound(resource_path('choose_sound.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)
        
        #destroy the precious canvas (choosing screen)
        root.destroy()
        
        global bg_image_choice
        #set the background as fgyy
        bg_image_choice = 3



    #if the player chooses red laser
    def red_laser():
        
        global root
        
        #play choose_sound
        winsound.PlaySound(resource_path('choose_sound.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)
        
        #destroy the precious canvas (choosing screen)
        root.destroy()
        
        global laser_choice
        #set the laser as red
        laser_choice = 1


    #if the player chooses blue laser
    def blue_laser():
        
        global root
        
        #play choose_sound
        winsound.PlaySound(resource_path('choose_sound.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)
        
        #destroy the precious canvas (choosing screen)
        root.destroy()
        
        global laser_choice
        #set the laser as blue
        laser_choice = 2


    #if the player chooses yellow laser
    def yellow_laser():
        
        global root
        
        #play choose_sound
        winsound.PlaySound(resource_path('choose_sound.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)
        
        #destroy the precious canvas (choosing screen)
        root.destroy()
        
        global laser_choice
        #set the laser as yellow
        laser_choice = 3


    def got_it():
        
        global root
        
        #play choose_sound
        winsound.PlaySound(resource_path('choose_sound.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)

        #destroy the precious canvas (instruction screen)
        root.destroy()

        
    #this functions starts a countdown before the game actually starts
    def start_countdown():
        #countdown 3-2-1 animation
        #sound effects
        winsound.PlaySound(resource_path("Tick"), winsound.SND_ASYNC | winsound.SND_ALIAS ) 
        #show each number only about a second
        for a in range(60):
            canvas.itemconfigure(count3, state = NORMAL) 
            root.update()
            time.sleep(0.01)  
        winsound.PlaySound(resource_path("Tick"), winsound.SND_ASYNC | winsound.SND_ALIAS )
        for b in range(60):
            canvas.itemconfigure(count3, state = HIDDEN)
            canvas.itemconfigure(count2, state = NORMAL) 
            root.update()
            time.sleep(0.01)  
        winsound.PlaySound(resource_path("Tick"), winsound.SND_ASYNC | winsound.SND_ALIAS )
        for c in range(60):
            canvas.itemconfigure(count2, state = HIDDEN)
            canvas.itemconfigure(count1, state = NORMAL)   
            root.update()
            time.sleep(0.01) 
        
        #delete them after
        canvas.delete(count3)
        canvas.delete(count2)
        canvas.delete(count1)                      
        
        canvas.update()


        
    #make the fruits appear on the screen
    def create_fruits():
        
        global fruits_list
        
        if game == True:

            #choose random fruits
            which_fruit = randint(1,8)
            this_fruit = ImageTk.PhotoImage(Image.open(resource_path(fruit_dic[which_fruit])))
            
            #randomly generate which colum (four in total) the fruits will be
            choose_position = randint (1,4)
            
            x_position = x_positions_dic[choose_position]  # choose the position from dict

            my_photo = canvas.create_image(x_position, 0, image = this_fruit)

            #append it to the list(image_if, y volocity, image)
            fruits_list.append([my_photo, randint(8,15), this_fruit])

            #repeatedly generate fruit images every 0.25 second (change the density of the fruit)
            root.after(250,create_fruits)
        
        
        
    #make the bombs appear on the screen
    def create_bombs():
        
        global bomb_list
        
        if game == True:
            
            #randomly generate which colum (four in total) the fruits will be
            choose_position = randint (1,4)
            
            x_position = x_positions_dic[choose_position]  # choose the position from dict

            bomb_photo = canvas.create_image(x_position, 0, image = bomb_image)

            #append it to the list(image_if, y volocity, image)
            bomb_list.append([bomb_photo, randint(8,15), bomb_image])

            #repeatedly generate fruit images every 0.25 second (change the density of the fruit)
            root.after(1500,create_bombs)
        
        

    def move_fruits():
        
        global score, hold, root, this_splash, game, win
        
        #iterate through the fruit list
        for fruit in fruits_list:
            #call the move function, move the fruit
            canvas.move(fruit[0], 0, fruit[1])
            
            #get the coordinates of the fruits and check if thry are in the range of the laser when which is pressed and if they are out of the canvas
            if 550 <= (canvas.coords(fruit[0]))[1] <= 650 and hold == True:
                
                #play score sound
                #winsound.PlaySound('score_sound.wav', winsound.SND_ASYNC | winsound.SND_FILENAME)
                
                canvas.delete(fruit[0])
                fruits_list.remove(fruit)
                score += 1
                #change the displaying score
                canvas.itemconfigure(score_display, text = score) 
                root.update()
                
                #occasionally show the splash effects
                splash_prob = randint (1,10)
                if splash_prob == 1:
                    #choose random splash color
                    which_splash = randint(1,4)
                    this_splash = ImageTk.PhotoImage(Image.open(resource_path(splash_dic[which_splash])))
                    
                    #choose where the splash is placed
                    splash_x = randint(0,800)
                    splash_y = randint(200,1000)
                    canvas.create_image(splash_x, splash_y, image = this_splash)
                    
                elif score == 100:
                    #cancel the laser effect even though the user is still holding the mouse to let them know that the game is over
                    hold = False
                    
                    #turn off create fruits and bombs function
                    game = False
                    
                    mixer.music.stop()
                    
                    #play the win quick sound
                    winsound.PlaySound(resource_path('win_quick.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)
                    
                    #delete everything on the canvas
                    canvas.delete(ALL)
                    # add the chosen image to the bg
                    canvas.create_image(0,0, image = bg_image, anchor = 'nw')
                    #display text GAME OVER!
                    canvas.create_text(400,600, text = "GAME OVER!", font = ("rockwell", 50), fill = "white")
                    root.update()
                    #let the text last 3 seconds
                    time.sleep(3)
                    #kill the root
                    root.destroy()
                    
                    win = True
                    
            #cancel fruit out from canvs if it is outside of boarder
            elif (canvas.coords(fruit[0]))[1] >= 1300:
                canvas.delete(fruit[0])
                fruits_list.remove(fruit)

        root.after(10, move_fruits)  # calls the move_fruits after every 0.01 seconds (change the speed of the fruit)
        
        
        
    def move_bombs():
        
        global lives, root, hold, game, win
        
        #iterate through the bomb list
        for bomb in bomb_list:
            #call the move function, move the bomb
            canvas.move(bomb[0], 0, bomb[1])
            #get the coordinates of the bombs and check if thry are in the range of the laser when which is pressed and if they are out of the canvas
            if 550 <= (canvas.coords(bomb[0]))[1] <= 650 and hold == True:
                #play explosion sound
                winsound.PlaySound(resource_path('bomb_sound.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)
                
                lives -= 1
                
                #show the exlosion animation
                for gif in explosion_giflist:
                    #place each frame on the canvas, x position depends on the bomb position
                    explosion_photo = canvas.create_image((canvas.coords(bomb[0]))[0], 600, image=gif)
                    canvas.update()
                    #place every 0.01 second
                    time.sleep(0.05)
                    #append displayed images to a list and delete them later in case the canvas freezes.
                    explosion_finished.append(explosion_photo)
                    canvas.delete(explosion_finished[0])
                    explosion_finished.remove(explosion_finished[0])
                #remove the bomb from screen
                canvas.delete(bomb[0])
                bomb_list.remove(bomb)
                
                #minus 1 life
                if len(heart_list) > 1:
                    canvas.delete(heart_list[0])
                    heart_list.remove(heart_list[0])
                else:
                    #cancel the laser effect even though the user is still holding the mouse to let them know that the game is over
                    hold = False
                    
                    game = False
                    
                    mixer.music.stop()
                    
                    #remove the last heart
                    canvas.delete(heart_list[0])
                    heart_list.remove(heart_list[0])
                    
                    #play the win quick sound
                    winsound.PlaySound(resource_path('lost_quick.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)
                    
                    #delete everything on the canvas
                    canvas.delete(ALL)
                    
                    # add the chosen image to the bg
                    canvas.create_image(0,0, image = bg_image, anchor = 'nw')
                    #display text GAME OVER!
                    canvas.create_text(400,600, text = "GAME OVER!", font = ("rockwell", 50), fill = "white")
                    root.update()
                    #let the text last 4 seconds
                    time.sleep(4)
                    #kill the root
                    root.destroy()
                    
                    win = False
                
                #remove the bomb if it goes out side of the boarder
            elif (canvas.coords(bomb[0]))[1] >= 1300:
                canvas.delete(bomb[0])
                bomb_list.remove(bomb)

        root.after(10, move_bombs)  # calls the move_bombs after every 0.01 seconds (change the speed of the bomb)
        
        
        
    #show the laser animation while clicking
    def laser(event = None):
        
        global hold
        hold = True
        
        #play laser shot sound
        winsound.PlaySound(resource_path('laser_shot.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)
        
        # loop through the gif image objects for a while
        for k in range(0, 1000):
            for gif in laser_giflist:
                #place each frame on the canvas
                laser_photo = canvas.create_image(400, 600, image=gif)
                canvas.update()
                #place every 0.01 second
                time.sleep(0.01)
                
                #append displayed images to a list and delete them later in case the canvas freezes.
                laser_finished.append(laser_photo)
                canvas.delete(laser_finished[0])
                laser_finished.remove(laser_finished[0])
                
                if hold == False:
                    return
                   
        #repeat this function,move the laer every 0.1 seconds      
        root.after(10, laser)
        
              
              
    def cancel_laser(event = None):
        global hold
        hold = False
        
        
    #if the user chooses yes    
    def again_yes():
        
        global root, again
        
        #play choose_sound
        winsound.PlaySound(resource_path('choose_sound.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)
        
        again = True
        root.destroy()
        
        
    #if the user chooses no
    def again_no():
        
        global root, again
        
        #play choose_sound
        winsound.PlaySound(resource_path('choose_sound.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)
        
        again = False
        root.destroy()
        

    def last_screen():
        
        global root
        #thanks for playing screen
        root = Tk()

        last = Canvas(root, height = 1200, width = 800, bg = "black")
        last.pack()
        
        report_screen_bg = PhotoImage(file = resource_path("report_screen_bg.png"))
        last.create_image(0,0, image = report_screen_bg, anchor = NW)
        
        last.create_text(400, 600, text = "Thanks For Playing!",font = ("rockwell", 30), fill = "white")
        
        time.sleep(3)
        
        root.destroy()
        
        mainloop()

    
    #play intro sound
    mixer.music.load('intro.wav')
    mixer.music.play()
    
#[---------------------------------------------------Assigning Variables-------------------------------------------------------]
    
    heart_list = []

    fruits_list = []

    bomb_list = []

    fruit_coords = []

    bomb_coords = []

    explosion_list = ["explosion_1.gif","explosion_2.gif","explosion_3.gif","explosion_4.gif","explosion_5.gif","explosion_6.gif","explosion_7.gif",]

    explosion_giflist = []

    explosion_finished = []

    red_laser_list = ["laser_red_1.png","laser_red_2.png","laser_red_3.png","laser_red_4.png"]

    yellow_laser_list = ["laser_yellow_1.png","laser_yellow_2.png","laser_yellow_3.png","laser_yellow_4.png"]

    blue_laser_list = ["laser_blue_1.png","laser_blue_2.png","laser_blue_3.png","laser_blue_4.png"]

    laser_giflist = []

    laser_finished = []

    x_positions_dic = {1: 160, 2: 287.5, 3: 462.5, 4:637.5}

    #import the fruit images
    fruit_dic = {
        1: r"watermelon.png" ,
        2: r"apple.png" ,
        3: r"pear.png",
        4: r"blueberry.png",
        5: r"banana.png",
        6: r"cherry.png",
        7: r"mango.png",
        8: r"lemon.png"
        } # images path

    #import the splash images
    splash_dic = {
        1: r"yellow_splash.png",
        2: r"red_splash.png",
        3: r"green_splash.png",
        4: r"blue_splash.png"
        }

    #import guns image
    guns_dic = {
        1: r"red_gun.png",
        2: r"yellow_gun.png",
        3: r"blue_gun.png"
        }

    hold = False

    game = True

    again = True

    score = 0

    lives = 3


#[---------------------------------------------------Starting the Game-------------------------------------------------------]

    #start the first screen
    root = Tk ()

    intro_screen = Canvas(root, height = 1200, width = 800, bg = 'black')

    #create the background
    first_canvas = PhotoImage(file = resource_path("first_bg.png"))
    intro_screen.create_image(0,0, image = first_canvas, anchor = 'nw')
    intro_screen.pack()

    #trigger get_name(), continue to the next canvas
    go_button = PhotoImage(file = resource_path("go_button.png"))

    #intro_screen.create_image(600, 650, image=go_button)
    go = Button (root,image = go_button, width = 50, height = 50, command = get_name, cursor = 'tcross', activeforeground = 'cyan')
    intro_screen.create_window (550, 1000, window = go)
    intro_screen.pack()

    #name entry box
    name = StringVar()
    name_entry = Entry(root, textvariable = name)
    intro_entry = intro_screen.create_window (370, 1000, window = name_entry, height = 50, width = 300)
    intro_screen.pack()

    intro_screen.create_text (400, 930, text = "Please Enter Your Name Here:", font = ("rockwell", 15), fill = "white")

    mainloop()





    #start the second screen (background choosing screen)
    root = Tk()

    choosing_screen = Canvas(root, height = 1200, width = 800, bg = 'white')
    choosing_screen.pack()

    #import background image
    second_canvas = PhotoImage (file = resource_path("second_canvas.png"))

    #import the three square images
    fgyy_square = PhotoImage(file = resource_path("fgyy_square.png"))
    tzl_square = PhotoImage(file = resource_path("tzl_square.png"))
    wqsy_square = PhotoImage(file = resource_path("wqsy_square.png"))

    #place background
    choosing_screen.create_image(0,0, image = second_canvas, anchor = 'nw')

    #create the first button
    choose_fgyy = Button (root, image = fgyy_square,width=200,height=200, command = bg_fgyy, cursor = 'tcross')
    choosing_screen.create_window(400,250, window = choose_fgyy)
    choosing_screen.pack()

    #create the second button
    choose_tzl = Button (root, image = tzl_square,width=200,height=200, command = bg_tzl, cursor = 'tcross')
    choosing_screen.create_window(400,500, window = choose_tzl)
    choosing_screen.pack()

    #create the third button
    choose_wqsy = Button (root, image = wqsy_square,width=200,height=200, command = bg_wqsy, cursor = 'tcross')
    choosing_screen.create_window(400,750, window = choose_wqsy)
    choosing_screen.pack()

    #create the black rectangle
    choosing_screen.create_rectangle (0,950, 800, 1050, fill = 'black')

    #display the chosing background text
    choosing_screen.create_text (400,1000, text = "Choose Your Background!", font = ("rockwell", 30), fill = "white")

    mainloop()




    #start the third screen (gun choosing screen)
    root = Tk()

    choosing_laser = Canvas(root, height = 1200, width = 800, bg = 'white')
    choosing_laser.pack()

    #import background image
    third_canvas = PhotoImage (file = resource_path("third_canvas.png"))

    #import the three square images
    red_square = PhotoImage(file = resource_path("red_square.png"))
    blue_square = PhotoImage(file = resource_path("blue_square.png"))
    yellow_square = PhotoImage(file = resource_path("yellow_square.png"))

    #place background
    choosing_laser.create_image(0,0, image = third_canvas, anchor = 'nw')

    #create the first button
    choose_red = Button (root, image = red_square,width=200,height=200, command = red_laser, cursor = 'tcross')
    choosing_laser.create_window(400,250, window = choose_red)
    choosing_laser.pack()

    #create the second button
    choose_blue = Button (root, image = blue_square,width=200,height=200, command = blue_laser, cursor = 'tcross')
    choosing_laser.create_window(400,500, window = choose_blue)
    choosing_laser.pack()

    #create the third button
    choose_yellow = Button (root, image = yellow_square,width=200,height=200, command = yellow_laser, cursor = 'tcross')
    choosing_laser.create_window(400,750, window = choose_yellow)
    choosing_laser.pack()

    #create the black rectangle
    choosing_laser.create_rectangle (0,950, 800, 1050, fill = 'black')

    #display the chosing laser text
    choosing_laser.create_text (400,1000, text = "Choose Your Laser!", font = ("rockwell", 30), fill = "white")

    mainloop()




    #create instruction screen
    root = Tk()

    ins_screen = Canvas(root, height = 1200, width = 800, bg = 'black')
    ins_screen.pack()

    #import and put bg
    ins_bg = PhotoImage(file = resource_path("ins_bg.png"))
    ins_screen.create_image(0, 0, image = ins_bg, anchor = NW)

    #place the text
    title = ins_screen.create_text(270, 250, text = "Instruction:", font = ("rockwell", 20), fill = "white")
    ins = ins_screen.create_text(410, 650, text = "1. Hold left mouse button to trigger the \n\n    laser, release it to stop the laser\n\n\n2. Your goal is to get as many fruits as\n\n    possible, but to avoid those annoying\n\n    bombs. Whenever your laser cuts a fruit,\n\n    you will gain one point. The score is\n\n    shown on the top left corner.\n\n    You will win if your score reaches 100\n\n\n3. Remember! You only have three lives,\n\n    everytime you explode a bomb,\n\n    your will loose one life, until none \n\n    of them left\n\n\n4. Enjoy and have FUN!", font = ("rockwell", 11), fill = "white")
    #warning = ins_screen.create_text(400, 1080, text = "***Please manually close this page if the button is not working***", font = ("rockwell", 10), fill = "black")
    
    #create the button
    got_it = Button(root, command = got_it, cursor = 'tcross', text = 'GOT IT! -->')
    ins_screen.create_window(590,1000, window = got_it)
    ins_screen.pack()

    mainloop()





    #create game area

    #stop the sound
    mixer.music.stop()

    root = Tk ()

    #Cursor shape
    root.configure(cursor = "target")

    canvas = Canvas (root, height = 1200, width = 800, bg = 'black')
    canvas.pack()

    #import the bomb image
    bomb_image = PhotoImage(file = resource_path("bomb.png"))

    #import heart photo
    heart = PhotoImage(file = resource_path('heart.png'))

    #create a list of explosion images objects
    for image_file in explosion_list:
        explosion_photo = PhotoImage(file = resource_path(image_file))
        explosion_giflist.append(explosion_photo)

    #which background is chosen by the user
    if bg_image_choice == 1:
        bg_image = PhotoImage(file = resource_path("fgyy_canvas.png"))
    elif bg_image_choice == 2:
        bg_image = PhotoImage(file = resource_path("tzl_canvas.png"))
    elif bg_image_choice == 3:
        bg_image = PhotoImage(file = resource_path("wqsy_canvas.png"))

    # add the chosen image to the bg
    canvas.create_image(0,0, image = bg_image, anchor = 'nw')

    #dicide which color is the laser
    if laser_choice == 1:
        laser_list = red_laser_list
        
        #import the gun images
        red_gun = PhotoImage(file = resource_path("red_gun.png"))
        red_gun2 = PhotoImage(file = resource_path("red_gun2.png"))
        #place the gun image
        canvas.create_image (100,600, image = red_gun)
        canvas.create_image (700,600, image = red_gun2)

    elif laser_choice == 2:
        laser_list = blue_laser_list
        
        #import the gun images
        blue_gun = PhotoImage(file = resource_path("blue_gun.png"))
        blue_gun2 = PhotoImage(file = resource_path("blue_gun2.png"))
        #place the gun image
        canvas.create_image (100,600, image = blue_gun)
        canvas.create_image (700,600, image = blue_gun2)
        
    elif laser_choice == 3:
        laser_list = yellow_laser_list
        
        #import the gun images
        yellow_gun = PhotoImage(file = resource_path("yellow_gun.png"))
        yellow_gun2 = PhotoImage(file = resource_path("yellow_gun2.png"))
        #place the gun image
        canvas.create_image (100,600, image = yellow_gun)
        canvas.create_image (700,600, image = yellow_gun2)

    #append the PhotoImage to a gif list
    for imagefile in laser_list:
        laser_photo = PhotoImage(file = resource_path(imagefile))
        laser_giflist.append(laser_photo)

    #add the score text
    canvas.create_text(0,0, text = "Score:", font = ("rockwell", 40), fill = "white", anchor = NW)

    #add the actual score
    score_display = canvas.create_text(100,150, text = score, font = ("rockwell", 40), fill = "white")

    #Start time countdown, create and hide the numbers
    count3 = canvas.create_text(400,600, text = "3", font = ("rockwell", 100), fill = "white", state = HIDDEN)
    count2 = canvas.create_text(400,600, text = "2", font = ("rockwell", 100), fill = "white", state = HIDDEN)
    count1 = canvas.create_text(400,600, text = "1", font = ("rockwell", 100), fill = "white", state = HIDDEN)

    #create the heart images
    heart1 = canvas.create_image (800,150, image = heart, anchor = NE)
    heart_list.append(heart1)
    heart2 = canvas.create_image (800,75, image = heart, anchor = NE)
    heart_list.append(heart2)
    heart3 = canvas.create_image (800,0, image = heart, anchor = NE)
    heart_list.append(heart3)

    start_countdown()

    #import theme sound
    mixer.music.load(resource_path('game_sound.wav'))
    mixer.music.play(-1)

    create_fruits()

    create_bombs()

    move_fruits()

    move_bombs()

    #if the user presses the left mouse button, the laser effect is trigured
    root.bind("<Button-1>", laser)

    #if the user releases the left mouse button, the laser effect is canceled
    root.bind("<ButtonRelease-1>",cancel_laser)

    mainloop()






    if win == True:


        #win report screen
        root = Tk()

        #play the music
        winsound.PlaySound(resource_path('win_canvas.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)

        win_report_screen = Canvas(root, height = 1200, width = 800, bg = "black")
        win_report_screen.pack()

        report_screen_bg = PhotoImage(file = resource_path("report_screen_bg.png"))
        win_report_screen.create_image(0,0, image = report_screen_bg, anchor = NW)

        #import heart photo
        heart = PhotoImage(file = resource_path('heart.png'))

        #display the YOU WON! text
        win_report_screen.create_text(400, 300, text = "YOU WON,", font = ("rockwell", 40), fill = "white")

        #display player name
        win_report_screen.create_text(400, 420, text = player_name+"!", font = ("rockwell", 60), fill = "white")

        #display_lives
        win_report_screen.create_text(400, 600, text = "You Have "+str(lives)+" Live(s) Left!", font = ("rockwell", 30), fill = "white")

        #display the hearts left
        if lives == 3:
            win_report_screen.create_image(400, 700, image = heart)
            win_report_screen.create_image(320, 700, image = heart)
            win_report_screen.create_image(475, 700, image = heart)
            
        elif lives == 2:
            win_report_screen.create_image(350, 700, image = heart)
            win_report_screen.create_image(450, 700, image = heart)
            
        elif lives == 1:
            win_report_screen.create_image(400, 700, image = heart)

        win_report_screen.create_text(400, 800, text = "Do You Want to Play Again?", font = ("rockwell", 25), fill = "white")
        
        #import the button images
        yes_image = PhotoImage (file = resource_path("yes.png"))
        no_image = PhotoImage (file = resource_path("no.png"))
        
        #the YES button
        yes = Button (root,image = yes_image, width = 100, height = 100, command = again_yes, cursor = 'tcross', activeforeground = 'cyan')
        win_report_screen.create_window (300, 1000, window = yes)
        win_report_screen.pack()
        
        #the NO button
        no = Button (root,image = no_image, width = 100, height = 100, command = again_no, cursor = 'tcross', activeforeground = 'cyan')
        win_report_screen.create_window (500, 1000, window = no)
        win_report_screen.pack()

        mainloop()





    if win == False:


        #loose report screen
        root = Tk()

        #play the music
        winsound.PlaySound(resource_path('loose_canvas.wav'), winsound.SND_ASYNC | winsound.SND_FILENAME)

        win_report_screen = Canvas(root, height = 1200, width = 800, bg = "black")
        win_report_screen.pack()

        report_screen_bg = PhotoImage(file = resource_path("report_screen_bg.png"))
        win_report_screen.create_image(0,0, image = report_screen_bg, anchor = NW)

        #display the YOU LOST! text
        win_report_screen.create_text(400, 300, text = "YOU LOST,", font = ("rockwell", 40), fill = "white")

        #display player name
        win_report_screen.create_text(400, 420, text = player_name+"!", font = ("rockwell", 60), fill = "white")

        win_report_screen.create_text(400, 630, text = "You Scored "+str(score)+" Points!", font = ("rockwell", 30), fill = "white")
        
        win_report_screen.create_text(400, 800, text = "Do You Want to Play Again?", font = ("rockwell", 25), fill = "white")
        
        #import the button images
        yes_image = PhotoImage (file = resource_path("yes.png"))
        no_image = PhotoImage (file = resource_path("no.png"))
        
        #the YES button
        yes = Button (root,image = yes_image, width = 100, height = 100, command = again_yes, cursor = 'tcross', activeforeground = 'cyan')
        win_report_screen.create_window (300, 1000, window = yes)
        win_report_screen.pack()
        
        #the NO button
        no = Button (root,image = no_image, width = 100, height = 100, command = again_no, cursor = 'tcross', activeforeground = 'cyan')
        win_report_screen.create_window (500, 1000, window = no)
        win_report_screen.pack()

        mainloop()
        
    
        

