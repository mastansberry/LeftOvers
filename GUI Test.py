# GUI Test (1.4.5)

import Tkinter

#create root window
root = Tkinter.Tk()
root.wm_title('Jacob U. Circle Program')

#create slider variables
radius_intvar = Tkinter.IntVar()
xpos_intvar = Tkinter.IntVar()
ypos_intvar = Tkinter.IntVar()
red_intvar = Tkinter.IntVar()
green_intvar = Tkinter.IntVar()
blue_intvar = Tkinter.IntVar()

#set slider variables
radius_intvar.set(100)
xpos_intvar.set(0)
ypos_intvar.set(0)
red_intvar.set(127)
green_intvar.set(127)
blue_intvar.set(127)

#define function to handle slider changes
def slider_changed(new_intval):
    #read all slider variables
    r = radius_intvar.get()
    x = xpos_intvar.get()
    y = ypos_intvar.get()
    rcol = red_intvar.get()
    gcol = green_intvar.get()
    bcol = blue_intvar.get()
    
    #set circle coordinates and fill color
    color_hexval = '#' + hexstring(rcol) + hexstring(gcol) + hexstring(bcol)
    ball_canvas.coords(circle_item, 150 + x - r, 150 + y - r, 150 + x + r, 150 + y + r)
    ball_canvas.itemconfig(circle_item, fill = color_hexval)
    
    #insert text in hexstring viewer
    hex_textbox.insert(Tkinter.END, color_hexval + '\n')
    #scroll to the end of the text box
    hex_textbox.see(Tkinter.END)

#create sliders
radius_slider = Tkinter.Scale(root, from_ = 0, to = 150, variable = radius_intvar, label = 'radius', orient = Tkinter.HORIZONTAL, command = slider_changed)
x_slider = Tkinter.Scale(root, from_ = -300, to = 300, variable = xpos_intvar, label = 'x', orient = Tkinter.HORIZONTAL, command = slider_changed)
y_slider = Tkinter.Scale(root, from_ = -300, to = 300, variable = ypos_intvar, label = 'y', orient = Tkinter.HORIZONTAL, command = slider_changed)
red_slider = Tkinter.Scale(root, from_ = 0, to = 255, variable = red_intvar, label = 'Red', orient = Tkinter.HORIZONTAL, command = slider_changed)
green_slider = Tkinter.Scale(root, from_ = 0, to = 255, variable = green_intvar, label = 'Green', orient = Tkinter.HORIZONTAL, command = slider_changed)
blue_slider = Tkinter.Scale(root, from_ = 0 ,to = 255, variable = blue_intvar, label = 'Blue', orient = Tkinter.HORIZONTAL, command = slider_changed)

#create program info text
text = Tkinter.Label(root, text = 'Jacob U.\nCircle Program')

#create displays
ball_canvas = Tkinter.Canvas(root, width = 300, height = 300, background = '#FFFFFF')
hex_textbox = Tkinter.Text(root, width = 10)

#grid all widgets
text.grid(row = 0, column = 0)
ball_canvas.grid(row = 0, column = 1, columnspan = 3)
hex_textbox.grid(row = 0, column = 4, rowspan = 3)
radius_slider.grid(row = 1, column = 1)
x_slider.grid(row = 1, column = 2)
y_slider.grid(row = 1, column = 3)
red_slider.grid(row = 2, column = 1)
green_slider.grid(row = 2, column =2)
blue_slider.grid(row = 2, column = 3)

#create the circle item
circle_item = ball_canvas.create_oval(150 - radius_intvar.get(), 150 - radius_intvar.get(), 150 + radius_intvar.get(), 150 + radius_intvar.get(), outline = '#000000', fill = '#00FFFF')

#create function to convert color ints to hex values
def hexstring(slider_intvar):
    '''A function to prepare data from controller's widget for view's consumption
    
    slider_intvar is an IntVar between 0 and 255, inclusive
    hexstring() returns a 2-character string representing a value in hexadecimal
    '''
    # Convert to hex
    slider_hex = hex(slider_intvar)
    # Drop the 0x at the beginning of the hex string
    slider_hex_digits = slider_hex[2:] 
    # Ensure two digits of hexadecimal:
    if len(slider_hex_digits)==1:
        slider_hex_digits = '0' + slider_hex_digits 
    return slider_hex_digits
    
#event loop
root.mainloop()