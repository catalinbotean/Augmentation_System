from tkinter import Tk, Button, Label, filedialog


class SelectDirectoryWindow:
    def __init__(self, new_window):
        self.window = new_window
        self.select_button = Button(new_window, text="Select Directory", fg='black', command=self.choose_directory)
        self.select_button.place(x=20, y=100)
        self.close_button = Button(new_window, text="Close Window", fg='black', command=self.close_window)
        self.close_button.place(x=150, y=100)
        self.directory_name = "No directory selected"
        self.directory_label = Label(new_window, text=self.directory_name, fg='white', font=("Helvetica", 16))
        self.directory_label.place(x=55, y=50)

    def choose_directory(self):
        directory = filedialog.askdirectory()
        self.directory_name = directory
        self.directory_label['text'] = directory

    def close_window(self):
        self.window.destroy()

    def get_directory(self):
        return self.directory_name


def create_ui():
    window = Tk()
    select_directory = SelectDirectoryWindow(window)
    window.title('FCV Project')
    window.geometry("300x200")
    window.mainloop()
    return select_directory.get_directory()

