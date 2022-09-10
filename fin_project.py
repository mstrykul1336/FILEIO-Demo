#Mikinzi Strykul
#Mental Health Project
#imports the time module to use in the journal
import time
#imports the time module part that will actually calculate it into readable characters
from time import ctime
mood_scale_list=5
print('Welcome to the Mental Health Recording Journal.')
start=input('Would you like to start for today? (Y/N?)')
while start=='Y':
    for i in range(0,1):
        #this creates a file to write the journal and mood into, append to make sure it doesn't overwrite the old information
        f= open("daily_journal.txt","a")
        f.write (ctime())
        #writes the current time of the PC
        f.write ('   \n')
        f.close
        print('What is your mood rating for today')
        mood_scale=input('Input the number between 1 and 9, 1 being the worst day ever and 9 being the best.')
        f= open("daily_journal.txt","a")
        f2=open("mood_numbers.txt","a")
        #this txt file contains just the numbers for the plot later
        f2.write(mood_scale)
        f2.write('  ')
        f2.close()
        f.write("Today's mood rating is, "+ mood_scale,)
        f.write('    \n')
        f.close()
        print('Time to journal the thoughts for the day!')
        journal=input('Journal those thoughts:')
        f= open("daily_journal.txt","a")
        f.write(journal)
        f.write('  \n')
        f.close()
    break
#if the user says anything but 'Y', it will cancel the program
else:
    print('Thank you for time. Have a good day!')
    exit()
#this function is used to bring up the journals and advice
def previous_journals_func():
    print('Alright. I am going to bring up the previous journals for you.')
    with open('daily_journal.txt') as f:
          journal_contents=f.read()
          print(journal_contents)
          print('---------------------------------------------')
          print('If you need help immediately, contact the suicide hotline: 800-273-8255')
          print("Let's learn a breathing technique! First, we are going to breathe around the shape of the Python shell.")
          print("Start at the top, where it says *Python 3.8.2 Shell* breathing in across that line.")
          print("Then, go down the side of the box while holding in that deep breath.")
          print("On the bottom of the block, breathe it out and keep pushing it all out as you go to the other side and return to the top.")
          print("Repeat as needed! This is breathing around a square and helps to control deep breathing!")
          print("Everything will be alright, thank you for taking care of yourself!")
          
con=input('Would you like to see the graph progress of your moods that are journaled for this week? (Y/N)? (Only do this if you have 7 entries!)')
if con=='Y':
    #numpy and matplotlib are used to create the graph and numpy is used to take the seven numbers from the scale and convert them
    import matplotlib.pyplot
    import matplotlib.pyplot as plt
    import numpy as np
    days=[1,2,3,4,5,6,7]
    #this opens the numbers file for Python to read the values and put them into the graph
    f2=open("mood_numbers.txt","r")
    mood_numbers=f2.read()
    mood_plot=np.loadtxt('mood_numbers.txt')
    #all of this info in the plt.plot tells the plot what it needs to look like
    plt.plot(days,mood_plot, color='blue', linestyle='solid', linewidth='2', marker='o', markerfacecolor='red')
    plt.ylabel('Mood Scale (1-10)')
    plt.xlabel('Days')
    plt.title('Journalized Mood Scales')
    plt.show()
    previous_journals_func()
else:
    previous_journals_func()



        

