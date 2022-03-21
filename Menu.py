
from analizar_archivo import analizar_form





class programa():
    def __init__(self):
        self.reportes()
       

    def menu(self):
        datos=analizar_form()
        
        inicio = "<html><head><link rel=\"stylesheet\" type=\"text/css\" href=\"estilo.css\" media=\"screen\" /></head><body>"
       
        print(datos.string_html)
       
        final = inicio + datos.string_html  + "</tbody></table></html></body>"
        f = open ('report_202001574.html','w')
        f.write(final)
        f.close()



    def reportes(self):
        datos=analizar_form()
        inicio = "<html><head><link rel=\"stylesheet\" type=\"text/css\" href=\"estilo.css\" media=\"screen\" /></head><body>"
        html_producto = datos.string_html+"""
            <div><button> Menu</button><select>
            <option value="value1">Value 1</option>
            <option value="value2" selected="selected">Reportes</option>
            <option value="value3">Value 3</option>
            </select></div>
            <div><textarea></textarea></div>
            <div>
            <div><button> Analizar</button></div>
            </div>
            </div>"""
        print(datos.tokens_encontados)

        print(+html_producto)


            
       
        final = inicio   + "</tbody></table></html></body>"

        f = open ('report_202001574.html','w')
        f.write(final)
        f.close()
a=programa()