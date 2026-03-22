import tkinter as tk
import random
import time

# Create window
root = tk.Tk()
root.title("Memory Puzzle Game")
root.geometry("400x500")

# Game setup
cards = list(range(1, 9)) * 2
random.shuffle(cards)

buttons = []
first_card = None
second_card = None
revealed = [False] * 16
start_time = time.time()

# Timer label
timer_label = tk.Label(root, text="Time: 0 sec", font=("Arial", 14))
timer_label.pack(pady=10)

# Update timer
def update_timer():
    elapsed = int(time.time() - start_time)
    timer_label.config(text=f"Time: {elapsed} sec")
    root.after(1000, update_timer)

# Handle button click
def on_click(index):
    global first_card, second_card

    if revealed[index]:
        return

    # Show card value
    buttons[index].config(text=str(cards[index]), state="disabled")

    if first_card is None:
        first_card = index
    elif second_card is None:
        second_card = index
        root.after(500, check_match)

# Check if cards match
def check_match():
    global first_card, second_card

    if cards[first_card] == cards[second_card]:
        revealed[first_card] = True
        revealed[second_card] = True
    else:
        buttons[first_card].config(text="", state="normal")
        buttons[second_card].config(text="", state="normal")

    first_card = None
    second_card = None

    # Check win condition
    if all(revealed):
        win_game()

# Win message
def win_game():
    elapsed = int(time.time() - start_time)
    result = tk.Label(root, text=f"You Won! 🎉\nTime: {elapsed} sec", font=("Arial", 16))
    result.pack(pady=20)

# Create grid
frame = tk.Frame(root)
frame.pack()

for i in range(16):
    btn = tk.Button(frame, text="", width=8, height=4,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    buttons.append(btn)

# Start timer
update_timer()

# Run app
root.mainloop()