
from operator import le
from tkinter import Y, Tk                               #Libreria para explorador de archivos (Se usara para leer data e instrucciones)
from tkinter.filedialog import askopenfilename
from urllib.parse import parse_qs


class form:
    def __init__(self):
        self.tipo=""
        self.valor=""
        self.fondo=""
        self.valores=[]
        self.evento=""
        self.nombre=""
        self.tipo_activado=False
        self.valor_activado=False
        self.fondo_activado=False
        self.valores_activado=False
        self.evento_activado=False
        self.nombre_activado=False
        self.datos=[]

    def imprimir(self):
        return {
            "tipo":self.tipo,
            "valor":self.valor,
            "fondo":self.fondo,
            "valores":self.valores,
            "evento":self.evento,
        }

    def imprimir_datos(self):
        return {
            "Estos son los datos":self.datos,
        }


class datoformulario:
    def __init__(self):
        self.nombre = ""
        self.numericos = []
        

    def imprimir(self):
        #print("//////////",self.nombre,self.numericos,"//////////")
        pass









class analizar_form:
    def __init__(self):
        self.lista_tokens = []
        self.texto= ""
        self.lista_formualrios=[]
        self.string_html=""
        self.analizador()
        self.linea=0

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
        self.linea=0
        self.string_html = ""
        self.texto =self.leer()
        objeto=form()
        clase = datoformulario()
        self.tokens_encontados=""
        while self.texto != "":
            letra = self.leer_letra()
            if letra.isalpha() : 
                lectura = self.letras_s0()
                                         #Identificar "lo que es"
                
                if lectura=="tipo":
                    objeto.tipo_activado = True
                elif lectura == "valor":
                    objeto.valor_activado = True
                elif lectura == "fondo":
                    objeto.fondo_activado = True
                elif lectura == "evento":
                    objeto.evento_activado = True
                elif lectura == "nombre":
                    objeto.nombre_activado = True
                elif lectura == "valores":
                    objeto.valores_activado = True
                


                self.lista_tokens.append(lectura)

            elif letra == "~":
                self.quitar_primera_letra()
                
                self.lista_tokens.append("~")
            elif letra == "[":
                self.quitar_primera_letra()
                objeto.valores=[]
                self.lista_tokens.append("[")
            elif letra == "]":
                

                self.quitar_primera_letra()
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

                if objeto.tipo != "":
                    #print(objeto.tipo,objeto.valor)
                    self.string_html = self.string_html + self.tipo_valor(objeto.tipo,objeto.valor,objeto.fondo,objeto.nombre,objeto.valores)
                    objeto.tipo = ""
                    #print(objeto.valores)
                    #print(self.string_html)
                
                   
                   
                
                if objeto.evento_activado == True:
                    objeto.evento_activado = False  #TIPO
                    objeto.evento = lectura
                    #print(lectura)

                




            elif letra == ":":
                self.quitar_primera_letra()
                self.lista_tokens.append(":")
            elif letra == "'":
                lectura = self.comillas_s0()
                #print(lectura)
                
                objeto.valores.append(lectura) 
                #print(objeto.valores)
                self.lista_tokens.append(lectura)



                
            elif letra == "\"" :
                
               
                

                lectura = self.comillas_s0()
                if objeto.tipo_activado == True:
                    objeto.tipo_activado = False  #TIPO
                    objeto.tipo = lectura
                   # print(lectura)
                elif objeto.valor_activado == True:
                    objeto.valor_activado = False #valor
                    objeto.valor = lectura
                elif objeto.fondo_activado == True:
                    objeto.fondo_activado = False #fondo
                    objeto.fondo = lectura
                
                elif objeto.nombre_activado == True:
                    objeto.nombre_activado = False #nombre
                    objeto.nombre = lectura
                    #print(lectura)    


                self.lista_tokens.append(lectura)
            elif letra == ",":
                self.quitar_primera_letra()
                
                

                       
                self.lista_tokens.append(",")
            elif letra == "\n" or letra == "\t" or letra == " ":
                if letra== "\n":
                   # print(lectura)
                    self.linea=self.linea+1
                    self.tokens_encontados= self.reportes(self.linea,self.lista_tokens)
                   # print(self.linea)
                self.quitar_primera_letra()

            else:
                self.quitar_primera_letra()
                print({"error":letra}) 
        #print(self.lista_tokens)
        #valor = objeto.imprimir()
       # print(valor)
        
                

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
    def comillas_s0(self):
        letra = self.leer_letra()
        if letra == '\"' or letra == "“" or letra == "”" or letra == "'":
            self.quitar_primera_letra()
            return letra +  self.comillas_s1()
    def comillas_s1(self):
        letra = self.leer_letra()
        if letra != '\"'and letra != "“" and letra != "”" and letra != "'":
            self.quitar_primera_letra()
            return letra + self.comillas_s1()
        else:
            self.quitar_primera_letra()
            return letra

    def valor(self,objeto_valor):
        objeto=objeto_valor
        if objeto != " ":
            return objeto
    def tipo_valor(self,tipo,valor,fondo,nombre,valores):
        valor=valor.replace("\"","")
        if tipo == "\"etiqueta\"":
            return "<div><label>"+self.valor(valor)+"</label></div>"
        elif tipo == "\"texto\"":
            fondo=fondo.replace("\"","")
            x="<div> <input type=\"text\"  placeholder=\""+self.valor(fondo)+"\"> </div>"
            return x
        elif tipo == "\"grupo-radio\"":
            nombre=nombre.replace("\"","")
            #print(valores)
            string=""
            for elemento in valores:
                valorNuevo = elemento.replace("\'","")
                #print("###########")
               # print(valorNuevo)
                string=string+"<input type=\"checkbox\" />"+valorNuevo + "<label>"
                
            y="<div><label>"+self.valor(nombre)+":"+"</label>"+string+"</div>"
            return y
        elif tipo == "\"grupo-option\"":
            #print(valores)
            nombre=nombre.replace("\"","")
            string=""
            x=0
            for elemento in valores:
                valorNuevo = elemento.replace("\'","")
                string=string+"<option value="+str(x)+">"+valorNuevo+"</option>"
                x=x+1
            y="<div><label>"+self.valor(nombre)+":"+"</label><select name=\"select\">"+string+"</select></div>"
            return y
        elif tipo == "\"boton\"":
            valor=valor.replace("\"","")
            l="<div><button>"+valor+"</button></div>"
            #print(l)

            return l

        else:
            #print({"errro_valor":tipo})
            return ""

    def reportes(self,linea,tokens):
        linea=linea
        tokens_detectados=""
        for i in tokens:
            tokens_detectados=tokens_detectados+i
            print(i)
            return tokens_detectados
       


    
    
        

     

#a=analizar_form()