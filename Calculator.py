import tkinter as t

# eval function : 매개변수로 받은 expression (=식)을 문자열로 받아서, 실행하는 함수
# 계산결과가 연속으로 나오도록 프로그래밍 할 필요 없음

window = None # 이름만
display_label = None
expression = ''

def press(x) : 
    global expression
    expression += str(x)
    display_label['text'] = expression

    
def press_del() : 
    global expression
    expression = expression[:len(expression)-1]
    display_label['text'] = expression
 
def press_clear() : 
    global expression
    expression = ''
    display_label['text'] = '0'
    
def press_result() : 
    global expression
    try : 
        if '÷' in expression or '×' in expression or '²' in expression: 
            expression = expression.replace('÷','/')
            expression = expression.replace('×', '*')
            expression = expression.replace('²', '**2')
            
        total = str(eval(expression))
        display_label['text'] = total
        expression = ''
        
    except :
        display_label['text'] = 'Error'
 


def create_window():
    global window
    global display_label
    
    window = t.Tk()
    window.title('Jaecal')
    window.resizable(False,False)
    # window.resizable(True,True,True) # x,y,z축을 고정시키겠다 -> 각각 False로 처리
    
    display_label = t.Label(window, textvariable = '', anchor = 'e', relief=t.SUNKEN, width = 20, font='Arial 20')
    display_label.grid(row=0, column =0, columnspan=4)
    
    btn0 = t.Button(window, text ='0', width=3, height=3, font='Arial 15', command = lambda :press(0))
    btn1 = t.Button(window, text ='1', width=3, height=3, font='Arial 15', command = lambda :press(1))
    btn2 = t.Button(window, text ='2', width=3, height=3, font='Arial 15', command = lambda :press(2))
    btn3 = t.Button(window, text ='3', width=3, height=3, font='Arial 15', command = lambda :press(3))
    btn4 = t.Button(window, text ='4', width=3, height=3, font='Arial 15', command = lambda :press(4))
    btn5 = t.Button(window, text ='5', width=3, height=3, font='Arial 15', command = lambda :press(5))
    btn6 = t.Button(window, text ='6', width=3, height=3, font='Arial 15', command = lambda :press(6))
    btn7 = t.Button(window, text ='7', width=3, height=3, font='Arial 15', command = lambda :press(7))
    btn8 = t.Button(window, text ='8', width=3, height=3, font='Arial 15', command = lambda :press(8))
    btn9 = t.Button(window, text ='9', width=3, height=3, font='Arial 15', command = lambda :press(9))
 
    btn1.grid(row=2, column=0)
    btn2.grid(row=2, column=1)
    btn3.grid(row=2, column=2)
    btn4.grid(row=3, column=0)
    btn5.grid(row=3, column=1)  
    btn6.grid(row=3, column=2)
    btn7.grid(row=4, column=0)
    btn8.grid(row=4, column=1)
    btn9.grid(row=4, column=2)
    btn0.grid(row=5, column=1)
    
    # command 뒤에는 ()를 사용하지 못하지만 lambda를 쓰면 가능함
    clearBtn = t.Button(window, text='C',width =3,height=3,font='Arial 15', command = press_clear , fg ='red')
    resultBtn = t.Button(window, text='=',width =3,height=3,font='Arial 15', command = press_result, fg = 'blue')
    addBtn = t.Button(window, text='+',width =3,height=3,font='Arial 15', command = lambda :press('+'),fg = 'blue')
    subBtn = t.Button(window, text='-',width =3,height=3,font='Arial 15', command = lambda :press('-'),fg = 'blue')
    mulBtn = t.Button(window, text='×',width =3,height=3,font='Arial 15', command = lambda :press('×'),fg = 'blue')
    divBtn = t.Button(window, text='÷',width =3,height=3,font='Arial 15', command = lambda :press('÷'),fg = 'blue')
    dotBtn = t.Button(window, text='ㆍ',width =3,height=3,font='Arial 15', command = lambda :press('.'),fg = 'blue')
    expBtn = t.Button(window, text='X²',width =3,height=3,font='Arial 15', command = lambda :press('²') ,fg = 'blue')
    delBtn = t.Button(window, text='◀',width =3,height=3,font='Arial 15', command = lambda :press_del(),fg = 'blue')
    perBtn = t.Button(window, text='%',width =3,height=3,font='Arial 15', command = lambda :press('÷100') ,fg = 'blue') # x 0.01표시
    # backspace 연산자 : 처음 ~ 나중-1 인덱스까지 슬라이싱
  
    clearBtn.grid(row=1,column=0)
    resultBtn.grid(row=5,column=2)
    addBtn.grid(row=2,column=3)
    subBtn.grid(row=3,column=3)
    mulBtn.grid(row=4,column=3)
    divBtn.grid(row=5,column=3)
    dotBtn.grid(row=5, column=0)
    expBtn.grid(row=1, column=3)
    delBtn.grid(row=1,column=1)
    perBtn.grid(row=1,column=2)
    
create_window()
window.mainloop()



    
