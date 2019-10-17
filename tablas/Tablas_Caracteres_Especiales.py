from javax.swing import JFrame
from javax.swing import JTable
from javax.swing import JScrollPane
from java.awt import Font

class Tablas_Caracteres_Especiales(JFrame):
    def __init__(self):
        super (Tablas_Caracteres_Especiales,self).__init__()
        self.window()

    def window(self):
        self.setTitle("Tablas Caracteres")
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setLayout(None)
        self.setLocationRelativeTo(None)
        self.setVisible(True)

    def config():

        self.barra =JScrollPane();
        self.Tab_Caracteres_Especiales =JTable();
        nombre = ["nombre","apeM","apeP"]
        datos = ["victor","esau","cholo"]
        self.Tab_Caracteres_Especiales = JTable(datos,nombre);
        self.Tab_Caracteres_Especiales.addRow(datos);
      #  self.Tab_Caracteres_Especiales.setFont(Font("Tahoma", 0, 14)); # NOI18N
        self.barra.setViewportView(self.Tab_Caracteres_Especiales);
        #TODO: imcompleto se nesita una array y python maneja listas :(

        self.getContentPane().add(self.barra);
        self.barra.setBounds(0, 0, 929, 574);

        self.setBounds(0, 0, 939, 604);


if __name__ == '__main__':      
    Tablas_Caracteres_Especiales()


