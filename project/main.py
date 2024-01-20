import tkinter as tk
from project.pages.main_page import MainPage
from project.pages.info_page import InfoPage
from ttkbootstrap import Style


# Each component/page of the application is structured in classes. This is not very Pythonic, but it helps to keep the
# code organized and easy to read. Each class is a page of the application.

class TkinterApp(tk.Tk):
    """ This is the main class of the application. It inherits from tk.Tk, which is the main class of the Tkinter """

    def __init__(self, *args, **kwargs):
        """ This method is called when the application is initialized.
        Here we define the main window of the application and the style of the application.
        We also define the main container of the application, which is a Frame that will hold all the other frames/pages.
        """
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Weather Information")
        self.style = Style(theme="darkly")

        # This is the main container of the application. It is a Frame that will hold all the other frames/pages.
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Here we add all the pages of the application. Each page is a class that inherits from tk.Frame.
        for F in (MainPage, InfoPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        """
        This method is used to show a frame/page of the application.
        It is called by the buttons of the application.
        """
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    app = TkinterApp()
    app.mainloop()
