from tkinter import *
import turtle
import random

root = Tk()
flagW=False
flagL=False
flafA=False
flagWr=False
gameFlag=True
wrongCount=0
word_space_position=[]

user_list_correct  = []
user_list_wrong = []
user_input=[]
dash=[]
letter=[]
root.configure(background="black")
root.geometry('1920x1080')

hmTC=(0,0)
hm=turtle.Turtle()
hm.speed(0)
state=turtle.Turtle()
state.ht()
def correct():
        state.clear()
        state.color("green")
        state.write("Correct!!",font=("Arial",50,"bold"))
def lose():
    state.clear()
    state.color("blue")
    state.write("YOU LOSE!!", font=("Arial",50,"bold"))
    cordxy=letter[0].pos()
    temp=turtle.Turtle()
    temp.ht()
    temp.speed(0)
    temp.color("blue")
    temp.penup()
    temp.setpos(cordxy[0],cordxy[1]+60)
    temp.pendown()
    temp.write("The word is : ", word,align="left",font=("Arial", 20, "bold"))         
    for i in range(len(word)):
        if(word[i] not in user_list_correct):
            letter[i].color("red")
            letter[i].write(word[i],align="left",font=("Arial", 20, "bold"))


def evaluate(word,user_input):
    global wrongCount
    global gameFlag
    if(gameFlag==True):
        if(user_input in word and user_input not in user_list_correct):
            tempPositionList=[]
            for i in range(len(word)):
                if(word[i]==user_input):
                    letter[i].write(user_input,align="left", font=("Arial", 20, "bold"))
                    user_list_correct.append(user_input)
                    tempPositionList.append(i)
                    correct()                    
                    if(len(user_list_correct)==len(word)):
                        win()
                        gameFlag=False 
    #return tempPositionList
        else:
            if(user_input in user_list_correct):
                already()
            else:
                wrong()
                user_list_wrong.append(user_input)
                wrongCount+=1
                if(wrongCount>=9):
                    lose()
                    gameFlag=False
                Hangman(wrongCount)

def win():
        state.clear()
        state.color("brown")
        state.write("YOU WIN!!", font=("consolas",50,"bold"))
def already():  
        state.clear()
        state.color("green")
        state.write("Already in use!", font=("consolas",50,"bold"))
def wrong():
        state.clear()
        state.color("red")
        state.write("wrong!!", font=("Arial",30,"bold"))
        
def A():
    evaluate(word,"A")
def B():
    evaluate(word,"B")
def C():
    evaluate(word,"C")
def D():
    evaluate(word,"D")
def E():
    evaluate(word,"E")
def F():
    evaluate(word,"F")
def G():
    evaluate(word,"G")
def H():
    evaluate(word,"H")
def I():
    evaluate(word,"I")
def J():
    evaluate(word,"J")
def K():
    evaluate(word,"K")
def L():
    evaluate(word,"L")
def M():
    evaluate(word,"M")
def N():
    evaluate(word,"N")
def O():
    evaluate(word,"O")
def P():
    evaluate(word,"P")
def Q():
    evaluate(word,"Q")
def R():
    evaluate(word,"R")
def S():
    evaluate(word,"S")
def T():
    evaluate(word,"T")
def U():
    evaluate(word,"U")
def V():
    evaluate(word,"V")
def W():
    evaluate(word,"W")
def X():
    evaluate(word,"X")
def Y():
    evaluate(word,"Y")
def Z():
    evaluate(word,"Z")
    #function which controls the drawing of hangman figure.
def Hangman(num):
        global hmTC
        if(num==0):
                hm.penup()
                hm.setpos(-670,-340)
                hm.pendown()
                hm.ht()
                hm.begin_fill()
                hm.fd(400)
                hm.lt(90)
                hm.fd(50)
                hm.lt(90)
                hm.fd(390)
                hm.rt(90)
                hm.fd(600)
                hm.rt(90)
                hm.fd(400)
                hm.rt(90)
                hm.fd(20)
                hm.lt(90)
                hm.fd(10)
                hm.lt(90)
                hmTC=hm.pos()
                hm.fd(30)              
                hm.lt(90)
                hm.fd(420)
                hm.lt(90)
                hm.fd(550)
                hm.end_fill()        
                hm.pensize(5)
        elif(num==1):
                hm.penup()
                hm.setpos(hmTC[0],hmTC[1])
                hm.rt(90)
                hm.pendown()
                hm.circle(40)
               
        elif(num==2):
                hm.penup()
                hm.setpos(hmTC[0],hmTC[1]-80)
                hm.lt(90)
                hm.pendown()
                hm.fd(140)
                hmTC=hm.pos()
        elif(num==3):
                hm.penup()
                hm.rt(30)
                hm.pendown()
                hm.fd(100)
                hm.rt(60)
                hm.fd(10)
                hm.penup()
                hm.rt(180)
                hm.fd(10)
                hm.rt(30)
                hm.fd(100)
                hm.rt(90)
                hm.pendown()
        elif(num==4):
                hm.penup()
                hm.setpos(hmTC[0],hmTC[1])
                
                hm.pendown()
                hm.lt(60)
                hm.fd(100)
                hm.lt(60)
                hm.fd(10)
                      
        elif(num==5):
                hm.penup()
                hm.setpos(hmTC[0],hmTC[1])
                hm.lt(90)
                hm.fd(90)
                hm.lt(180)
                hm.rt(30)
                hm.pendown()
                hm.fd(80)
                hm.rt(60)      
        elif(num==6):
                hm.penup()
                hm.setpos(hmTC[0],hmTC[1])
                hm.rt(90)
                hm.fd(90)
                hm.lt(180)
                hm.lt(30)
                hm.pendown()
                hm.fd(80)        
        elif(num==7):
                hm.penup()
                hm.setpos(-235.00,265.00)
                hm.rt(90)
                hm.pendown()
                hm.circle(4)
        elif(num==8):
                hm.penup()
                hm.setpos(-265,265.00)
                hm.rt(90)
                hm.pendown()
                hm.circle(4)
        else:
            hm.penup()
            hm.setpos(hm.pos()[0]+25,hm.pos()[1]-35)
            hm.pendown()
            hm.rt(30)
            hm.circle(10,180)
    #creates boxes to type characters in    
def createDash(num):
        for i in range(num):
            dash.append(turtle.Turtle())
            dash[i].color("#800000","white")
            dash[i].pensize(4)
            letter.append(turtle.Turtle())      
            dash[i].ht()
            dash[i].speed(0)
            letter[i].ht()      
            dash[i].penup()
            letter[i].penup()       
            dash[i].setpos(-600+i*50,-200)
            letter[i].setpos(-595+i*50,-200)        
            dash[i].pendown()
            letter[i].pendown()
            if(i in word_space_position):
                        dash[i].penup()
                        continue
            dash[i].begin_fill()
            dash[i].fd(50)
            dash[i].lt(90)
            dash[i].fd(55)
            dash[i].lt(90)
            dash[i].fd(50)
            dash[i].lt(90)
            dash[i].fd(55)
            dash[i].end_fill()
        return letter   
  
def easy():
    #han()
    global word
    root.destroy()
    f = open("easy.txt")
    word_list=[]
    for line in f:
        line = line.strip()
        word_list.append(line)
    wor = random.choice(word_list)
    wor=wor.upper()
    l = len(wor)
      
    word = list(wor)
    
    for c in range(len(word)):
        if(word[c]==' '):
            word_space_count+=1
            word_space_position.append(c)
            user_list_correct.append(' ')
    wn = turtle.Screen()
    wn.setup (width=1920,height=1080, startx=0, starty=0)
    wn.bgcolor("yellow")
    wn.tracer(2)
    Hangman(0)
    letter = createDash(len(word))
    wn.tracer(1)
    wn.onkey(A,"a")
    wn.onkey(B,"b")
    wn.onkey(A,"a")
    wn.onkey(A,"A")
    wn.onkey(B,"b")
    wn.onkey(B,"B")
    wn.onkey(C,"c")
    wn.onkey(C,"C")
    wn.onkey(D,"d")
    wn.onkey(D,"D")
    wn.onkey(E,"e")
    wn.onkey(E,"E")
    wn.onkey(F,"f")
    wn.onkey(F,"F")
    wn.onkey(G,"g")
    wn.onkey(G,"G")
    wn.onkey(H,"h")
    wn.onkey(H,"H")
    wn.onkey(I,"i")
    wn.onkey(I,"I")
    wn.onkey(J,"j")
    wn.onkey(J,"J")
    wn.onkey(K,"k")
    wn.onkey(K,"K")
    wn.onkey(L,"l")
    wn.onkey(L,"L")
    wn.onkey(M,"m")
    wn.onkey(M,"M")
    wn.onkey(N,"n")
    wn.onkey(N,"N")
    wn.onkey(O,"o")
    wn.onkey(O,"O")
    wn.onkey(P,"p")
    wn.onkey(P,"P")
    wn.onkey(Q,"q")
    wn.onkey(Q,"Q")
    wn.onkey(R,"r")
    wn.onkey(R,"R")
    wn.onkey(S,"s")
    wn.onkey(S,"S")
    wn.onkey(T,"t")
    wn.onkey(T,"T")
    wn.onkey(U,"u")
    wn.onkey(U,"U")
    wn.onkey(V,"v")
    wn.onkey(V,"V")
    wn.onkey(W,"w")
    wn.onkey(W,"W")
    wn.onkey(X,"x")
    wn.onkey(X,"X")
    wn.onkey(Y,"y")
    wn.onkey(Y,"Y")
    wn.onkey(Z,"z")
    wn.onkey(Z,"Z")
    if(gameFlag==True):
        wn.listen()
    #turtle.done()
def medium():
    #han()
    global word
    root.destroy()
    f = open("medium.txt")
    word_list=[]
    for line in f:
        line = line.strip()
        word_list.append(line)
    wor = random.choice(word_list)
    wor=wor.upper()
    l = len(wor)
      
    word = list(wor)
    
    for c in range(len(word)):
        if(word[c]==' '):
            word_space_count+=1
            word_space_position.append(c)
            user_list_correct.append(' ')
    wn = turtle.Screen()
    wn.setup (width=1920,height=1080, startx=0, starty=0)
    wn.bgcolor("yellow")
    wn.tracer(2)
    Hangman(0)
    letter = createDash(len(word))
    wn.tracer(1)
    wn.onkey(A,"a")
    wn.onkey(B,"b")
    wn.onkey(A,"a")
    wn.onkey(A,"A")
    wn.onkey(B,"b")
    wn.onkey(B,"B")
    wn.onkey(C,"c")
    wn.onkey(C,"C")
    wn.onkey(D,"d")
    wn.onkey(D,"D")
    wn.onkey(E,"e")
    wn.onkey(E,"E")
    wn.onkey(F,"f")
    wn.onkey(F,"F")
    wn.onkey(G,"g")
    wn.onkey(G,"G")
    wn.onkey(H,"h")
    wn.onkey(H,"H")
    wn.onkey(I,"i")
    wn.onkey(I,"I")
    wn.onkey(J,"j")
    wn.onkey(J,"J")
    wn.onkey(K,"k")
    wn.onkey(K,"K")
    wn.onkey(L,"l")
    wn.onkey(L,"L")
    wn.onkey(M,"m")
    wn.onkey(M,"M")
    wn.onkey(N,"n")
    wn.onkey(N,"N")
    wn.onkey(O,"o")
    wn.onkey(O,"O")
    wn.onkey(P,"p")
    wn.onkey(P,"P")
    wn.onkey(Q,"q")
    wn.onkey(Q,"Q")
    wn.onkey(R,"r")
    wn.onkey(R,"R")
    wn.onkey(S,"s")
    wn.onkey(S,"S")
    wn.onkey(T,"t")
    wn.onkey(T,"T")
    wn.onkey(U,"u")
    wn.onkey(U,"U")
    wn.onkey(V,"v")
    wn.onkey(V,"V")
    wn.onkey(W,"w")
    wn.onkey(W,"W")
    wn.onkey(X,"x")
    wn.onkey(X,"X")
    wn.onkey(Y,"y")
    wn.onkey(Y,"Y")
    wn.onkey(Z,"z")
    wn.onkey(Z,"Z")
    if(gameFlag==True):
        wn.listen()
def hard():
    global word
    root.destroy()
    f = open("hard.txt")
    word_list=[]
    for line in f:
        line = line.strip()
        word_list.append(line)
    wor = random.choice(word_list)
    wor=wor.upper()
    l = len(wor)
    word = list(wor)
    for c in range(len(word)):
        if(word[c]==' '):
            word_space_count+=1
            word_space_position.append(c)
            user_list_correct.append(' ')
    wn = turtle.Screen()
    wn.setup (width=1920,height=1080, startx=0, starty=0)
    wn.bgcolor("yellow")
    wn.tracer(2)
    Hangman(0)
    letter = createDash(len(word))
    wn.tracer(1)
    wn.onkey(A,"a")
    wn.onkey(B,"b")
    wn.onkey(A,"a")
    wn.onkey(A,"A")
    wn.onkey(B,"b")
    wn.onkey(B,"B")
    wn.onkey(C,"c")
    wn.onkey(C,"C")
    wn.onkey(D,"d")
    wn.onkey(D,"D")
    wn.onkey(E,"e")
    wn.onkey(E,"E")
    wn.onkey(F,"f")
    wn.onkey(F,"F")
    wn.onkey(G,"g")
    wn.onkey(G,"G")
    wn.onkey(H,"h")
    wn.onkey(H,"H")
    wn.onkey(I,"i")
    wn.onkey(I,"I")
    wn.onkey(J,"j")
    wn.onkey(J,"J")
    wn.onkey(K,"k")
    wn.onkey(K,"K")
    wn.onkey(L,"l")
    wn.onkey(L,"L")
    wn.onkey(M,"m")
    wn.onkey(M,"M")
    wn.onkey(N,"n")
    wn.onkey(N,"N")
    wn.onkey(O,"o")
    wn.onkey(O,"O")
    wn.onkey(P,"p")
    wn.onkey(P,"P")
    wn.onkey(Q,"q")
    wn.onkey(Q,"Q")
    wn.onkey(R,"r")
    wn.onkey(R,"R")
    wn.onkey(S,"s")
    wn.onkey(S,"S")
    wn.onkey(T,"t")
    wn.onkey(T,"T")
    wn.onkey(U,"u")
    wn.onkey(U,"U")
    wn.onkey(V,"v")
    wn.onkey(V,"V")
    wn.onkey(W,"w")
    wn.onkey(W,"W")
    wn.onkey(X,"x")
    wn.onkey(X,"X")
    wn.onkey(Y,"y")
    wn.onkey(Y,"Y")
    wn.onkey(Z,"z")
    wn.onkey(Z,"Z")
    if(gameFlag==True):
        wn.listen()


mylabel=Label(root,text="choose your option",padx=200,pady=50,bg="orange", fg= "black" , font=("consolas",18,"bold")).place(x=580,y=100)
button1=Button(root,text="EASY",padx=70, pady =30 , bg = "light sky blue" , fg= "black" , font=("consolas",16,"bold"),command=easy).place(x=550,y=450)
button2=Button(root,text="MEDIUM",padx=51, pady =30 , bg = "light sky blue" , fg= "black" , font=("consolas",16,"bold"),command=medium).place(x=850,y=450)
button3=Button(root,text="HARD",padx=70, pady =30 , bg = "light sky blue" , fg= "black" , font=("consolas",16,"bold"),command=hard).place(x=1150,y=450)
root.mainloop()