import tkinter as tk

def convert_currency():
    try:
        amount = float(amount_entry.get())
        rate = float(rate_entry.get())
        converted_amount = amount * rate
        result_label.config(text=f"Converted Amount: {converted_amount}")
    except ValueError:
        result_label.config(text="Invalid input")
# Create the main window
window = tk.Tk()
window.title("Currency Converter")

# Create the input fields
amount_label = tk.Label(window, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()

rate_label = tk.Label(window, text="Exchange Rate:")
rate_label.pack()
rate_entry = tk.Entry(window)
rate_entry.pack()

# Create the convert button
convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack()

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main loop
window.mainloop()