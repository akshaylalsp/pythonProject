import echelonForm,rank,rowReduced,determinat,main
from tkinter import Tk, Label, StringVar, Button, Entry,Message,Frame


def inputMatrix(m,n):
    window = Tk()
    window.title("Matrix")
    #window.geometry("650x500+120+120")
    window.geometry('400x600')
    window.configure(bg='bisque2')
    window.resizable(False, False)

    outputFrame = Frame(window)

    def clear_frame(frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    def matrixFrame(matrix):
        clear_frame(outputFrame)
        matrix_input = Label(outputFrame, text="\n".join(["  ".join(map(str, row)) for row in matrix]))
        matrix_input.place(x=10,y=10)
        outputFrame.place(x=15,y=310,width=370,height=210)


    def message(string,value):
        clear_frame(outputFrame)
        messageFrame = Label(outputFrame,text=f"{string} of matrix is {value}")
        messageFrame.place(x=53,y=47,height=47,width=248)
        outputFrame.place(x=15,y=310,width=370,height=210)

    def detException():
        clear_frame(outputFrame)
        messageFrame1 = Label(outputFrame,text="oops!! not a square matrix")
        messageFrame1.place(x=53,y=47,height=47,width=248)
        outputFrame.place(x=15,y=310,width=370,height=210)


    # empty arrays for your Entrys and StringVars
    text_var = []
    entries = []
    
    # callback function to get your StringVars
    def get_mat():
        matrix = []
        for i in range(rows):
            matrix.append([])
            for j in range(cols):
                matrix[i].append(int(text_var[i][j].get()))

  
        return matrix
    
    def callEchelon():
        matrixFrame(echelonForm.echelon_form(get_mat()))

    def callRowReduced():
        matrixFrame(rowReduced.row_reduce(get_mat()))

    def callBack():
        window.destroy()
        main.main()



        

    def callRank():
        message("Rank",rank.rank(get_mat()))

    def callDet():
        matrix=get_mat()
        row=len(matrix)
        col=len(matrix[0])
        if row!=col:
            detException()
        else:
            result=determinat.determinant(matrix)
            message("determinant",result)

    Label(window, text="Enter matrix :", font=('arial', 10, 'bold'),bg="bisque2").place(x=20, y=20)

    x2 = 0
    y2 = 0
    rows, cols = (m,n)
    for i in range(rows):
        # append an empty list to your two arrays
        # so you can append to those later
        text_var.append([])
        entries.append([])
        for j in range(cols):
            # append your StringVar and Entry V 
            text_var[i].append(StringVar())
            entries[i].append(Entry(window, textvariable=text_var[i][j],width=3))
            entries[i][j].place(x=60 + x2, y=50 + y2)
            x2 += 30

        y2 += 30
        x2 = 0


    # button= Button(window,text="Submit", bg='bisque3', width=15, command=get_mat)
    # button.place(x=160,y=300)
    buttonRRF=Button(window,text='RRF',command=callRowReduced)
    buttonEch=Button(window,text='EchelonForm',command=callEchelon)
    buttonRank=Button(window,text='Rank',command=callRank)
    buttonDeterminant=Button(window,text='Determinat',command=callDet)
    buttonBack=Button(window,text='Back',command=callBack)
    # buttonReset=Button(window,text='Reset')
    buttonRRF.place(x=20,y=571,width=70,height=25)
    buttonEch.place(x=110,y=571,width=70,height=25)
    buttonRank.place(x=210,y=571,width=70,height=25)
    buttonDeterminant.place(x=300,y=571,width=70,height=25)
    buttonBack.place(x=45,y=536,width=70,height=25)
    # buttonReset.place(x=280,y=536,width=70,height=25)


    

    window.mainloop()