import tkinter as tk

def runner(text, root):
    popup = tk.Toplevel()

    popup.title("Selected Text")

    text_widget = tk.Text(popup, wrap=tk.WORD, height=20, width=80, font=("Arial", 18))
    text_widget.pack(padx=20, pady=20)

    text_widget.insert(tk.END, text)

    def close_popup(event=None):
        popup.destroy()
        root.quit()

    popup.bind('<Escape>', close_popup)
    popup.protocol("WM_DELETE_WINDOW", close_popup)
    # Sets the window position to the top-left corner
    popup.geometry("+0+0")

def create_popup(text):
    root = tk.Tk()
    root.withdraw()

    runner(text, root)

    root.mainloop()

if __name__ == "__main__":
    create_popup("DEBUG TEXT")
