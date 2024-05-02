import tkinter
top = tkinter.Tk()
Can = tkinter.Canvas(top, bg="red", height=300, width=300)
WindH = Can.winfo_height()
WindW = Can.winfo_width()
blink = True 
cursor = None
CursorX = 0
CursorY = 0

def tik(): 
    global blink
    global CursorX
    global CursorY
    global cursor

    # Erase last-drawn cursor 
    Can.delete(cursor)

    
    if blink:
        cursor = Can.create_rectangle(CursorX+5, CursorY-5, CursorX+5+0.8, CursorY+5, fill='black')
    blink = not blink
    Can.after(400, tik) 

Can.after(500, tik) 
globalText=""

def keyevent(event):
    Can.delete('all')
    global globalText

## Don't add control characters to global text: 
    if event.char!='\x08': 
        globalText+=event.char
        last_char=globalText[-1]


    if event.keysym =='BackSpace': 
        globalText=globalText[:-1]

## Drawing the text and cursor: 
    drawText()

def keytab(event):
    global globalText
    Can.delete('all')
    
## Don't add control characters to global text: 
    if event.char!='\x08': 
        globalText+='     '
        last_char=globalText[-1]

## Drawing the text and cursor for tab: 
    drawText()

def drawText():  
    iChar=0
    charWidth=8
    xOffset=10 
    yOffset=10
    global globalText
    global blink
    global CursorX
    global CursorY

    maxChar = 4

    lines = globalText.split("\r")
    splitLines = []
    for line in lines: 
        if len(line) < maxChar : 
            splitLines.append(line)
        else:
            x = line
            while len(x) > maxChar : 
                splitLines.append(line[:maxChar])
                x = line[maxChar:]
            if len(x) > 0: 
              splitLines.append(x)

    yOffset=10
    print(splitLines)
    for newline in splitLines: 
        drawLine(newline, yOffset) 
        yOffset+=10


# This will draw the line 

def drawLine(line, yOffset):  
    iChar=0
    charWidth=8
    xOffset=10 
    global blink
    global CursorX
    global CursorY

    x = 0
    for currentKey in line:
        if currentKey=='\r':
            yOffset+=10
            xOffset=10
            iChar= -1
        if currentKey=='\x08':
            pass 
        else:   
            x = charWidth*iChar+xOffset
            Can.create_text(x, yOffset, text=currentKey, fill="black")    
            iChar+=1

    CursorX=x 
    CursorY=yOffset


top.bind("<KeyPress>", keyevent)

top.bind("<Tab>", keytab)

Can.pack()

top.mainloop()