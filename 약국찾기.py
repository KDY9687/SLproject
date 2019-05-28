from tkinter import*
from tkinter import font
import tkinter.messagebox

m_Tk = Tk()
m_Tk.geometry("400x600")

def InitTopText():
    TempFont =  font.Font(m_Tk, size = 15, weight = 'bold', family = 'Consolas')
    MainText = Label(m_Tk, font = TempFont, text = "약국 검색 프로그램 ")
    MainText.pack()
    MainText.place(x = 110)

def initSearchListBox():
    pass

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(m_Tk, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(m_Tk, font = TempFont, width = 20, borderwidth = 8, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x = 25, y = 55)

    InputLabel1 = Entry(m_Tk, font = TempFont, width = 20, borderwidth = 8, relief = 'ridge')
    InputLabel1.pack()
    InputLabel1.place(x=25, y=105)

def InitButton():
    TempFont = font.Font(m_Tk, size=15, weight='bold', family = 'Consolas')
    SearchButton = Button(m_Tk, font = TempFont, text = "검색", command = SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x = 300, y = 55)

    SearchByDayButton = Button(m_Tk, font = TempFont, text = "요일")
    SearchByDayButton.pack()
    SearchByDayButton.place(x = 300, y = 105)

    UpdateDB = Button(m_Tk, font = TempFont, text = "갱신")
    UpdateDB.pack()
    UpdateDB.place(x = 300, y = 155)


def SearchButtonAction():
    global SearchListBox

    RenderText.configure(state = 'normal')
    RenderText.delete(0.0, END)
    initSearchIndex = SearchListBox.curselection()[0]

    RenderText.configure(state = 'disabled')

def IniteRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(m_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x = 375, y = 200)

    TempFont = font.Font(m_Tk, size=10, family='Consolas')
    RenderText = Text(m_Tk, width=49, height=27, borderwidth=12, relief='ridge',
                      yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')

InitTopText()
InitInputLabel()
InitButton()
#SearchButtonAction()
IniteRenderText()
m_Tk.mainloop()