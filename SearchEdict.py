from tkinter import *

from tkinter import ttk

import webbrowser




root = Tk()

root.title('SearchEdict')



style = ttk.Style()

style.theme_use('winnative')




label1 = ttk.Label(root, text='Query : ')

label1.grid(row=0, column=0)

entry1 = ttk.Entry(root, width=50)

entry1.grid(row=0, column=1, columnspan=4)



btn2 = StringVar()



def callback():

   

    if btn2.get() == 'Google' and entry1.get() != '':

        webbrowser.open('http://google.com/search?q='+entry1.get())

       

    elif btn2.get() == 'Amazon' and entry1.get() != '':

        webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='+entry1.get())



    elif btn2.get() == 'youTube' and entry1.get() != '':

        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())



    elif btn2.get() == 'WallPapers' and entry1.get() != '':

        webbrowser.open('https://wallhaven.cc/search?q='+entry1.get())



    elif btn2.get() == 'News' and entry1.get() != '':

        webbrowser.open('https://news.google.com/search?for='+entry1.get())

   

    else:

        pass



def get(event):



    if btn2.get() == 'Google' and entry1.get() != '':

        webbrowser.open('http://google.com/search?q='+entry1.get())



    elif btn2.get() == 'Amazon' and entry1.get() != '':

        webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='+entry1.get())



    elif btn2.get() == 'youTube' and entry1.get() != '':

        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())



    elif btn2.get() == 'WallPapers' and entry1.get() != '':

        webbrowser.open('https://wallhaven.cc/search?q='+entry1.get())



    elif btn2.get() == 'News' and entry1.get() != '':

        webbrowser.open('https://news.google.com/search?for='+entry1.get())




    else:
         

        pass



entry1.bind('<Return>', get)



MyButton1 = ttk.Button(root, text='Search', width=10, command=callback)

MyButton1.grid(row=0, column=6)



MyButton2 = ttk.Radiobutton(root, text='Google', value='Google', variable=btn2)

MyButton2.grid(row=1, column=1, sticky=W)


MyButton3 = ttk.Radiobutton(root, text='Amazon', value='Amazon', variable=btn2)

MyButton3.grid(row=1, column=3, sticky=W)



MyButton4 = ttk.Radiobutton(root, text='YouTube', value='youTube', variable=btn2)

MyButton4.grid(row=1, column=4, sticky=E)



MyButton6 = ttk.Radiobutton(root, text='WallPapers', value='WallPapers', variable=btn2)

MyButton6.grid(row=3, column=1, sticky= W)



MyButton6 = ttk.Radiobutton(root, text='News', value='News', variable=btn2)

MyButton6.grid(row=3, column=3, sticky= W)





entry1.focus()

root.wm_attributes('-topmost', 1)

btn2.set('Google')

root.mainloop()
