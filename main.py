from javax.swing import JFrame
from javax.swing import JMenuBar
from javax.swing import JMenuItem
from javax.swing import JScrollPane
from javax.swing import JMenu 
from javax.swing import JTextArea
from javax.swing import JFileChooser    
from archivos import *
from lexico_sintactico.analizador_lexicotest import *
from info.informacion import *
from lexico_sintactico.analizador_sintactico import *
from io import open

###########################################################################
###########################################################################
#####   Metacompilador utlizando la libreria swing de java             ####
#####   Primera version del metacompilador  :(                         ####
#####   @Autor VictorJX                                                ####
#####                                                                  ####
#####                                                                  ####
###########################################################################
###########################################################################


class main(JFrame):
    def __init__(self):
        super(main,self).__init__()
        self.Config()
        self.windows()
        self.ruta=""

    def windows(self):
        self.setTitle("IDE Meta Compilador")
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setLayout(None)
        self.setLocationRelativeTo(None)
        self.setVisible(True)



    def Config(self):
        self.panel = JScrollPane()
        self.txtArea_Principal =JTextArea()
        self.jScrollPane1 =JScrollPane()
        self.txtTerminal =JTextArea()
        self.Menu =JMenuBar()
        self.menu_Archivo =JMenu()
        self.menu_Nuevo =JMenuItem()
        self.menuabrir =JMenuItem()
        self.menucerrar =JMenuItem()
        self.menuguardar =JMenuItem()
        self.menuguardarcomo =JMenuItem()
        self.menusalir =JMenuItem()
        self.menu_Edicion =JMenu()
        self.menu_cortar =JMenuItem()
        self.menu_copiar =JMenuItem()
        self.menu_pegar =JMenuItem()
        self.menu_Tablas =JMenu()
        self.menu_TablasEstaticas =JMenu()
        self.submenu_palabrasReservadas =JMenuItem()
        self.submenu_CaracteresEspeciales =JMenuItem()
        self.submenu_operadores =JMenu()
        self.ta_di_conu_enteros =JMenuItem()
        self.ta_di_conu_reales =JMenuItem()
        self.ta_di_conu_cientificos =JMenuItem()
        self.menu_TablaasDinamicas =JMenu()
        self.submenu_simbolos =JMenuItem()
        self.submenu_identificadores =JMenuItem()
        self.submenu_errores =JMenuItem()
        self.submenu_constantesNumericas =JMenu()
        self.ta_es_op_aritmeticos =JMenuItem()
        self.ta_es_op_relacionales =JMenuItem()
        self.ta_es_op_logicos =JMenuItem()
        self.submenu_Constantes_No_Numericas =JMenu()
        self.tab_caracteres =JMenuItem()
        self.tab_cadenas =JMenuItem()
        self.menu_Analisis =JMenu()
        self.ana_lexico =JMenuItem()
        self.ana_sintactico =JMenuItem()
        self.ana_semantico =JMenuItem()
        self.menu_Acerca_de =JMenu()
        self.btn_integrantes =JMenuItem()
        #########################
        self.jf = JFileChooser()

        #########################


        self.txtArea_Principal.setColumns(20)
        self.txtArea_Principal.setRows(5)
        self.txtArea_Principal.setAutoscrolls(False)
        self.txtArea_Principal.setEnabled(False)
        self.panel.setViewportView(self.txtArea_Principal)
        self.getContentPane().add(self.panel)
        self.panel.setBounds(0, 0, 1080, 450)


        self.txtTerminal.setColumns(20)
        self.txtTerminal.setRows(5)
        self.txtTerminal.setAutoscrolls(False)
        self.txtTerminal.setFocusable(False)
        self.jScrollPane1.setViewportView(self.txtTerminal)

        self.getContentPane().add(self.jScrollPane1)
        self.jScrollPane1.setBounds(0, 460, 1080, 150)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>MENU ARCHIVOS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.menu_Archivo.setText("Archivo")
        
        self.menu_Nuevo.addActionListener(lambda event : self.nuevo(event))
        self.menu_Nuevo.setText("Nuevo")
        self.menu_Archivo.add(self.menu_Nuevo)

        self.menuabrir.setText("Abrir")
        self.menuabrir.addActionListener(lambda event : self.abrir(event))
        self.menu_Archivo.add(self.menuabrir)

        self.menucerrar.setText("Cerrar")
        self.menucerrar.addActionListener(lambda event : self.cerrar(event))
        self.menu_Archivo.add(self.menucerrar)

        self.menuguardar.setText("Guardar")
        self.menuguardar.addActionListener(lambda event : self.guardar(event))
        self.menu_Archivo.add(self.menuguardar)
        
        self.menuguardarcomo.setText("Guardar como")
        self.menuguardarcomo.addActionListener(lambda event : self.guardarcomo(event))
        self.menu_Archivo.add(self.menuguardarcomo)

        self.menusalir.setText("Salir")
        self.menusalir.addActionListener(lambda event : self.salir(event))
        self.menu_Archivo.add(self.menusalir)
        
        
        self.Menu.add(self.menu_Archivo)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>MENU EDICION<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.menu_Edicion.setText("Edicion")

        self.menu_cortar.setText("Cortar")
        self.menu_cortar.addActionListener(lambda event : self.cortar(event))
        self.menu_Edicion.add(self.menu_cortar)

        self.menu_copiar.setText("Copiar")
        self.menu_copiar.addActionListener(lambda event : self.copiar(event))
        self.menu_Edicion.add(self.menu_copiar)

        self.menu_pegar.setText("Pegar")
        self.menu_pegar.addActionListener(lambda event : self.pegar(event))
        self.menu_Edicion.add(self.menu_pegar)

        self.Menu.add(self.menu_Edicion)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>MENU TABLAS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.menu_Tablas.setText("Tablas")

        self.menu_TablasEstaticas.setText("Tablas Estaticas")

        self.submenu_palabrasReservadas.setText("Tabla de palabras reservadas")
        self.menu_TablasEstaticas.add(self.submenu_palabrasReservadas)

        self.submenu_CaracteresEspeciales.setText("Tabla de caracteres especiales")
        self.menu_TablasEstaticas.add(self.submenu_CaracteresEspeciales)

        self.submenu_operadores.setText("Tabla de operadores")

        self.ta_es_op_aritmeticos.setText("Aritmeticos")
        self.submenu_operadores.add(self.ta_es_op_aritmeticos)

        self.ta_es_op_relacionales.setText("Relacionales")
        self.submenu_operadores.add(self.ta_es_op_relacionales)

        self.ta_es_op_logicos.setText("Logicos")
        self.submenu_operadores.add(self.ta_es_op_logicos)

        self.menu_TablasEstaticas.add(self.submenu_operadores)

        self.menu_Tablas.add(self.menu_TablasEstaticas)

        self.menu_TablaasDinamicas.setText("Tablas Dinamicas")

        self.submenu_simbolos.setText("Tabla de simbolos")
        self.menu_TablaasDinamicas.add(self.submenu_simbolos)

        self.submenu_identificadores.setText("Tabla de identificadores")
        self.menu_TablaasDinamicas.add(self.submenu_identificadores)

        self.submenu_errores.setText("Tabla de errores")
        self.menu_TablaasDinamicas.add(self.submenu_errores)

        self.submenu_constantesNumericas.setText("Tabla de constantes numericas")

        self.ta_di_conu_enteros.setText("Enteros")
        self.ta_di_conu_enteros.addActionListener(lambda event : self.numeroenteros(event))        
        self.submenu_constantesNumericas.add(self.ta_di_conu_enteros)

        self.ta_di_conu_reales.setText("Reales")
        self.ta_di_conu_reales.addActionListener(lambda event : self.numeroreales(event))
        self.submenu_constantesNumericas.add(self.ta_di_conu_reales)

        self.ta_di_conu_cientificos.setText("Cientificos")
        self.submenu_constantesNumericas.add(self.ta_di_conu_cientificos)

        self.menu_TablaasDinamicas.add(self.submenu_constantesNumericas)

        self.submenu_Constantes_No_Numericas.setText("Tabla de constantes no numericas")

        self.tab_caracteres.setText("Caracteres")
        self.submenu_Constantes_No_Numericas.add(self.tab_caracteres)

        self.tab_cadenas.setText("Cadenas")
        self.submenu_Constantes_No_Numericas.add(self.tab_cadenas)

        self.menu_TablaasDinamicas.add(self.submenu_Constantes_No_Numericas)

        self.menu_Tablas.add(self.menu_TablaasDinamicas)

        self.Menu.add(self.menu_Tablas)

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>MENU ANALISIS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        self.menu_Analisis.setText("Analisis")

        self.ana_lexico.setText("Lexico")
        self.ana_lexico.addActionListener(lambda event : self.lexico(event))
        self.menu_Analisis.add(self.ana_lexico)

        self.ana_sintactico.setText("Sintactico")
        self.ana_sintactico.addActionListener(lambda event : self.sintactico(event))        
        self.menu_Analisis.add(self.ana_sintactico)

        self.ana_semantico.setText("Semantico")
        self.menu_Analisis.add(self.ana_semantico)

        self.Menu.add(self.menu_Analisis)

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>MENU ACERCA DE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.menu_Acerca_de.setText("Acerca de")

        self.btn_integrantes.setText("Integrante del proyecto")
        self.btn_integrantes.addActionListener(lambda event : self.integrantes(event))
        self.menu_Acerca_de.add(self.btn_integrantes)

        self.Menu.add(self.menu_Acerca_de)

        





        self.setJMenuBar(self.Menu)
        self.setBounds(0, 0, 1095, 670)
        
######################################    
    def integrantes(self,event):
        informacion()
    def cortar(self,event): 
        self.txtArea_Principal.cut()    
    def copiar(self,event): 
        self.txtArea_Principal.copy()
    def pegar(self,event): 
        self.txtArea_Principal.paste()
    def salir(self,event): 
        self.dispose()
######################################    



    def guardarcomo(self,event): pass
    def guardar(self,event):
        if self.ruta == "":
            self.txtTerminal.setText("no hay un directorio abierto")
        else:
            agregar(self.ruta,str(self.txtArea_Principal.getText()))

    def cerrar(self,event): 
        self.txtArea_Principal.setText("")
        self.txtArea_Principal.setEnabled(False)
        
        self.ruta=""
        

    
    def abrir(self,event):   
        self.jf.showOpenDialog(self)
        self.ruta = self.jf.getSelectedFile()    
        self.txtArea_Principal.setEnabled(True)
        self.txtArea_Principal.setText(abrir(self.ruta)) 




    def nuevo(self,event):
        if self.ruta == "":
            print("no pasa nada")
        else:
            print("hay un archivo existente")
            self.ruta =""
            
        self.txtArea_Principal.setEnabled(True)
        self.txtArea_Principal.setText("")
######################################    
    def lexico(self,event):
        self.txtTerminal.setText("")
        archivo = open("{}".format(self.ruta),"r")
        texto = ""
        for a in prueba(self.txtArea_Principal.getText()):
            texto += a+"\n"
        
        self.txtTerminal.setText(texto)


    def sintactico(self,event):
        self.txtTerminal.setText("")
        texto=""
        for a in prueba_sintactica(self.txtArea_Principal.getText()):
            texto +=a+"\n"

        self.txtTerminal.setText(texto)
        



        
        
        
        
        
        
        
        
        
if __name__ == '__main__':      
    main()
    #TODO: Main     