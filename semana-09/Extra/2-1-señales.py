from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal

class Persona:
    def __init__(self,nombre):
        self.nombre = nombre
    def gritar(self):
        print(self.nombre)
class MyWindow(QMainWindow):

    my_signal = pyqtSignal(str)
    my_other_signal = pyqtSignal(Persona)

    def __init__(self):
        super().__init__()
        # Conectamos la señal a la función my_function.
        self.my_signal.connect(self.my_function)
        self.my_other_signal.connect(self.my_other_function)

    def keyPressEvent(self, event):
        self.my_signal.emit(event.text())

    def mousePressEvent(self, event):
        print(event.x())
        print(event.y())
        self.my_other_signal.emit(Persona("Francisco"))

    def my_function(self, string):
        print("Me han llamado")
        print(string)
    def my_other_function(self,Persona):
        Persona.gritar()

if __name__ == '__main__':
    app = QApplication([])
    ex = MyWindow()
    ex.setGeometry(100,100,500,500)
    ex.show()
    app.exec_()
