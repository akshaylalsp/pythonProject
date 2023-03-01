import tkinter as tk
import matrixInput

def main():
    windowFirst= tk.Tk()
    windowFirst.geometry('400x200')
    def callMatrixInput():
        m=int(entryM.get())
        n=int(entryN.get())
        windowFirst.destroy()
        matrixInput.inputMatrix(m,n)


        
    label1=tk.Label(windowFirst,text="enter dimension",pady=2,padx=0)
    entryM=tk.Entry(windowFirst,text='m')
    labelX=tk.Label(windowFirst,text='x')
    entryN=tk.Entry(windowFirst,text='n')
    buttonGo=tk.Button(windowFirst,text='go',command=callMatrixInput)
    label1.pack()
    entryM.pack()
    labelX.pack()
    entryN.pack()
    buttonGo.pack()


    windowFirst.mainloop()

if __name__=='__main__':
    main()