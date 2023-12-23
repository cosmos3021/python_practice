import tkinter as tk

window = tk.Tk()
window.title = 'Log-in'
window.geometry('1200x700+100+10')
window.resizable(False, False)

bigmg = ('맑은 고딕', 20, 'bold')
smlmg = ('맑은 고딕', 16, 'bold')

def result() :
    if enter.get() == 'qGphJD' :
        label = tk.Label(text = '사람입니다', font = smlmg)
        label.pack()

    else :
        label = tk.Label(text = '사람이 아닙니다', font = smlmg)
        label.pack()

label = tk.Label(text = '캡챠', font = bigmg)
label.pack()

label = tk.Label(text = '사진에 나온 글씨를 입력하세요', font = smlmg)
label.pack()

img = tk.PhotoImage(file = 'captcha.png')
buttonimage = tk.Button(window, image = img)
buttonimage.pack()

enter = tk.Entry(window)
enter.place(relx = 0.5, rely = 0.3)
enter.pack()

button = tk.Button(window, text = '확인', font = smlmg, command = result)
button.pack()
enter.place(relx = 0.5, rely = 0.3)

window.mainloop()