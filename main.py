import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication
from UI import Ui_Form
from random import randint


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonPressEvent)
        self.func = None
        self.do_paint = False
        self.setMouseTracking(True)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.paint_Circle(qp, randint(100, 600), randint(100, 600))
            self.do_paint = False
            qp.end()

    def buttonPressEvent(self):
        self.do_paint = True
        self.update()

    def paint_Circle(self, qp, x, y):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        Rad = randint(3, 100)
        qp.drawEllipse(x - Rad, y - Rad, 2 * Rad, 2 * Rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
