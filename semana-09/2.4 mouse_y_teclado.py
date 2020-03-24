import sys
import time
from PyQt5.QtCore import (QObject, pyqtSignal)
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel)

class MiSignal(QObject):
    """
    Esta clase contiene las señales que permiten la comunicación entre
    elementos de la GUI.
    """
    escribe_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.text = ''



class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializa_GUI()

    def inicializa_GUI(self):
        self.s = MiSignal()
        self.s.escribe_signal.connect(self.escribe_etiqueta)
        self.s.printea_signal.connect(self.printea_letra)


        self.etiqueta1 = QLabel('Etiqueta', self)
        self.etiqueta1.move(20, 10)
        self.resize(self.etiqueta1.sizeHint())

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        """
        Este evento maneja cuando se presiona alguno de los botones del mouse.
        """
        self.s.escribe_signal.emit()


    def keyPressEvent(self, event):
        """
        Este método maneja el evento que se produce al presionar las teclas.
        """
        self.s.printea_signal.emit()


    def escribe_etiqueta (self):
        self.etiqueta1.setText('Presionaron el mouse')
        self.etiqueta1.resize(self.etiqueta1.sizeHint())

    def printea_letra (self):
        print(self.sender())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiVentana()
    sys.exit(app.exec_())
