
from tkinter import Tk                               #Libreria para explorador de archivos (Se usara para leer data e instrucciones)
from tkinter.filedialog import askopenfilename


class form:
    def __init__(self):
        self.tipo=""
        self.valor=""
        self.fondo=""
        self.valores=""
        self.evento=""
        self.tipo_activado=False
        self.valor_activado=False
        self.fondo_activado=False
        self.valores_activado=False
        self.evento_activado=False

    def imprimir(self):
        return {
            "tipo":self.tipo,
            "valor":self.valor,
            "fondo":self.fondo,
            "valores":self.valores,
            "evento":self.evento,
        }










class analizar_form:
    def __init__(self):
        self.lista_tokens = []
        self.texto= ""
        self.analizador()

    def leer(self):
            Tk().withdraw()
            archivodata=""
            try:
                filename = askopenfilename(title="Seleccione un archivo",
                                                filetypes=[("Archivos","*.form"), 
                                                            ("All files","*")])
                print(filename)
                with open(filename) as infile:
                    archivodata=infile.read().strip()       #limpia cualquier carracter "corrupto"
            except:
                print("no se selecciono ningun archivo")
                return
            #Lectura
            return archivodata

    def analizador(self):
        self.texto =self.leer()
        objeto=form()
        while self.texto != "":
            letra = self.leer_letra()
            if letra.isalpha() : 
                lectura = self.letras_s0()
                                         #Identificar "lo que es"
                if lectura == "valor":
                    objeto.valor_activado = True
                elif lectura == "fondo":
                    objeto.fondo_activado = True
                elif lectura == "valores":
                    objeto.valores_activado = True
                elif lectura == "evento":
                    objeto.evento_activado = True 
                
                self.lista_tokens.append(lectura)
            elif letra == "~":
                self.quitar_primera_letra()
                
                self.lista_tokens.append("~")
            elif letra == "[":
                self.quitar_primera_letra()
                
                self.lista_tokens.append("[")
            elif letra == "]":
                self.quitar_primera_letra()
                #EVENTO
                self.lista_tokens.append("]")
            elif letra == "-":
                self.quitar_primera_letra()
                
                self.lista_tokens.append("-")    
            elif letra == "<":
                self.quitar_primera_letra()
                self.lista_tokens.append("<") 
            elif letra == ">":
                self.quitar_primera_letra()
                
                self.lista_tokens.append(">")
            elif letra == ":":
                
                self.quitar_primera_letra()
                
                self.lista_tokens.append(":")
            elif letra == "'":
                self.quitar_primera_letra()
                self.lista_tokens.append("'")
            elif letra == "\"":
                self.quitar_primera_letra()
               # if lectura=="tipo":
                  #  objeto.tipo_activado = True
                
                
                self.lista_tokens.append("\"")   
            elif letra == ",":
                self.quitar_primera_letra()
                #if objeto.tipo_activado == True:
                 #   objeto.tipo_activado = False 
                 #   objeto.tipo = lectura
                self.lista_tokens.append(",")
            elif letra == "\n" or letra == "\t" or letra == " ":   
                self.quitar_primera_letra()
            else:
                self.quitar_primera_letra()
                print({"error":letra}) 
        print(self.lista_tokens)
        valor = objeto.imprimir()
        print(valor)


    def leer_letra(self):
        if(self.texto != ""):
            return self.texto[0]
        else:
            return ""
    def letras_s0(self):
        letra = self.leer_letra()
        if letra.isalpha():
            self.quitar_primera_letra()
            return letra + self.letras_s1()

    def quitar_primera_letra(self):
        if(self.texto != ""):
            self.texto=self.texto[1:]
    def letras_s1(self):
        letra = self.leer_letra()
        if letra.isalpha():
            self.quitar_primera_letra()
            return letra + self.letras_s1()
        elif letra.isnumeric():
            self.quitar_primera_letra()
            return letra + self.letras_s1()
        else:
            return "" 

a=analizar_form()