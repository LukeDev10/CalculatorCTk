import customtkinter as ctk

page = ctk.CTk()
page.geometry("400x500")
page.title("Calculadora CTk")

# Configurando as extensõesda ui
page.rowconfigure([0,1,2,3,4 ], weight=1)
page.columnconfigure([0,1,2,3], weight=1)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "C","0","=","+"
]




entry = ctk.CTkEntry(page, font=("Arial", 24))
entry.grid(row=0, column=0, sticky="nsew", columnspan=4, pady=15)
entry.insert("end", "0")





def verify(char):
    txt = entry.get()

    def add(char):
        if char in "0123456789":
            if txt=="": entry.insert("end", "0")
            elif txt=="0":
                entry.delete(0, "end")
                entry.insert("end", char)
            elif txt[-1]=="0" and txt[-2] in "+-*/":
                entry.delete(len(txt)-1)
                entry.insert("end", char)
            elif txt[-1]=="/" and char=="0": return False
            else:
                entry.insert("end", char)


        elif char in ".+-*/":
            if txt[-1]==char: return False
            elif txt[-1]!=char and txt[-1] in ".+-*/":
                entry.delete(len(txt)-1)
                entry.insert("end", char)
            else:
                entry.insert("end", char)
            


# region remove
    def remove(char):
        i=0
        et = int(len(txt))
        while (i!=et):
            entry.delete(0)
            i+=1
        entry.insert("end", "0")
# endregio





    def result(txt):
        if txt=="":
            entry.insert("end", "0")
            text=0
        else:
            text = eval(txt)
        i=0
        et = int(len(txt))
        while (i!=et):
            entry.delete(0)
            i+=1
        
        entry.insert("end", text)


    if char in "0123456789.+-*/": add(char)
    elif char in "cC": remove(char)
    else: result(txt)



def keys(event):
    print(event.keysym)
    if event.keysym=="equal" or event.keysym=="Return": verify("=")
    elif event.keysym=="BackSpace" or event.keysym=="Delete": verify("c")
    elif event.char in "0123456789.+-*/": verify(event.char)
    return "break"

entry.bind("<Key>", keys)




def new_buttons():
    x=0; y=1
    for button in buttons:

        new_button = ctk.CTkButton(page, text=button, command=lambda char=button: verify(char))
        new_button.grid(row=y, column=x, sticky="nsew", pady=3, padx=3)

        if x==3: x=0; y+=1
        else: x+=1

new_buttons() # Criando os botões
page.mainloop() 





# equal and Return : "="
# BackSpace : "C"