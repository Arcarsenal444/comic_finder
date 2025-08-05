
"""
comic_finder.py
programmed by: @arcarsenal444
created: fall 2023
An application used to help connect readers who are
new to comic books with titles of interest.
"""


#import libraries

import tkinter
from tkinter import messagebox
from tkinter import simpledialog
import datetime
import webbrowser


def main():
    program_on = True
    count = 0
    title_list = []
    while program_on:
              
        tkinter.messagebox.showinfo("Comic Finder", "Welcome to Comic Finder TM.")
        print("\U0001f9b8")


        # DROPDOWN MENUS FOR PREFERENCE SELECTION -----

        # 1. Genre Selection -----

        pref_list = []

        # Create the default window
        root = tkinter.Tk()
        root.title("Genre Selection Screen")
        root.geometry('600x400')
          
        # Create the list of options
        options_list = ["Action", "Horror", "Sci-Fi", "Romance"]
          
        # Variable to keep track of the option
        # selected in OptionMenu
        value_inside = tkinter.StringVar(root)
          
        # Set the default value of the variable
        value_inside.set("Select a genre that interests you")
          
        # Create the optionmenu widget and passing the options_list and value_inside to it.
        question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
        question_menu.pack()
          
        # Function to print the submitted option-- testing purpose
          
        def print_answers():
            print("\nSelected Option: {}".format(value_inside.get()))
            genre = value_inside.get()
            #print(genre)
            pref_list.append(genre)
            #print(pref_list)
                     
        # Submit button
        # Whenever we click the submit button, our submitted
        # option is printed ---Testing purpose
        submit_button = tkinter.Button(root, text='Submit', command=print_answers)
        submit_button.pack()
          
        root.mainloop()


        # 2. Age Group Selection -----

        # Create the default window
        root = tkinter.Tk()
        root.title("Age Group Selection Screen")
        root.geometry('600x400')
          
        # Create the list of options
        options_list = ["Adult", "Children"]
          
        # Variable to keep track of the option
        # selected in OptionMenu
        value_inside = tkinter.StringVar(root)
          
        # Set the default value of the variable
        value_inside.set("Select an age group that interests you")
          
        # Create the optionmenu widget and passing 
        # the options_list and value_inside to it.
        question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
        question_menu.pack()
          
        # Function to print the submitted option-- testing purpose
          
        def print_answers():
            print("\nSelected Option: {}".format(value_inside.get()))
            #return None
            age_group = value_inside.get()
            #print(age_group)
            pref_list.append(age_group)
            #print(pref_list)
                     
        # Submit button: Whenever we click the submit button, our submitted option is printed ---Testing purpose
        submit_button = tkinter.Button(root, text='Submit', command=print_answers)
        submit_button.pack()
          
        root.mainloop()


        # Additional feature -----

        if "Action" in pref_list and "Adult" in pref_list:
            print("\nNOTE: You're on your way toward a COMIC FINDER recommended selection!")


        # 3. Canon Selection -----

        # Create the default window
        root = tkinter.Tk()
        root.title("Canon Selection Screen")
        root.geometry('600x400')
          
        # Create the list of options
        options_list = ["Eastern", "Western"]
          
        # Variable to keep track of the option
        # selected in OptionMenu
        value_inside = tkinter.StringVar(root)
          
        # Set the default value of the variable
        value_inside.set("Select a canon")
          
        # Create the optionmenu widget and passing 
        # the options_list and value_inside to it.
        question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
        question_menu.pack()
          
        # Function to print the submitted option-- testing purpose
          
        def print_answers():
            print("\nSelected Option: {}".format(value_inside.get()))
            #return None
            canon = value_inside.get()
            #print(canon)
            pref_list.append(canon)
            #print(pref_list)
                     
        # Submit button
        # Whenever we click the submit button, our submitted
        # option is printed ---Testing purpose
        submit_button = tkinter.Button(root, text='Submit', command=print_answers)
        submit_button.pack()
          
        root.mainloop()

        # END OF THE DROPDOWN MENU FOR PREF SELECTION -----


        # MATCHING PREFERENCES WITH TITLES

        if pref_list == ["Horror", "Adult", "Eastern"]:
            tkinter.messagebox.showinfo("Comic Finder",
                                        "Based on your preferences, we suggest Death Note as a title of interest.")
            
        elif pref_list == ["Sci-Fi", "Adult", "Western"]:
            tkinter.messagebox.showinfo("Comic Finder",
                                        "Based on your preferences, we suggest Nowhere Men as a title of interest.")

        elif pref_list == ["Action", "Adult", "Eastern"]:
            tkinter.messagebox.showinfo("Comic Finder",
                                        "Based on your preferences, we suggest Berserk as a title of interest.")

        elif pref_list == ["Horror", "Adult", "Western"]:
            tkinter.messagebox.showinfo("Comic Finder",
                                        "Based on your preferences, we suggest Black Monday Murders as a title of interest.")

        elif pref_list == ["Action", "Children", "Eastern"]:
            tkinter.messagebox.showinfo("Comic Finder",
                                        "Based on your preferences, we suggest One Piece as a title of interest.")

        elif pref_list == ["Romance", "Adult", "Western"]:
            tkinter.messagebox.showinfo("Comic Finder",
                                        "Based on your preferences, we suggest Strangers in Paradise as a title of interest.")
        
        elif pref_list == ["Romance", "Children", "Western"]:
            tkinter.messagebox.showinfo("Comic Finder",
                                        "Based on your preferences, we suggest Archies as a title of interest.")

        elif pref_list == ["Sci-Fi", "Children", "Western"]:
            tkinter.messagebox.showinfo("Comic Finder",
                                        "Based on your preferences, we suggest The Adventures of Ender as a title of interest.")
        
        else:
            tkinter.messagebox.showinfo("Comic Finder",
                                        "A comic of those specifications has never been created. Perhaps there's a market for a talented writer/artist.")


        # DROPDOWN MENU FOR SELECTING A TITLE -----

        # Create the default window
        root = tkinter.Tk()
        root.title("Title Selection Screen")
        root.geometry('700x500')
          
        # Create the list of options
        options_list = ["Berserk", "Death Note", "Black Monday Murders", "Nowhere Men",
                        "One Piece", "Strangers in Paradise", "Archies", "The Adventures of Ender"]
          
        # Variable to keep track of the option
        # selected in OptionMenu
        value_inside = tkinter.StringVar(root)
          
        # Set the default value of the variable
        value_inside.set("Select a title to continue the process and find important stats...")
          
        # Create the optionmenu widget and passing 
        # the options_list and value_inside to it.
        question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
        question_menu.pack()
          
        # Function to print the submitted option-- testing purpose
          
        def print_answers():
            print("\nSelected Option: {}".format(value_inside.get()))
            #return None
            title = value_inside.get()
            #print(title)
                     
        # Submit button: Whenever we click the submit button, our submitted option is printed ---Testing purpose
        submit_button = tkinter.Button(root, text='Submit', command=print_answers)
        submit_button.pack()
          
        root.mainloop()

        # END OF THE DROPDOWN MENU FOR TITLE SELECTION -----



        # title list for loop -----
        
        title = value_inside.get()
        title_list.append(title)

        for item in title_list:
            print(f"Your selection list now includes {item}.")


        # invoke scrambler function -----

        scrambled_title = scrambler(title)
        print("\nIn case you need to encode the title to send to your espionage contacts spread throughout the former Soviet states, the encoded title is {word}.".format(word = scrambled_title))


        # validating input with while loop four lines below) -----

        options_list = ["Berserk", "Death Note", "Black Monday Murders", "Nowhere Men",
                        "One Piece", "Strangers in Paradise", "Archies", "The Adventures of Ender"]
        title = value_inside.get()
        ish_num = tkinter.simpledialog.askinteger("Comic Finder", "How many issues will you read?")
        while ish_num < 1:
            ish_num = tkinter.simpledialog.askinteger("Comic Finder", "Please select the number of issues.")
        #print(ish_num)
        tkinter.messagebox.showinfo("Comic Finder", f"You've selected {ish_num} issues.")

        if title == "Berserk":
            print("\nBerserk issues are $1.50 apiece.")
            issue_cost = ish_num * 1.50
            rounded_cost = "{:.2f}".format(issue_cost)
            print(f"You must pay a total of ${rounded_cost} for {ish_num} issues.")
            print("\nBerserk issues take 15 minutes to read.")
            ish_time = ish_num * 15
            print(f"You will spend {ish_time} minutes reading the {ish_num} issues.")
            count += 1
            if count == 1:
                print("\nYou have been suggested 1 title.")
            elif count >= 2:
                print(f"\nYou have been suggested {count} titles.")

        elif title == "Death Note":
            print("\nDeath Note issues are $2.50 apiece.")
            issue_cost = ish_num * 2.50
            rounded_cost = "{:.2f}".format(issue_cost)
            print(f"You must pay a total of ${rounded_cost} for {ish_num} issues.")
            print("\nDeath Note issues take 22 minutes to read.")
            ish_time = ish_num * 22
            print(f"You will spend {ish_time} minutes reading the {ish_num} issues.")
            count += 1
            if count == 1:
                print("\nYou have been suggested 1 title.")
            elif count >= 2:
                print(f"\nYou have been suggested {count} titles.")

        elif title == "Black Monday Murders":
            print("\nBlack Monday Murders issues are $3.00 apiece.")
            issue_cost = ish_num * 3.00
            rounded_cost = "{:.2f}".format(issue_cost)
            print(f"You must pay a total of ${rounded_cost} for {ish_num} issues.")
            print("\nBlack Monday Murders issues take 24 minutes to read.")
            ish_time = ish_num * 24
            print(f"You will spend {ish_time} minutes reading the {ish_num} issues.")
            count += 1
            if count == 1:
                print("\nYou have been suggested 1 title.")
            elif count >= 2:
                print(f"\nYou have been suggested {count} titles.")

        elif title == "Nowhere Men":
            print("\nNowhere Men issues are $1.25 apiece.")
            issue_cost = ish_num * 1.25
            rounded_cost = "{:.2f}".format(issue_cost)
            print(f"You must pay a total of ${rounded_cost} for {ish_num} issues.")
            print("\nNowhere Men issues take 18 minutes to read.")
            ish_time = ish_num * 18
            print(f"You will spend {ish_time} minutes reading the {ish_num} issues.")
            count += 1
            if count == 1:
                print("\nYou have been suggested 1 title.")
            elif count >= 2:
                print(f"\nYou have been suggested {count} titles.")

        elif title == "One Piece":
            print("\nOne Piece issues are $2.35 apiece.")
            issue_cost = ish_num * 2.35
            rounded_cost = "{:.2f}".format(issue_cost)
            print(f"You must pay a total of ${rounded_cost} for {ish_num} issues.")
            print("\nOne Piece issues take 13 minutes to read.")
            ish_time = ish_num * 13
            print(f"You will spend {ish_time} minutes reading the {ish_num} issues.")
            count += 1
            if count == 1:
                print("\nYou have been suggested 1 title.")
            elif count >= 2:
                print(f"\nYou have been suggested {count} titles.")

        elif title == "Strangers in Paradise":
            print("\nStrangers in Paradise issues are $3.15 apiece.")
            issue_cost = ish_num * 3.15
            rounded_cost = "{:.2f}".format(issue_cost)
            print(f"You must pay a total of ${rounded_cost} for {ish_num} issues.")
            print("\nStrangers in Paradise issues take 17 minutes to read.")
            ish_time = ish_num * 17
            print(f"You will spend {ish_time} minutes reading the {ish_num} issues.")
            count += 1
            if count == 1:
                print("\nYou have been suggested 1 title.")
            elif count >= 2:
                print(f"\nYou have been suggested {count} titles.")

        elif title == "Archies":
            print("\nArchies issues are $3.15 apiece.")
            issue_cost = ish_num * 3.15
            rounded_cost = "{:.2f}".format(issue_cost)
            print(f"You must pay a total of ${rounded_cost} for {ish_num} issues.")
            print("\nArchies issues take 12 minutes to read.")
            ish_time = ish_num * 12
            print(f"You will spend {ish_time} minutes reading the {ish_num} issues.")
            count += 1
            if count == 1:
                print("\nYou have been suggested 1 title.")
            elif count >= 2:
                print(f"\nYou have been suggested {count} titles.")

        elif title == "The Adventures of Ender":
            print("\nThe Adventures of Ender issues are $3.15 apiece.")
            issue_cost = ish_num * 3.15
            rounded_cost = "{:.2f}".format(issue_cost)
            print(f"You must pay a total of ${rounded_cost} for {ish_num} issues.")
            print("\nThe Adventures of Ender issues take 21 minutes to read.")
            ish_time = ish_num * 21
            print(f"You will spend {ish_time} minutes reading the {ish_num} issues.")
            count += 1
            if count == 1:
                print("\nYou have been suggested 1 title.")
            elif count >= 2:
                print(f"\nYou have been suggested {count} titles.")


        # wild card property -----

        wild_card = tkinter.messagebox.askyesno("Wild Card Suggestion", "Would you like a wild card?")
        if wild_card:
            random.shuffle(options_list)
            #print(options_list)
            popped_item = options_list.pop() 
            print(f"\nWhy don't you try {popped_item}?")
        else:
            print("\nMaybe some other time you'd like to try a wild card...")


        # list making from .txt files, validating input (while loop), and use of .title case to simplify string input -----

        catalog_list = list_maker("file1.txt", "r")
        code_list = list_maker("file2.txt", "r")

        choice = input("\nAn Amazon.com window will open for your convenience. For ordering purposes, enter a title to find its official ACA code: ").title()
        while choice not in catalog_list:
            choice = input("\nError. For ordering purposes, enter a title to find its official ACA code: ").title()

        index_num = catalog_list.index(choice)
        comic_code = code_list[index_num]
        print(f"\nThe ACA code for {choice} is {comic_code}.")


        # an additional web-browsing feature -----
        webbrowser.open_new_tab("https://www.amazon.com")
        #end of additional feature -----

  
        # close off the while loop
        now = datetime.datetime.now()
        program_on = tkinter.messagebox.askyesno("Comic Finder TM",
                                                 "Would you like to repeat the painful process?")

    print("\nThank you for your patronage. Have a nice day.")
    print(f"Session concluded at {now}.")
    

# scrambler function -----

import random

def scrambler(title):
    scrambler_pre_list = []
    scrambled_title = ""
    for letter in title:
        scrambler_pre_list.append(letter)
    #print(scrambler_pre_list)
    random.shuffle(scrambler_pre_list)
    #print(scrambler_pre_list)
    for item in scrambler_pre_list:
        scrambled_title += item
    return scrambled_title


# function to create lists from .txt files -----

def list_maker(data, action):
    # opening the file in read mode 
    my_file = open(data, action) 
  
    # reading the file 
    data = my_file.read() 
  
    # replacing end splitting the text  
    # when newline ('\n') is seen. 
    data_into_list = data.split("\n") 
    return data_into_list
    #my_file.close()


# invocation of the main
if __name__ == '__main__':
    main()
