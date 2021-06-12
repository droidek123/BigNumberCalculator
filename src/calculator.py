#======================#
#      Calculator      #
#----------------------#
import Tkinter
import ctypes

equation = ""
expression = "0"
firstParameter = "0"
secondParameter = "0"
character = ""
isResult = False
mode = 1
operation = ctypes.CDLL("./operations.so")

add = operation.add
add.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]
add.restype = ctypes.c_double

subb = operation.subb
subb.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]
subb.restype = ctypes.c_double

mul = operation.mul
mul.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]
mul.restype = ctypes.c_double

divd = operation.divd
divd.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]
divd.restype = ctypes.c_double

sinassemb = operation.sinassemb
sinassemb.argtypes = [ctypes.c_double, ctypes.c_int]
sinassemb.restype = ctypes.c_double

cosassemb = operation.cosassemb
cosassemb.argtypes = [ctypes.c_double, ctypes.c_int]
cosassemb.restype = ctypes.c_double

inte = operation.inte
inte.argtypes = [ctypes.c_long]
inte.restype = ctypes.c_double

powerto = operation.powerto
powerto.argtypes = [ctypes.c_double, ctypes.c_int, ctypes.c_int]
powerto.restype = ctypes.c_double

square = operation.square
square.argtypes = [ctypes.c_double, ctypes.c_int]
square.restype = ctypes.c_double

button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}

def clear_parameters():
    global expression
    global firstParameter
    global secondParameter
    global character
    global isResult
    firstParameter = "0"
    secondParameter = "0"
    expression = "0"
    character = ""
    isResult = False
    equation.set(expression)

def clear():
    global expression
    expression = "0"

def clean():
    global expression
    expression = ""
    equation.set(expression)

def button_click(num):
    global expression
    global isResult
    if expression == "0":
        if num != ".":
            clean()
    if isResult == True:
        isResult = False
        firstParameter = "0"
    expression += str(num)
    equation.set(expression)

def charecter_click(c):
    global expression
    global firstParameter
    global character
    global isResult
    if isResult ==False:
        firstParameter = float(expression)
    else:
        isResult = False
    character = c
    clear()

def setMode(i):
    global mode
    mode = i

def equalpress():
    global expression
    global firstParameter
    global secondParameter
    global character
    global mode
    global isResult
    if character == "pow":
        secondParameter = int(expression)
    else:
        secondParameter = float(expression)
    if character == "+":
        firstParameter = operation.add(firstParameter,secondParameter,mode)
        equation.set(firstParameter)
        expression = ""
    elif character == "-":
        firstParameter = operation.subb(firstParameter,secondParameter,mode)
        equation.set(firstParameter)
        expression = ""
    elif character == "*":
        firstParameter = operation.mul(firstParameter,secondParameter,mode)
        equation.set(firstParameter)
        expression = ""
    elif character == "/":
        firstParameter = operation.divd(firstParameter,secondParameter,mode)
        equation.set(firstParameter)
        expression = ""
    elif character == "pow":
        print(firstParameter)
        print(secondParameter)
        print(mode)
        firstParameter = operation.powerto(firstParameter,mode, secondParameter)
        equation.set(firstParameter)
        expression = ""
    isResult = True
    clear()

def sinus():
    global expression
    global firstParameter
    global isResult
    if isResult == False:
        firstParameter = float(expression)
    firstParameter = operation.sinassemb(firstParameter,mode)
    equation.set(firstParameter)
    expression = ""
    isResult = True
    clear()

def cosinus():
    global expression
    global firstParameter
    global isResult
    if isResult == False:
        firstParameter = float(expression)
    firstParameter = operation.cosassemb(firstParameter,mode)
    equation.set(firstParameter)
    expression = ""
    isResult = True
    clear()

def tangens():
    global expression
    global firstParameter
    global isResult
    if isResult == False:
        firstParameter = float(expression)
    if firstParameter % 180 == 0:
        firstParameter = "0"
        equation.set(firstParameter)
    elif firstParameter % 90 == 0:
        firstParameter = "Inf"
        equation.set(firstParameter)
    else:
        firstParameter = operation.sinassemb(firstParameter,mode)/operation.cosassemb(firstParameter,mode)
        equation.set(firstParameter)
    expression = ""
    isResult = True
    clear()

def cotangens():
    global expression
    global firstParameter
    global isResult
    if isResult == False:
        firstParameter = float(expression)
    if firstParameter % 180 == 0:
        firstParameter = "Inf"
        equation.set(firstParameter)
    else:
        firstParameter = operation.cosassemb(firstParameter,mode)/operation.sinassemb(firstParameter,mode)
    equation.set(firstParameter)
    expression = ""
    isResult = True
    clear()

def integral():
    global expression
    global firstParameter
    global isResult
    clear_parameters()
    firstParameter = operation.inte(100000)
    equation.set(firstParameter)
    expression = ""
    isResult = True
    clear()

def sqrt_():
    global expression
    global firstParameter
    global isResult
    if isResult == False:
        firstParameter = float(expression)
    firstParameter = operation.square(firstParameter, mode)
    equation.set(firstParameter)
    expression = ""
    isResult = True
    clear()

# tworzenie frame
gui = Tkinter.Tk()
gui.configure(background="gray20")
gui.title("Calculator")
gui.geometry("502x444")


equation = Tkinter.StringVar()
equation.set(expression)

# Output
expression_field = Tkinter.Entry(gui, font=('sans-serif', 20, 'bold'), textvariable=equation,
                     bd=5, insertwidth = 5, bg='#BBB', justify='right').grid(columnspan=4, ipadx=40)


#Buttons
# 1 row
buttonT0 = Tkinter.Button(gui, button_params_main, text='M0',
                    command=lambda:setMode(1)).grid(row=1, column=0, sticky="nsew")
buttonT1 = Tkinter.Button(gui, button_params_main, text='M1',
                    command=lambda:setMode(2)).grid(row=1, column=1, sticky="nsew")
buttonT2 = Tkinter.Button(gui, button_params_main, text='M2',
                    command=lambda:setMode(3)).grid(row=1, column=2, sticky="nsew")
buttonT3 = Tkinter.Button(gui, button_params_main, text='M3',
                    command=lambda:setMode(4)).grid(row=1, column=3, sticky="nsew")

# 2 row
buttonSin = Tkinter.Button(gui, button_params_main, text='sin',
                  command=lambda:sinus()).grid(row=2, column=0, sticky="nsew")
buttonCos = Tkinter.Button(gui, button_params_main, text='cos',
                  command=lambda:cosinus()).grid(row=2, column=1, sticky="nsew")
buttonIntegral = Tkinter.Button(gui, button_params_main, text='tan',
                    command=lambda:tangens()).grid(row=2, column=2, sticky="nsew")
buttonPlus = Tkinter.Button(gui, button_params_main, text='ctg',
                    command=lambda:cotangens()).grid(row=2, column=3, sticky="nsew")

# 3 row
buttonSin = Tkinter.Button(gui, button_params_main, text='pow',
                    command=lambda:charecter_click("pow")).grid(row=3, column=2, sticky="nsew")
buttonCos = Tkinter.Button(gui, button_params_main, text='sqrt',
                  command=lambda:sqrt_()).grid(row=3, column=1, sticky="nsew")
buttonIntegral = Tkinter.Button(gui, button_params_main, text='int',
                  command=lambda:integral()).grid(row=3, column=0, sticky="nsew")
buttonSum = Tkinter.Button(gui, button_params_main, text=' = ',
                  command=lambda:equalpress()).grid(row=3, column=3, sticky="nsew")

# 4 row
button9 = Tkinter.Button(gui, button_params_main, text='9',
                  command=lambda:button_click(9)).grid(row=4, column=2, sticky="nsew")
button8 = Tkinter.Button(gui, button_params_main, text='8',
                  command=lambda:button_click(8)).grid(row=4, column=1, sticky="nsew")
button7 = Tkinter.Button(gui, button_params_main, text='7',
                  command=lambda:button_click(7)).grid(row=4, column=0, sticky="nsew")
buttonPlus = Tkinter.Button(gui, button_params_main, text=' + ',
                  command=lambda:charecter_click("+")).grid(row=4, column=3, sticky="nsew")

# 5 row
button6 = Tkinter.Button(gui, button_params_main, text='6',
                  command=lambda:button_click(6)).grid(row=5, column=2, sticky="nsew")
button5 = Tkinter.Button(gui, button_params_main, text='5',
                  command=lambda:button_click(5)).grid(row=5, column=1, sticky="nsew")
button4 = Tkinter.Button(gui, button_params_main, text='4',
                  command=lambda:button_click(4)).grid(row=5, column=0, sticky="nsew")
buttonMinus = Tkinter.Button(gui, button_params_main, text=' - ',
                  command=lambda:charecter_click("-")).grid(row=5, column=3, sticky="nsew")

# 6 row
button3 = Tkinter.Button(gui, button_params_main, text='3',
                  command=lambda:button_click(3)).grid(row=6, column=2, sticky="nsew")
button2 = Tkinter.Button(gui, button_params_main, text='2',
                  command=lambda:button_click(2)).grid(row=6, column=1, sticky="nsew")
button1 = Tkinter.Button(gui, button_params_main, text='1',
                  command=lambda:button_click(1)).grid(row=6, column=0, sticky="nsew")
buttonMul = Tkinter.Button(gui, button_params_main, text=' * ',
                  command=lambda:charecter_click("*")).grid(row=6, column=3, sticky="nsew")

# 7 row
buttonDot = Tkinter.Button(gui, button_params_main, text='.',
                  command=lambda:button_click(".")).grid(row=7, column=2, sticky="nsew")
button0 = Tkinter.Button(gui, button_params_main, text='0',
                  command=lambda:button_click(0)).grid(row=7, column=1, sticky="nsew")
buttonC = Tkinter.Button(gui, button_params_main, text='C',
                  command=lambda:clear_parameters()).grid(row=7, column=0, sticky="nsew")
buttonDiv = Tkinter.Button(gui, button_params_main, text=' / ',
                  command=lambda:charecter_click("/")).grid(row=7, column=3, sticky="nsew")


# Main loop xdd
gui.mainloop()
