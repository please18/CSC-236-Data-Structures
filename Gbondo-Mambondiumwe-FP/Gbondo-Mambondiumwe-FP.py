# coding=utf-8 (Do not delete coding=utf-8)
#####################################################################################
# FINAL LAB PROJECT
# CSC 236-DATA STRUCTURES AND ALGORITHMS
# Authors: Saffa Gbondo and Marima Andrew Mambondiumwe
# Driver- Saffa Gbondo
# Navigator- Marima Andrew Mambondiumwe
# ######### ACKNOWLEDGEMENTS ################# ACKNOWLEDGEMENTS #######################
# Dr Jan Pearce for content on exploring the Tkinter module.
# http://cs.berea.edu/courses/csc226/tasks/t18.gui-making.html
#
# Project Idea obtained from CSC 236 A17: ANIMAL GUESSING GAME, modified by authors to use a stack instead of a tree and also use the Tkinter module
# http://cs.berea.edu/courses/csc236/tasks/a17.animal.tree.html
#
# Consultations: Newboston youtube Python GUI with Tkinter tutorial videos
#                https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d
#
# All images obtained from:
# https://images.google.com/
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#######################################################################################################################

from Tkinter import *                                               # imports the Tkinter library


class Stack:
    """this opens a window and allows the user to input in animals from given options and the animals will then be appended to a stack"""

    def __init__(self, master):  # the initializer method acts as the constructor and initializes the parent window
        """initializes the values to be used in the class and acts as a constructor"""
        self.items = []
        self.empty_list = []
        frame = Frame(master)                                       # this creates a frame widget for grouping and organizing the layout on the master window
        frame.grid(column=1000, row=1000, sticky=(N, W, E, S))      # creates a grid that organizes widgets in a table-like structure
        frame.pack()                                                # this packs and displays widgets in rows and columns

        self.customFont = ('times', 15, 'bold', 'italic')           # Sets font to the new values
        self.customFont1 = ('times', 10, 'bold', 'italic')          # Sets font to the new values
        self.intro = Label(frame, text="Welcome, this program stacks three-letter animals on to a Stack").pack()
        self.selection = Label(frame, text="Please select from the following animals to append it to a stack").pack()
        self.animals = Label(frame, text="Ant, Bat, Bee, Cat, Cow, Dog, Fox, Rat, Pig").pack()

        self.data = StringVar()
        self.my_data = Entry(root, textvariable=self.data).pack(side=TOP)
        self.append_button = Button(frame, text="APPEND", command=self.append_list, fg="White", bg="Green",
                                    font=self.customFont).pack(side=RIGHT)
        self.append_button = Button(frame, text="PEEk", command=self.peek, fg="White", bg="Red",
                                    font=self.customFont).pack(side=LEFT)
        self.append_button = Button(frame, text="POP/REMOVE", command=self.popping, fg="White", bg="Red",
                                    font=self.customFont).pack(side=LEFT)

        # ************** IMAGES ************* Imports and saves images
        self.photo1 = PhotoImage(file="cow.gif")  # imports and saves the image for a cow
        self.photo2 = PhotoImage(file="cat.gif")  # imports and saves the image for a cat
        self.photo3 = PhotoImage(file="dog.gif")  # imports and saves the image for a dog
        self.photo4 = PhotoImage(file="pig.gif")  # imports and saves the image for a pig
        self.photo5 = PhotoImage(file="rat.gif")  # imports and saves the image for a rat
        self.photo6 = PhotoImage(file="ant.gif")  # imports and saves the image for an ant
        self.photo7 = PhotoImage(file="bat.gif")  # imports and saves the image for a bat
        self.photo8 = PhotoImage(file="bee.gif")  # imports and saves the image for a bee
        self.photo9 = PhotoImage(file="fox.gif")  # imports and saves the image for a fox
        self.photo10 = PhotoImage(file="1.gif")  # imports and saves the image for a box

    def append_list(self):
        """this method adds the inputted animals to the stack and also displays an image that corresponds to the animal chosen"""
        my_list = self.data.get().lower()
        # this portion has a big(0) of 0(1), which is to insert an item to the stack
        self.empty_list.append(my_list)
        Label(root, text=self.empty_list).pack()
        if str(my_list) == 'cow':
            Label(root, image=self.photo1).place(x=2, y=0, relwidth=0.25, relheight=0.4)
        elif str(my_list) == 'cat':
            Label(root, image=self.photo2).place(x=2, y=0, relwidth=0.25, relheight=0.4)
        elif str(my_list) == 'dog':
            Label(root, image=self.photo3).place(x=2, y=0, relwidth=0.25, relheight=0.4)
        elif str(my_list) == 'pig':
            Label(root, image=self.photo4).place(x=2, y=0, relwidth=0.25, relheight=0.4)
        elif str(my_list) == 'rat':
            Label(root, image=self.photo5).place(x=2, y=0, relwidth=0.25, relheight=0.4)
        elif str(my_list) == 'ant':
            Label(root, image=self.photo6).place(x=2, y=0, relwidth=0.25, relheight=0.4)
        elif str(my_list) == 'bat':
            Label(root, image=self.photo7).place(x=2, y=0, relwidth=0.25, relheight=0.4)
        elif str(my_list) == 'bee':
            Label(root, image=self.photo8).place(x=2, y=0, relwidth=0.25, relheight=0.4)
        elif str(my_list) == 'fox':
            Label(root, image=self.photo9).place(x=2, y=0, relwidth=0.25, relheight=0.4)
        else:
            Label(root, text="There is no animal like that").place(x=2, y=0, relwidth=0.25, relheight=0.4)

    def isEmpty(self):
        """this method returns an empty list"""
        return self.items == []

    def push(self, item):
        """this allowes the items to be stacked in order of which they are added"""
        self.items.append(item)

    def pop(self):
        """this allows items to be removed from the stack"""
        return self.empty_list.pop()

    def popping(self):
        """items are removed from the stack, one after the other from the last one that was added"""
        self.pop()
        n = len(self.empty_list)
        if n > 0:
            # removes the last animal added and then displays the image of the current animal to be removed next
            if self.empty_list[n - 1] == 'cow':
                Label(root, text=self.empty_list).pack()
                Label(root, image=self.photo1).place(x=2, y=0, relwidth=0.25, relheight=0.4)
            elif self.empty_list[n - 1] == 'cat':
                Label(root, text=self.empty_list).pack()
                Label(root, image=self.photo2).place(x=2, y=0, relwidth=0.25, relheight=0.4)
            elif self.empty_list[n - 1] == 'dog':
                Label(root, text=self.empty_list).pack()
                Label(root, image=self.photo3).place(x=2, y=0, relwidth=0.25, relheight=0.4)
            elif self.empty_list[n - 1] == 'pig':
                Label(root, text=self.empty_list).pack()
                Label(root, image=self.photo4).place(x=2, y=0, relwidth=0.25, relheight=0.4)
            elif self.empty_list[n - 1] == 'rat':
                Label(root, text=self.empty_list).pack()
                Label(root, image=self.photo5).place(x=2, y=0, relwidth=0.25, relheight=0.4)
            elif self.empty_list[n - 1] == 'ant':
                Label(root, text=self.empty_list).pack()
                Label(root, image=self.photo6).place(x=2, y=0, relwidth=0.25, relheight=0.4)
            elif self.empty_list[n - 1] == 'bat':
                Label(root, text=self.empty_list).pack()
                Label(root, image=self.photo7).place(x=2, y=0, relwidth=0.25, relheight=0.4)
            elif self.empty_list[n - 1] == 'bee':
                Label(root, text=self.empty_list).pack()
                Label(root, image=self.photo8).place(x=2, y=0, relwidth=0.25, relheight=0.4)
            elif self.empty_list[n - 1] == 'fox':
                Label(root, text=self.empty_list).pack()
                Label(root, image=self.photo9).place(x=2, y=0, relwidth=0.25, relheight=0.4)
            else:
                Label(root, text='There is no animal like that').pack()
                # Label(root, text='The list is not empty yet').pack()
        else:
            Label(root, text='the list is empty').pack()
            Label(root, image=self.photo10).place(x=2, y=0, relwidth=0.25, relheight=0.4)

    def peek(self):
        """allows you to see the items that are already in the stack"""
        Label(root, text=self.empty_list).pack()
        return self.items[len(self.items) - 1]

    def size(self):
        """returns the length of the stack"""
        return len(self.items)


root = Tk()
root.title("Animal Stack Game")  # this sets the title of the window to Stack Lab

name = Stack(root)

root.mainloop()
