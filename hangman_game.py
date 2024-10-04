import random
import tkinter as tk
from tkinter import messagebox


class Hangman:

  
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")      
        self.words = ["python", "hangman", "tkinter", "programming", "challenge"]
        self.secret_word = random.choice(self.words)
        self.guesses = []
        self.max_attempts = 6
        self.attempts = 0
        self.create_widgets()

  
    def create_widgets(self):
        self.word_label = tk.Label(self.master, text=self.get_display_word(), font=("Helvetica", 24))
        self.word_label.pack(pady=20)
        self.guess_entry = tk.Entry(self.master, font=("Helvetica", 18))
        self.guess_entry.pack(pady=10)
        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=10)
        self.attempts_label = tk.Label(self.master, text=f"Attempts left: {self.max_attempts - self.attempts}", font=("Helvetica", 18))
        self.attempts_label.pack(pady=10)

  
    def get_display_word(self):
        display = ""
        for letter in self.secret_word:
            if letter in self.guesses:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()

  
    def make_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return
        if guess in self.guesses:
            messagebox.showinfo("Already Guessed", "You have already guessed that letter.")
            return
        self.guesses.append(guess)
        if guess not in self.secret_word:
            self.attempts += 1
        self.update_game_status()

  
    def update_game_status(self):
        self.word_label.config(text=self.get_display_word())
        self.attempts_label.config(text=f"Attempts left: {self.max_attempts - self.attempts}")
        if self.attempts >= self.max_attempts:
            messagebox.showinfo("Game Over", f"You lost! The word was: {self.secret_word}")
            self.master.quit()
        elif all(letter in self.guesses for letter in self.secret_word):
            messagebox.showinfo("Congratulations", "You've guessed the word!")
            self.master.quit()
if __name__ == "__main__":
    root = tk.Tk()
    game = Hangman(root)
    root.mainloop()
