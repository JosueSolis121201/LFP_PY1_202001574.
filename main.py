import tkinter as tk
from analizar_archivo import analizar_form
from tkinter import END


class tkinter:
    def __init__(self):
        self.textExample=""
        self.lectura=None
        


        root = tk.Tk()
        root.geometry("500x300")
        self.raiz = root
   

        self.textExampl=tk.Text(root, height=10)
        self.textExampl.pack()
        self.textExampl.insert('1.0', 'Reporte de tokens')
        btnRead=tk.Button(root, height=1, width=12, text="Reporte Errores", command=self.getTextInput2)
                            
        btnRead.pack()

        menu=tk.Button(root, height=1, width=12, text="Reporte Tokens", command=self.getTextInput)
                        
        menu.pack()

        submitButton = tk.Button(root,height=1, width=12, command=self.cargar_datos, text="Cargar datos")
        submitButton.pack()
        root.mainloop()

    def getTextInput(self): 
        self.textExampl.delete('1.0', END)
        valor = self.lectura.reportes()
        self.textExampl.insert('1.0',valor)
    
    def getTextInput2(self): 
        self.textExampl.delete('1.0', END)
        valor = self.lectura.reportes_errores()
        self.textExampl.insert('1.0',valor)


    def cargar_datos(self):
        self.lectura = analizar_form()

        


a=tkinter()





