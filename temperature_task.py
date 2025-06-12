'''
An app that converts temperature beween F and C

Version 11: basic functions that coonvert temperature: no validation
 '''

from tkinter import *

class Converter:

    '''Set up the GUI'''
    def __init__(self):

        # main window
        self.root = Tk()
        self.root.title("Temperature Converter")

        # container for frames
        self.container = Frame(self.root)

        # dictionary to hold frames 
        self.frames = Frame(self.root)
        self.container.grid(row=0, column=0, sticky='nsew')

        # dictionary to hold frames
        self.frames = {}
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_c_frame"] = self.create_to_c_frame()
        self.frames["to_f_frame"] = self.create_to_f_frame()

        # show the initial frame
        self.show_frame("MainFrame")

    def run (self):
        self.root.mainloop()

    def show_frame(self, name):
        '''ldispay the required frame from the dictionary'''
        frame = self.frames[name]
        frame.tkraise()

    def create_main_frame(self):
        '''Create the home screen of the app'''
        frame = Frame(self.container)

        #Main heading
        heading = Label(frame, text="Temperature Converter", font="Verdana 16 bold")
        heading.pack(pady=20)

        to_c_button = Button(frame, text="Convert to Celsius", bg="yellow",font="Verdana 12 bold", command=lambda: self.show_frame("to_c_frame"))
        to_c_button.pack(pady=10)

        to_f_button = Button(frame, text="Convert to Fahrenheit", bg="red",  font="Verdana 12 bold", command=lambda: self.show_frame("to_f_frame"))
        to_f_button.pack(pady=10)

        return frame

    def create_to_c_frame(self):
        '''Create the frame to convert Fahrenheit to Celsius'''
        frame = Frame(self.container)

        label = Label(frame, text="Fahrenheit to Celsius", font="Verdana 14 bold")
        label.pack(pady=20)

        back_button = Button(frame, text="Back", command=lambda: self.show_frame("MainFrame"))
        back_button.pack(pady=10)

        return frame
    
    def create_to_f_frame(self):
        return
    
if __name__ == "__main__":
    app = Converter()
    app.run()

    