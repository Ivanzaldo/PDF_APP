import tkinter as tk

class GUI:

    def __init__(self):
        self.parent = tk.Tk()
        self.parent.title("GUI Window")
        # Button control
        button = tk.Button(
            self.parent, text = "New window", command = self.window)
        button.grid(sticky = tk.NSEW)
        # Define window size
        self.parent.geometry("278x26")

    def window(self):
        try:
            self.information.winfo_viewable()
        except AttributeError as err:
            self.information = tk.Toplevel(self.parent)
            # Make Toplevel a child of parent
            self.information.transient( self.parent )
            self.information.title("Information Window")

            # place all your widgets here

        else:
            self.information.focus_force()

if __name__ == "__main__":
    app = GUI()
    app.parent.mainloop()