import tkinter as tk
from tkinter import messagebox
import random

# ----------------------------
# GAME LOGIC
# ----------------------------
class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        # Title Label
        tk.Label(
            master,
            text="Guess a number between 1 and 100",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        # Entry Box
        self.guess_entry = tk.Entry(master, font=("Arial", 12))
        self.guess_entry.pack(pady=5)

        # Guess Button
        tk.Button(
            master,
            text="Guess",
            font=("Arial", 12),
            command=self.check_guess
        ).pack(pady=5)

        # Hint Label
        self.hint_label = tk.Label(master, text="", font=("Arial", 12))
        self.hint_label.pack(pady=10)

        # Reset Button
        tk.Button(
            master,
            text="Reset Game",
            font=("Arial", 12),
            command=self.reset_game
        ).pack(pady=5)

    # Function to check guess
    def check_guess(self):
        guess = self.guess_entry.get()

        if not guess.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a number!")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.secret_number:
            self.hint_label.config(text="Too Low! Try Again.")
        elif guess > self.secret_number:
            self.hint_label.config(text="Too High! Try Again.")
        else:
            messagebox.showinfo(
                "Congratulations!",
                f"You guessed it in {self.attempts} attempts!"
            )
            self.reset_game()

    # Reset Game
    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.hint_label.config(text="")
        self.guess_entry.delete(0, tk.END)

# ----------------------------
# MAIN EXECUTION
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
