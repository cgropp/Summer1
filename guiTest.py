from tkinter import *

# Tessting the GUI using the tkinter module
root = Tk() 
frame = Frame(root) 
frame.pack() 
bottomframe = Frame(root) 
bottomframe.pack( side = BOTTOM ) 
relevantData1 = Button(frame, text = 'RelevantData1', fg ='black') 
relevantData1.pack( side = LEFT) 
relevantData2 = Button(frame, text = 'RevelantData2', fg='black') 
relevantData2.pack( side = LEFT )

#bluebutton = Button(frame, text ='Blue', fg ='blue') 
#bluebutton.pack( side = LEFT ) 
#blackbutton = Button(bottomframe, text ='Black', fg ='black') 
#blackbutton.pack( side = BOTTOM) 
root.mainloop() 

