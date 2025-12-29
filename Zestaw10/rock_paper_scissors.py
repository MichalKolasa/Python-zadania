import tkinter as tk
import random

class Application(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Rock Paper Scissors")
        self.master.geometry("800x300")

        self.grid(sticky="nsew")

        # stan
        self.player_choice = tk.StringVar(value="—")
        self.computer_choice = tk.StringVar(value="—")
        self.result_var = tk.StringVar(value="-")

        # układ
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=1)

        self.create_frames()
        self.create_widgets()

    # kontener na widgety
    def create_frames(self):
        self.top_frame = tk.Frame(self)
        self.top_frame.grid(row=0, column=0, sticky="nsew", pady=20)

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.grid(row=1, column=0, pady=30)

        for i in range(3):
            self.top_frame.columnconfigure(i, weight=1)

        for i in range(3):
            self.bottom_frame.columnconfigure(i, weight=1)

    # utworzenie widgetów
    def create_widgets(self):
        # gracz
        player_title = tk.Label(
            self.top_frame, text="Your choice:", font=("Calibri", 20)
        )
        player_title.grid(row=0, column=0, pady=(0, 5))

        player_value = tk.Label(
            self.top_frame,
            textvariable=self.player_choice,
            font=("Arial", 28, "bold")
        )
        player_value.grid(row=1, column=0)

        # wynik
        result_title = tk.Label(
            self.top_frame, text="Result:", font=("Calibri", 20)
        )
        result_title.grid(row=0, column=1, pady=(0, 5))

        result_value = tk.Label(
            self.top_frame,
            textvariable=self.result_var,
            font=("Arial", 26, "bold")
        )
        result_value.grid(row=1, column=1)

        # komputer
        computer_title = tk.Label(
            self.top_frame, text="Computer choice:", font=("Calibri", 20)
        )
        computer_title.grid(row=0, column=2, pady=(0, 5))

        computer_value = tk.Label(
            self.top_frame,
            textvariable=self.computer_choice,
            font=("Arial", 28, "bold")
        )
        computer_value.grid(row=1, column=2)

        self.create_buttons()

    # utworzenie przycisków
    def create_buttons(self):
        tk.Button(
            self.bottom_frame, text="ROCK", width=12, height=3,
            command=lambda: self.play("ROCK")
        ).grid(row=0, column=0, padx=50)

        tk.Button(
            self.bottom_frame, text="PAPER", width=12, height=3,
            command=lambda: self.play("PAPER")
        ).grid(row=0, column=1, padx=50)

        tk.Button(
            self.bottom_frame, text="SCISSORS", width=12, height=3,
            command=lambda: self.play("SCISSORS")
        ).grid(row=0, column=2, padx=50)

    # logika gry
    def get_result(self, player, computer):
        if player == computer:
            return "DRAW 🤝"
        if (
            (player == "ROCK" and computer == "SCISSORS") or
            (player == "PAPER" and computer == "ROCK") or
            (player == "SCISSORS" and computer == "PAPER")
        ):
            return "WIN 🎉"
        return "LOSE ❌"

    def play(self, choice):
        computer = random.choice(["ROCK", "PAPER", "SCISSORS"])

        self.player_choice.set(choice)
        self.computer_choice.set(computer)
        self.result_var.set(self.get_result(choice, computer))


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
