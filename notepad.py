"""
Simple Notepd gui application 
basic idea :
when you open a already existing file then you have to show all the
contents of the file to the text editor..ie. you have to take all contents
of file and insert onto the text editor.

when you open a new file then you have to delete all the contents of the
text editor i.e. make a text editor blank

when you open a existing file then save it ,then you have to overwrite the
content of existing file..

"""

# from tkinter library import everything
# this is used for making gui application
from tkinter import *

# from tkinter.messagebox class import showinfo static method
# this is used for showing about notepad
from tkinter.messagebox import showinfo

# from tkinter.filedialog import askopenfilename,asksaveasfilename static method
# this is used for opening the pre-existing file
# and saving the file.
from tkinter.filedialog import askopenfilename, asksaveasfilename

# import os library
# this is used for retrieving the base name of the file
import os


# function for creating new file
def newFile() :

    # make file variable as a global
    # so that it is acessible freely
    # anywhere in the program
    global file

    # set the window name 
    root.title("Untitled - Notepad")

    # intialise file with None
    file = None

    # delete TextArea full content
    # 1.0 means 1st row and 0th column
    TextArea.delete(1.0, END)


# function for opening the already existing file
def openFile() :

    # make file variable as a global 
    global file

    # for opening the all type of existing file
    file = askopenfilename(defaultextension = ".txt",
                           filetypes = [("All Files","*.*"),
                                        ("Text Document","*.txt")])

    # if not assining anything
    # if you don't have any file to open
    if file == "" :
        
        #intialise file with None
        file = None

    # if you have a file to open 
    else :

        # set name of the gui window same
        # as the open file name
        root.title(os.path.basename(file)+ "- Notepad")

        # delete the overall content of the text area
        TextArea.delete(1.0,END)

        # open the file in read mode
        # file object is created first
        f = open(file,"r")

        # read method of file object shows the content
        # present in the file
        # insert content of file to the text area
        # from 1st row ,oth column to the end.
        TextArea.insert(1.0, f.read())

        # close the file object
        # because its work is complete
        f.close()


# function for saving the file        
def saveFile() :

    # make file variable as a global 
    global file

    # if file is none then save as a new file
    if file == None :

        # set the name of new file
        file =  asksaveasfilename(initialfile = "Untitled.txt",
                                  defaultextension = ".txt",
                           filetypes = [("All Files","*.*"),
                                        ("Text Document","*.txt")])

        if file == "" :
            #intialise file with None
            file = None

        else :
            # save as a new file

             # open the file in write mode
            # file object is created first   
            f = open(file,"w")

            # write the whole content of text area
            # into the file object.
            # getmethod gives the content of text area
            f.write(TextAre.get(1.0,END))

            # close and save the file object
            # because its work is complete
            f.close()

            # after saving the file ,title change
            # set the new title for root window
            root.title(os.path.basename(file) + "- Notepad")

    # if file is not none
    # then is is save as a new file
    # we can replace the content with
    # text area content.
    else :
        
        # open the file in write mode
        # file object is created first        
        f = open(file,"w")

        # write the whole content of text area
        # into the file object.
        # getmethod gives the content of text area.
        f.write(TextArea.get(1.0,END))

        # close and save the file object
        # because its work is complete
        f.close()

            
        

# function for destroying the gui applicaton
def quitApp() :
    root.destroy()

# function for cut functionality
def cut() :

    # using the text area inbuilt events
    TextArea.event_generate(("<<Cut>>"))

# function for copy functionality
def copy():
    
    # using the text area inbuilt events
    TextArea.event_generate(("<<Copy>>"))

# function for paste functionality
def paste():
    
    # using the text area inbuilt events
    TextArea.event_generate(("<<Paste>>"))

# function for about functionality
def about() :

    # its pop-up show info window with Notepad name and given msg
    showinfo("Notepad","Notepad by Code With Ankit Rai")


# Driver Code
if __name__ == "__main__" :

    # tkinter window is created
    root = Tk()

    # set the title window name
    root.title("Notepad")

    # set the icon for the gui application
    root.wm_iconbitmap(r"C:/Users/user/Pictures/notepad_icon.png")

    # set the geometry i.e.
    # length and breadth of the root window
    root.geometry("644x788")

    # create a text area for the root
    # with lunida 13 font
    # text area is for writing the content
    TextArea = Text(root,font = "lucida 13")

    # intialise file with None
    file = None

    # fix or adding the text area into the root window
    # with expanding and filling features
    # so that on increasing the size of window
    # text area size is also increarse
    TextArea.pack(expand = True,fill = BOTH)

    # let's create a menubar for the root window
    MenuBar = Menu(root)

    # File menu starts-----

    # create a file menu for menubar
    FileMenu = Menu(MenuBar, tearoff = 0)

    # command add to open new file
    FileMenu.add_command(label = "New",command = newFile)

    # command add to open alredy existing file
    FileMenu.add_command(label = "Open", command = openFile)

    # command add to save the current file
    FileMenu.add_command(label = " Save",command = saveFile)

    # adding the separator line in b/w exit label and other labels
    FileMenu.add_separator()

    # command add to exit the application
    FileMenu.add_command(label = "Exit",command = quitApp)

    # adding the file menu to the menubar with label File
    MenuBar.add_cascade(label = "File",menu = FileMenu)
    
    # File menu ends---

    # Edit Menu Starts---
    
    # create a Edit menu for menubar
    EditMenu = Menu(MenuBar, tearoff = 0)
 
    # add command to give a feature of cut,copy,paste function
    EditMenu.add_command(label = "Cut", command = cut  )
    EditMenu.add_command(label = "Copy", command = copy  )
    EditMenu.add_command(label = "Patse", command =  paste  )

    # adding the Edit menu to the menubar with label Edit
    MenuBar.add_cascade(label = "Edit",menu = EditMenu)
    
    # Edit menu ends -----

    # help menu starts ----

    # create a help menu for menubar
    HelpMenu = Menu(MenuBar,tearoff = 0)

    # command add to tell about the application
    HelpMenu.add_command(label = "About Notepad",command = about)

    # adding the help menu to the menubar with label help
    MenuBar.add_cascade(label = "Help",menu = HelpMenu )
      
    # help menu ends ---

    # set the root config
    # adding the menubar to the root window
    root.config(menu = MenuBar)

    # adding the scroll bar

    # scroll bar is generate for text area 
    Scroll = Scrollbar(TextArea)

    # set the location of the scroll bar
    Scroll.pack(side = RIGHT, fill = Y)
    
    # setting the scroll bar
    Scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = Scroll.set)

    # start the gui application
    root.mainloop()
