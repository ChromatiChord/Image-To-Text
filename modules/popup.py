import tkinter as tk

def runner(text, root):
    popup = tk.Toplevel()

    popup.title("Selected Text")

    text_widget = tk.Text(popup, wrap=tk.WORD, font=("Arial", 18), undo=True)
    text_widget.pack(padx=20, pady=20, expand=True, fill=tk.BOTH)

    text_widget.insert(tk.END, text)

    def close_popup(event=None):
        popup.destroy()
        root.quit()

    # Function to undo the last change in the text widget
    def undo(event=None):
        try:
            text_widget.edit_undo()
        except tk.TclError:
            pass

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