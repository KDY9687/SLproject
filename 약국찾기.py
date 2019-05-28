from tkinter import*
from tkinter import font
import  tkinter.messagebox

m_Tk = Tk()
m_Tk.geometry("400x600")

def IniteTopText():
    TempFont =  font.Font(m_Tk, size = 15, weight = 'bold', family = 'Consolas')
    MainText = Label(m_Tk, font = TempFont, text = "약국 검색 프로그램 ")
    MainText.pack()
    MainText.place(x = 110)

IniteTopText()
m_Tk.mainloop()