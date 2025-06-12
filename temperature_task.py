'''Add commentMore actions
An app that converts temperature beween F and C

Version 11: basic functions that coonvert temperature: no validation
Version 1: basic functions that convert temperature: no validation at all
 '''

from tkinter import *

class Converter:

    '''Set up the GUI'''
    def __init__(self):

        # main window
        self.root = Tk()
        self.root.title("Temperature Converter")

        # container for frames
        # Container for frames
        self.container = Frame(self.root)
        self.container.grid()

        # dictionary to hold frames 
        self.frames = Frame(self.root)
        self.container.grid(row=0, column=0, sticky='nsew')

        # dictionary to hold frames
        # Dictionary to hold frames
        self.frames = {}
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_c_frame"] = self.create_to_c_frame()
        self.frames["to_f_frame"] = self.create_to_f_frame()

        # show the initial frame
        # Show the initial frame
        self.show_frame("MainFrame")

    def run(self):
        self.root.mainloop()

    def show_frame(self, name):
        '''ldispay the required frame from the dictionary'''
        '''Display the required frame from the dictionary'''
        frame = self.frames[name]
        frame.tkraise()

    def create_main_frame(self):
        '''Create the home screen of the app'''
        '''Create the mainframe'''
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky=NSEW)


        #Main heading
        heading = Label(frame, text="Temperature Converter", font="Verdana 16 bold")
        heading.pack(pady=20)
        heading.grid(row=0, column=0, columnspan=2, stick=NSEW)

        to_c_button = Button(frame, text="Convert to Celsius", bg="yellow",font="Verdana 12 bold", command=lambda: self.show_frame("to_c_frame"))
        to_c_button.pack(pady=10)
        to_c_button = Button(frame, text="Convert to Celsius", bg="yellow", font="Verdana 12 bold",command=lambda: self.show_frame("to_c_frame"))
        to_c_button.grid(row=1, column=0, stick=NSEW)

        to_f_button = Button(frame, text="Convert to Fahrenheit", bg="red",  font="Verdana 12 bold", command=lambda: self.show_frame("to_f_frame"))
        to_f_button.pack(pady=10)
        to_f_button = Button(frame, text="Convert to Fahrenheit", bg="pink", font="Verdana 12 bold",command=lambda: self.show_frame("to_f_frame"))
        to_f_button.grid(row=1, column=1, stick=NSEW)

        return frame

    def create_to_c_frame(self):
        '''Create the frame to convert Fahrenheit to Celsius'''
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky=NSEW)

        label = Label(frame, text="Fahrenheit to Celsius", font="Verdana 14 bold")
        label.pack(pady=20)
        label = Label(frame, text="Enter the temperature in Fahrenheit", font="Verdana 14 bold")
        label.grid(row=0, column=0, columnspan=3, stick=NSEW)

        self.fahrenheit_entry = Entry(frame, justify=CENTER)
        self.fahrenheit_entry.grid(row=1, column=0, columnspan=3, stick=NSEW)

        convert_button = Button(frame, text="Convert", command=self.convert_to_celsius)
        convert_button.grid(row=2, column=0, stick=NSEW)
        
        back_button = Button(frame, text="Back", command=lambda: self.show_frame("MainFrame"))
        back_button.pack(pady=10)
        back_button.grid(row=2, column=1, stick=NSEW)

        reset_button = Button(frame, text="Reset", command=lambda: self.reset())
        reset_button.grid(row=2, column=2, stick=NSEW)

        self.converted_c_result = Label(frame, text="")
        self.converted_c_result.grid(row=3, column=0, columnspan=3, stick=NSEW)

        return frame
    

    def create_to_f_frame(self):
        '''Create the frame to convert Celsius to Fahrenheit'''
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky=NSEW)

        label = Label(frame, text="Enter the temperature in celsius", font="Verdana 14 bold")
        label.grid(row=0, column=0, columnspan=3, stick=NSEW)

        self.celsius_entry = Entry(frame, justify=CENTER)
        self.celsius_entry.grid(row=1, column=0, columnspan=3, stick=NSEW)

        convert_button = Button(frame, text="Convert", command=self.convert_to_fahrenheit)
        convert_button.grid(row=2, column=0, stick=NSEW)

        back_button = Button(frame, text="Back", command=lambda: self.show_frame("MainFrame"))
        back_button.grid(row=2, column=1, stick=NSEW)

        reset_button = Button(frame, text="Reset", command=lambda: self.reset())
        reset_button.grid(row=2, column=2, stick=NSEW)

        self.converted_f_result = Label(frame, text="")
        self.converted_f_result.grid(row=3, column=0, columnspan=3, stick=NSEW)

        return frame

    def convert_to_celsius(self):
        fahrenheit = float(self.fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5 / 9
        self.converted_c_result.config(text=f"It is {celsius}°C")

    def convert_to_fahrenheit(self):
        celsius = float(self.celsius_entry.get())
        fahrenheit = (celsius * 9 / 5) + 32
        self.converted_f_result.config(text=f"It is: {fahrenheit}°F")

    def reset(self):
        pass

if __name__ == "__main__":
    app = Converter()
    app.run()

    
    app.run()