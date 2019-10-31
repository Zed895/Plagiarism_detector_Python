#A common problem in academic settings is plagiarism
#detection. Fortunately, software can make this pretty easy!
#
#In this problem, you'll be given two files with text in
#them. Write a function called check_plagiarism with two
#parameters, each representing a filename. The function
#should find if there are any instances of 5 or more
#consecutive words appearing in both files. If there are,
#return the longest such string of words (in terms of number
#of words, not length of the string). If there are not,
#return the boolean False.
#
#For simplicity, the files will be lower-case text and spaces
#only: there will be no punctuation, upper-case text, or
#line breaks.
#
#We've given you three files to experiment with. file_1.txt
#and file_2.txt share a series of 5 words: we would expect
#check_plagiarism("file_1.txt", "file_2.txt") to return the
#string "if i go crazy then". file_1.txt and file_3.txt
#share two series of 5 words, and one series of 11 words:
#we would expect check_plagiarism("file_1.txt", "file_3.txt")
#to return the string "i left my body lying somewhere in the
#sands of time". file_2.txt and file_3.txt do not share any
#text, so we would expect check_plagiarism("file_2.txt",
#"file_3.txt") to return the boolean False.
#
#Be careful: there are a lot of ways to do this problem, but
#some would be massively time- or memory-intensive. If you
#get a MemoryError, it means that your solution requires
#storing too much in memory for the code to ever run to
#completion. If you get a message that says "KILLED", it
#means your solution takes too long to run.


#Add your code here!
def check_plagiarism(file1, file2):
    
    file1 = open(file1)
    myString1 = file1.read()
    myString1 = myString1.lower()
    splitted_words_1_for_list_method = myString1.split(" ")
    file1.close()
    
    file2 = open(file2)
    myString2 = file2.read()
    myString2 = myString2.lower()
    file2.close() 
    
    eleje = 0
    vege = 5
    kozos_list = []
    for i in range(0,10000):
        ellenorzendo = splitted_words_1_for_list_method[eleje:vege] 
        string_ellenorzendo = " ".join(ellenorzendo)
        if string_ellenorzendo in myString2:
            if string_ellenorzendo not in kozos_list:
                kozos_list.append(string_ellenorzendo)
            vege +=1
        else:
            eleje +=1
            vege = eleje+5
    
    #It is looking for the length of the longest element (in chars):
    leghosszabb_hossza = 5
    for item in kozos_list:
        if len(item) > leghosszabb_hossza:
            leghosszabb_hossza = len(item)
    

    #It is looking for the longest element(s):
    leghosszabb_elem = []
    for item in kozos_list:
        if len(item) == leghosszabb_hossza:
            split_item_list = item.split() #It checks if the length of the words are above 4.
            if len(split_item_list) > 4:
                leghosszabb_elem.append(item) 
   
    #If there is an at least 5 words long element in the common list then it prints it: 
    if len(leghosszabb_elem) > 0:
        return messagebox.showinfo("Plagiarized part:",leghosszabb_elem)
    else:
        return messagebox.showinfo("Plagiarized part:","I did not find plagiarism.")

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os

application_window = tk.Tk()
szoveg = "\n Select a text file to check, then those files which against you want to compare the first file.\n"
my_label = ttk.Label(application_window, text = szoveg)
my_label.grid(row =1, column=1)
application_window.geometry('580x100+250+250')
application_window.title("Plagiarism detector.")
application_window.start_button = tk.Button(text="Start")
application_window.start_button.grid(row = 10, column = 1, )

def start():
    my_filetypes = [('all files', '*'), ('text files', '.txt')]

    answer = filedialog.askopenfilename(parent=application_window,
                                        initialdir=os.getcwd(),
                                        title="File to check:",
                                        filetypes=my_filetypes)


    answer2 = filedialog.askopenfilenames(parent=application_window,
                                         initialdir=os.getcwd(),
                                         title="Against which files do you want it to be compared?",
                                         filetypes=my_filetypes)
    for i in range(len(answer2)):
        check_plagiarism(answer, answer2[i])
        
application_window.start_button['command'] = start





    
