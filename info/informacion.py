from javax.swing import JFrame
from javax.swing import JLabel 

class informacion(JFrame):
    def __init__(self):
        self.windows()
        self.config()

    def windows(self):
        self.setTitle("Informacion")
        #self.setSize(100,100)
        self.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        self.setLayout(None)
        self.setLocationRelativeTo(None)
        self.setVisible(True)
    
    def config(self):
        self.integrantes = JLabel()
        self.victor = JLabel()
        self.osvaldo = JLabel()
        self.pedro = JLabel()
        self.python = JLabel()
        self.carita = JLabel()

        self.integrantes.setText("Integrantes")
        self.getContentPane().add(self.integrantes)
        self.integrantes.setBounds(76, 60, 100, 14)

        self.victor.setText("Victor Esau Jimenez Cholo")
        self.getContentPane().add(self.victor)
        self.victor.setBounds(38, 85, 180, 14)

        self.osvaldo.setText("Luis Osvaldo Perez Hernandez")
        self.getContentPane().add(self.osvaldo)
        self.osvaldo.setBounds(38, 105, 180, 14)

        self.pedro.setText("Pedro Guzman Primo")
        self.getContentPane().add(self.pedro)
        self.pedro.setBounds(38, 130, 150, 14)

        self.python.setText("HECHO CON  PYTHON ")
        self.getContentPane().add(self.python)
        self.python.setBounds(245, 85, 129, 14)

        self.carita.setText(":)")
        self.getContentPane().add(self.carita)
        self.carita.setBounds(288, 105, 8, 14)

        self.setBounds(0, 0, 416, 284)


if __name__ == '__main__':      
    informacion()  