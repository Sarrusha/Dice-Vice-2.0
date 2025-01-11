import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import random


class DiceRoller:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Vice")

        # Set the window size
        self.root.geometry("1920x1080")

        self.style = ttk.Style()
        self.setup_style()

        self.images = [tk.PhotoImage(file=f"dice_{i+1}.png") for i in range(10)]
        self.difficulty = tk.IntVar(value=6)
        self.specialization = tk.BooleanVar()
        self.dice_bag = tk.StringVar()  # Variable to store dice bag input

        self.create_ui()
        self.last_clicked_button = None  # Track the last clicked button

    def setup_style(self):
        self.style.theme_use('clam')
        self.style.configure('TButton', background='#000',
                             foreground='grey', relief='flat', padding=10)
        self.style.map('TButton', background=[('active', '#111')])
        self.style.configure('TLabel', background='#000', foreground='grey')
        self.style.configure('TCheckbutton', background='#000', foreground='grey')
        self.style.map('TCheckbutton', background=[
                       ('active', '#000')], foreground=[('active', 'grey')])
        self.style.configure('Custom.TFrame', background='#000')
        self.root.configure(background='#000')

    def create_ui(self):
        # Load custom font.
        custom_font = tkFont.Font(family="Times New Roman", size=20)
        large_font = tkFont.Font(family="Times New Roman", size=36)

        # Create frame for difficulty buttons
        difficulty_frame = tk.Frame(self.root, background='#000', bd=0)
        difficulty_frame.grid(row=0, column=0, sticky="w")

        # Create difficulty label
        ttk.Label(difficulty_frame, text="Difficulty:", font=custom_font, background='#000',
                  foreground='grey').grid(row=0, column=0, padx=30, pady=8, sticky='w')

        # Create round buttons for difficulty
        self.difficulty_buttons = []
        for i, num in enumerate(range(2, 11)):
            color = self.get_gradient_color(num)
            canvas = self.create_round_button(difficulty_frame, str(num), color, custom_font, num)
            canvas.grid(row=0, column=i + 1, padx=(0, 5), pady=8)
            self.difficulty_buttons.append(canvas)

        # Create specialization checkbox using ttk Checkbutton with custom style
        chk_btn = ttk.Checkbutton(difficulty_frame, text="Specialization",
                                  variable=self.specialization, style='TCheckbutton')
        chk_btn.grid(row=0, column=len(self.difficulty_buttons) + 1, padx=30, pady=8)

        # Create Dice Bag entry and button combined
        dice_bag_frame = tk.Frame(difficulty_frame, background='#000', bd=0)
        dice_bag_frame.grid(row=0, column=len(self.difficulty_buttons) + 2, padx=10, pady=8)
        dice_bag_entry = ttk.Entry(dice_bag_frame, textvariable=self.dice_bag,
                                   font=custom_font, width=5, justify='center')
        dice_bag_entry.grid(row=0, column=0, padx=7)
        dice_bag_entry.bind("<Return>", lambda event: self.roll_dice_bag()
                            )  # Bind Enter key press to roll_dice_bag
        roll_dice_bag_btn = ttk.Button(dice_bag_frame, text="Dice Bag",
                                       command=self.roll_dice_bag, style='TButton')
        roll_dice_bag_btn.grid(row=0, column=1, padx=7)

        # Create frame for dice buttons
        dice_frame = tk.Frame(self.root, background='#000', bd=0)
        # Adjust pady value for vertical position
        dice_frame.grid(row=1, column=0, sticky="n", pady=8)

        # Create buttons for rolling dice in 2 rows of 5 columns
        self.buttons = []  # List to store button references
        for i in range(2):
            for j in range(5):
                dice_num = i * 5 + j + 1
                # Ensure we don't exceed the number of images available(for now we have 10 images)
                if dice_num <= 10:
                    btn = ttk.Button(
                        dice_frame, image=self.images[dice_num-1], compound="top", style='TButton')
                    btn.config(command=lambda num=dice_num, button=btn: self.roll_dice(num, button))
                    btn.grid(row=i, column=j, padx=7, pady=8)
                    self.buttons.append(btn)

        # Create frame for results
        results_frame = tk.Frame(self.root, background='#000', bd=0)
        # Adjust pady value for vertical position
        results_frame.grid(row=2, column=0, pady=8, sticky="n")

        # Create output Text widget for results
        self.output_text = tk.Text(results_frame, font=large_font, background='#000',
                                   foreground='grey', wrap='word', height=8, width=35)
        self.output_text.grid(row=0, column=0, padx=7)
        self.output_text.insert('1.0', "Results will be shown here")
        self.output_text.config(state=tk.DISABLED)

        # Create Text widget for notes on the right side of the window
        self.notes_text = tk.Text(self.root, font=large_font, background='#000',
                                  foreground='grey', wrap='word', height=16, width=29)
        self.notes_text.grid(row=1, column=1, rowspan=2, sticky="nw", padx=7)
        self.notes_text.insert('1.0', "Notes")

    def create_round_button(self, parent, text, color, font, num):
        canvas = tk.Canvas(parent, width=50, height=50, highlightthickness=0, bg='#000')
        canvas.create_oval(5, 5, 45, 45, fill=color, outline=color)
        canvas.create_text(25, 25, text=text, fill='white', font=font)
        canvas.bind("<Button-1>", lambda e: self.set_difficulty(num, canvas))
        return canvas

    def get_gradient_color(self, value):
        # Define gradient colors from green to blue to purple
        if value <= 5:
            ratio = (value - 2) / 3
            r = int(0 + ratio * (0 - 0))
            g = int(255 + ratio * (0 - 255))
            b = int(0 + ratio * (255 - 0))
        else:
            ratio = (value - 5) / 5
            r = int(0 + ratio * (128 - 0))
            g = int(0 + ratio * (0 - 0))
            b = int(255 + ratio * (128 - 255))
        return f'#{r:02x}{g:02x}{b:02x}'

    def set_difficulty(self, num, canvas):
        self.difficulty.set(num)
        for btn in self.difficulty_buttons:
            btn.itemconfig(1, outline=btn['background'])
        canvas.itemconfig(1, outline='grey', width=2)

    def roll_dice(self, num_dice, button):
        # Reset border color of the previously clicked button. Maybe I'll remove this.
        if self.last_clicked_button:
            self.last_clicked_button.config(style='TButton')

        # Roll the dice!!! yay!!!(don't cheat lol)
        rolls = [random.randint(1, 10) for _ in range(num_dice)]
        successes = 0
        ten_count = 0

        for roll in rolls:
            if roll >= self.difficulty.get():
                successes += 1
            if roll == 10:
                ten_count += 1
            if roll == 1:
                successes -= 1

        if self.specialization.get():
            successes += ten_count

        # Prepare results text
        botch_text = " Botch!!" if successes < 0 else ""
        rolls_str = ", ".join(map(str, rolls))
        results_text = f"{successes} successes, of which {ten_count} ten(s){botch_text}\nResults: {rolls_str}"

        # Update output Text widget
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert('1.0', results_text)
        self.output_text.config(state=tk.DISABLED)

    def roll_dice_bag(self):
        try:
            num_dice = int(self.dice_bag.get())
            if num_dice > 0:
                self.roll_dice(num_dice, None)
            else:
                self.output_text.config(state=tk.NORMAL)
                self.output_text.delete('1.0', tk.END)
                self.output_text.insert('1.0', "Please enter a valid number of dice.")
                self.output_text.config(state=tk.DISABLED)
        except ValueError:
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert('1.0', "Please enter a valid number of dice.")
            self.output_text.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRoller(root)
    root.mainloop()
