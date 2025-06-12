'''
An app that converts temperature beween F and C

Version 1: basic functions that convert temperature: no validation at all
Version 2: change to a responsive layout using wieght
 '''

from tkinter import *

class Converter:
    '''Set up the GUI'''
    def __init__(self):
        self.root = Tk()
        self.root.title("Temperature Converter")
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)

        # Container for frames
        self.container = Frame(self.root)
        self.container.grid()
        self.container.grid_rowconfigure(0,weight=1)
        self.container.grid_columnconfigure(0,weight=1)

        # Dictionary to hold frames
        self.frames = {}
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_c_frame"] = self.create_to_c_frame()
        self.frames["to_f_frame"] = self.create_to_f_frame()

        # Show the initial frame
        self.show_frame("MainFrame")


    def run(self):
        '''runs the program'''
        self.root.mainloop()

    def show_frame(self, name):
        '''Display the required frame from the dictionary'''
        frame = self.frames[name]
        frame.tkraise()

    def create_main_frame(self):
        '''Create the mainframe'''
        
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky=NSEW)
        
        for i in range(2):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(2):
            frame.grid_columnconfigure(j, weight=1)            

        heading = Label(frame, text="Temperature Converter", font="Verdana 16 bold")
        heading.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        to_c_button = Button(frame, text="Convert to Celsius", bg="yellow", font="Verdana 12 bold",command=lambda: self.show_frame("to_c_frame"))
        to_c_button.grid(row=1, column=0, sticky=NSEW)

        to_f_button = Button(frame, text="Convert to Fahrenheit", bg="pink", font="Verdana 12 bold",command=lambda: self.show_frame("to_f_frame"))
        to_f_button.grid(row=1, column=1, sticky=NSEW)

        return frame

    def create_to_c_frame(self):
        '''Create the frame to convert Fahrenheit to Celsius'''
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky=NSEW)
        
        for i in range(4):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(3):
            frame.grid_columnconfigure(j, weight=1)

        label = Label(frame, text="Enter the temperature in Fahrenheit", font="Verdana 14 bold")
        label.grid(row=0, column=0, columnspan=3, sticky=NSEW)

        self.fahrenheit_entry = Entry(frame, justify=CENTER)
        self.fahrenheit_entry.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        convert_button = Button(frame, text="Convert", command=self.convert_to_celsius)
        convert_button.grid(row=2, column=0, sticky=NSEW)
        
        back_button = Button(frame, text="Back", command=lambda: self.show_frame("MainFrame"))
        back_button.grid(row=2, column=1, sticky=NSEW)

        reset_button = Button(frame, text="Reset", command=lambda: self.reset())
        reset_button.grid(row=2, column=2, sticky=NSEW)

        self.converted_c_result = Label(frame, text="")
        self.converted_c_result.grid(row=3, column=0, columnspan=3, sticky=NSEW)

        return frame

    def create_to_f_frame(self):
        '''Create the frame to convert Celsius to Fahrenheit'''
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky=NSEW)
        
        for i in range(4):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(3):
            frame.grid_columnconfigure(j, weight=1)

        label = Label(frame, text="Enter the temperature in celsius", font="Verdana 14 bold")
        label.grid(row=0, column=0, columnspan=3, sticky=NSEW)

        self.celsius_entry = Entry(frame, justify=CENTER)
        self.celsius_entry.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        convert_button = Button(frame, text="Convert", command=self.convert_to_fahrenheit)
        convert_button.grid(row=2, column=0, sticky=NSEW)

        back_button = Button(frame, text="Back", command=lambda: self.show_frame("MainFrame"))
        back_button.grid(row=2, column=1, sticky=NSEW)

        reset_button = Button(frame, text="Reset", command=lambda: self.reset())
        reset_button.grid(row=2, column=2, sticky=NSEW)

        self.converted_f_result = Label(frame, text="")
        self.converted_f_result.grid(row=3, column=0, columnspan=3, sticky=NSEW)

        return frame

    def convert_to_celsius(self):
        '''converts the fahrenheit input (from entry box) and converts it to celsius'''
        fahrenheit = float(self.fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5 / 9
        self.converted_c_result.config(text=f"It is {celsius:.2f}°C")

    def convert_to_fahrenheit(self):
        '''converts the celsius input (from entry box) and converts it to fahrenheit'''
        celsius = float(self.celsius_entry.get())
        fahrenheit = (celsius * 9 / 5) + 32
        self.converted_f_result.config(text=f"It is: {fahrenheit:.2f}°F")
    
    def reset(self):
        '''resets the entry box'''
        self.celsius_entry.delete(0, END)
        self.fahrenheit_entry.delete(0, END)
        self.converted_f_result.config(text="")
        self.converted_c_result.config(text="")

if __name__ == "__main__":
    app = Converter()
    app.run()