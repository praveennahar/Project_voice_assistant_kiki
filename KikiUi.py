
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KikiUi(object):
    def setupUi(self, KikiUi):
        KikiUi.setObjectName("KikiUi")
        KikiUi.resize(1263, 714)
        self.centralwidget = QtWidgets.QWidget(KikiUi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 1281, 721))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Black_Template.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-140, -100, 881, 651))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("__1.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(660, 10, 601, 411))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Iron_Template_1.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(700, 400, 551, 301))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("B.G_Template_1.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 620, 201, 71))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 87 26pt \"Arial Black\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 620, 201, 71))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 87 26pt \"Arial Black\";")
        self.pushButton_2.setObjectName("pushButton_2")
        KikiUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(KikiUi)
        QtCore.QMetaObject.connectSlotsByName(KikiUi)

    def retranslateUi(self, KikiUi):
        _translate = QtCore.QCoreApplication.translate
        KikiUi.setWindowTitle(_translate("KikiUi", "MainWindow"))
        self.pushButton.setText(_translate("KikiUi", "START"))
        self.pushButton_2.setText(_translate("KikiUi", "STOP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KikiUi = QtWidgets.QMainWindow()
    ui = Ui_KikiUi()
    ui.setupUi(KikiUi)
    KikiUi.show()
    sys.exit(app.exec_())
