# Dice-Vice-2.0
Dice roller for World of Darkness, Vampire rpg (d10)

# DICE VICE


https://github.com/user-attachments/assets/e601868c-b991-4f3e-930b-68add972c954



#### Description:

Welcome to DICE VICE, an easy dice roller designed specifically for Vampire, Werewolf, and other World of Darkness games!

It's been built with lots of love by a gamer, me, for other gamers, hopefully YOU.
First of all, it's totally free, for everybody.

##Dices
We roll 10-sided dice here, if you’re looking for different dice types like 4, 6, 8, 12, or 20 sides, this isn't the tool for you.
I know, even I love Dungeons and Dragons, but this is only for World of Darkness. Sorry adventurers.

I created this project hoping to spread the love for this beautiful game.
Feel free to use it as a digital dice alternative, but do consider supporting the official materials by purchasing handbooks and original source books if you can.

#Why?
Sometimes, I just forgot my dices at home, but I have my loyal laptop! So this is for these times when I have one but not the others, or when I want to help new players without dices when we play online.
Anyway, it is a good tools for convenience.

#What does the folders contain?
It’s really easy, in the main folder there are pictures and the program.
The program is written in python, for now it is a requirement to have python installed to be able to open it, but I want to convert it in the future in a .exe so that also non developer can use it.
For now, everything to be able to use it is in the folders, so developer feel free to look the code and use it!!!
The pictures are of my favorite dices. I took them personally, cut the background with Gimp and made them of a reasonable size.
#How to use it?
Just click on the .py, and a new window shall appear.
To select difficulty for the rolls, click on the colored circles. The default difficulty, is 6.
Then, insert the number of dices if you have more than 10 dices (works even under 10), push the dice bag button or push also enter onto the keyboard to roll. (the enter function used as the button was tricky)
Otherwise, just click on one of the 10 dices, and voilà! In the left bottom the result of the roll will appear, and the successes will be directly visualized, without the need to calculate it manually.
The system consider the 1 as a critical failure, removing 1 success from the successes pool, and also 10 as double successes IF the corresponding tick is selected in the middle upper of the app.

In case of a Botch (only if the total number of successes is negative), the results area will present the word “Botch” to signal that the action failed.

#Structure of the program:
I used Python and tkinter for the GUI.

Methods I employed:
setup_style(self): Configures the style for the tkinter widgets.
create_ui(self): Creates the user interface including frames, buttons, and text widgets.
create_round_button(self, parent, text, color, font, num): Creates a round button for the UI.
get_gradient_color(self, value): Generates a gradient color for buttons based on the value.
set_difficulty(self, num, canvas): Sets the difficulty level and updates button styles.
roll_dice(self, num_dice, button): Rolls the dice and updates the result display.
roll_dice_bag(self): Rolls a number of dice specified by the lucky user of my fabulous final program. (hope) This function is necessary when we rolls A LOT of dices.

Main Functionality:
As always, it creates the main application window (root), runs the tkinter main loop to keep the application running.

UI Elements to keep everything in the right place:
Frames: difficulty_frame, dice_bag_frame, dice_frame, results_frame
Widgets: Labels, Buttons, Text Widgets, Entries, Checkbuttons
Styles: Configured for various widgets to match the dark custom theme. I tried to fit everything nicely in the window.

#Future projects:
I hope to be able to expand this project when I have the time, so just stay tuned for a better UI, an history of the past rolls or more!

Thanks for your attention!



This program is an independent creation by a fan and doesn’t represent any official connection to White Wolf Inc., the creators behind World of Darkness games. Keep in mind, the copyrights on World of Darkness, White Wolf, the logo, and related symbols belong to White Wolf Inc.

Tags: RPG, White Wolf, World of Darkness, Vampire the Masquerade, Werewolf the Apocalypse
 
