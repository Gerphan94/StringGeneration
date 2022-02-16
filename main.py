from PyQt5 import QtCore, QtGui, QtWidgets
import random
import pyperclip
import string

class Ui_MainUI(object):
    def setupUi(self, MainUI):
        MainUI.setObjectName("MainUI")
        MainUI.setFixedSize(220, 520)
        self.CWidget = QtWidgets.QWidget(MainUI)
        self.CWidget.setObjectName("CWidget")
        self.lbTittle = QtWidgets.QLabel(self.CWidget)
        self.lbTittle.setGeometry(QtCore.QRect(20, 20, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbTittle.setFont(font)
        self.lbTittle.setObjectName("lbTittle")
        self.lbTittle.setText("R.a.n.d.o.M")
        self.lbTittle.setStyleSheet("color: Navy")
        self.GB1 = QtWidgets.QGroupBox(self.CWidget)
        self.GB1.setGeometry(QtCore.QRect(20, 60, 181, 101))
        self.GB1.setTitle("")
        self.GB1.setObjectName("GB1")
        self.cb1 = QtWidgets.QCheckBox(self.GB1)
        self.cb1.setGeometry(QtCore.QRect(10, 10, 150, 24))
        self.cb1.setObjectName("cb1")
        self.cb1.setText("Numberic digits (0-9)")
        self.cb1.setChecked(True)
        self.cb2 = QtWidgets.QCheckBox(self.GB1)
        self.cb2.setGeometry(QtCore.QRect(10, 30, 150, 24))
        self.cb2.setObjectName("cb2")
        self.cb2.setText("Uppercase letters (A-Z)")
        self.cb3 = QtWidgets.QCheckBox(self.GB1)
        self.cb3.setGeometry(QtCore.QRect(10, 50, 150, 24))
        self.cb3.setObjectName("cb3")
        self.cb3.setText("Lowercase letters (a-z)")
        self.cb4 = QtWidgets.QCheckBox(self.GB1)
        self.cb4.setGeometry(QtCore.QRect(10, 70, 150, 24))
        self.cb4.setObjectName("cb4")
        self.cb4.setText("Special character (!@#...)")
        self.GB2 = QtWidgets.QGroupBox(self.CWidget)
        self.GB2.setGeometry(QtCore.QRect(20, 170, 181, 80))
        self.GB2.setTitle("")
        self.GB2.setObjectName("GB2")
        self.lb1 = QtWidgets.QLabel(self.GB2)
        self.lb1.setGeometry(QtCore.QRect(10, 10, 100, 24))
        self.lb1.setObjectName("lb1")
        self.lb1.setText("String Length:")
        self.edt1 = QtWidgets.QLineEdit(self.GB2)
        self.edt1.setGeometry(QtCore.QRect(110, 10, 50, 24))
        self.edt1.setObjectName("edt1")
        self.edt1.setText("255")
        rx = QtCore.QRegExp("[1-9][0-9]{,4}")
        self.edt1.setValidator(QtGui.QRegExpValidator(rx))
        self.lb2 = QtWidgets.QLabel(self.GB2)
        self.lb2.setGeometry(QtCore.QRect(10, 40, 100, 24))
        self.lb2.setObjectName("lb12")
        self.lb2.setText("Paragraph Length:")
        self.spin = QtWidgets.QSpinBox(self.GB2)
        self.spin.setGeometry(QtCore.QRect(110, 40, 50, 24))
        self.spin.setRange(0,10)
        self.GB3 = QtWidgets.QGroupBox(self.CWidget)
        self.GB3.setGeometry(QtCore.QRect(20, 260, 181, 40))
        self.GB3.setTitle("")
        self.GB3.setObjectName("GB3")
        self.btnGet = QtWidgets.QPushButton(self.GB3)
        self.btnGet.setGeometry(QtCore.QRect(10, 10, 75, 24))
        self.btnGet.setObjectName("btnGet")
        self.btnGet.setText("Get string")
        self.btnGet.clicked.connect(self.getString)
        self.btnReset = QtWidgets.QPushButton(self.GB3)
        self.btnReset.setGeometry(QtCore.QRect(90, 10, 75, 24))
        self.btnReset.setObjectName("btnReset")
        self.btnReset.setText("Reset")
        self.btnReset.clicked.connect(self.reset)
        self.edtResult = QtWidgets.QTextEdit(self.CWidget)
        self.edtResult.setGeometry(QtCore.QRect(20, 310, 180, 130))
        self.edtResult.setObjectName("edtResult")
        self.edtResult.textChanged.connect(self.editingResult)
        self.GB4 = QtWidgets.QGroupBox(self.CWidget)
        self.GB4.setGeometry(QtCore.QRect(20, 450, 180, 35))
        self.GB4.setTitle("")
        self.GB4.setObjectName("GB4")
        self.btnCopy = QtWidgets.QPushButton(self.GB4)
        self.btnCopy.setGeometry(QtCore.QRect(40, 5, 100, 24))
        self.btnCopy.setObjectName("btnCopy")
        self.btnCopy.setText("Clipboard")
        self.btnCopy.clicked.connect(self.copyToClipboard)

        MainUI.setCentralWidget(self.CWidget)
        self.staB = QtWidgets.QStatusBar(MainUI)
        self.staB.setObjectName("staB")
        self.staB.showMessage("...")
        MainUI.setStatusBar(self.staB)
        QtCore.QMetaObject.connectSlotsByName(MainUI)

    def getString(self):
        
        stringResult = ""
        CB = []
        CB1 = CB2 = CB3 = CB4 = 0
        if (self.cb1.isChecked()):
            CB.append(1)
        if (self.cb2.isChecked()):
            CB.append(2)
        if (self.cb3.isChecked()):
            CB.append(3)
        if (self.cb4.isChecked()):
            CB.append(4)
        if (len(CB) == 0):
            self.staB.showMessage("No Option chosen")
            return
        p = int(self.spin.text())
        n = int(self.edt1.text())
        if (p == 0):
            for i in range(n):
                k = random.choice(CB)
                if (k ==1):
                    stringResult = stringResult + random.choice(string.digits)
                elif (k == 2):
                    stringResult = stringResult + random.choice(string.ascii_letters).upper()
                elif (k == 3):
                    stringResult = stringResult + random.choice(string.ascii_letters).lower()
                else:
                    stringResult = stringResult + random.choice(string.punctuation)
        else:
            iCount = 0
            while (iCount <= n):
                for i in range(p):
                    k = random.choice(CB)
                    if (iCount == n):
                        break
                    iCount = iCount + 1
                    if (k ==1):
                        stringResult = stringResult + random.choice(string.digits)
                    elif (k == 2):
                        stringResult = stringResult + random.choice(string.ascii_letters).upper()
                    elif (k == 3):
                        stringResult = stringResult + random.choice(string.ascii_letters).lower()
                    else:
                        stringResult = stringResult + random.choice(string.punctuation)
                if (iCount == n):
                    break
                stringResult = stringResult + " "
                iCount = iCount + 1
        self.edtResult.setText(stringResult)
        self.staB.showMessage("Susscess!")
        return

    def editingResult(self):
        self.edt1.setText(str(len(self.edtResult.toPlainText())))
        return

    def reset(self):
        self.edtResult.setText("")
        self.staB.showMessage("")
        return

    def copyToClipboard(self):
        tmpString = self.edtResult.toPlainText()
        if ( tmpString == ""):
            return
        pyperclip.copy(tmpString)
        self.staB.showMessage("Copied to clipboard")
        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainUI = QtWidgets.QMainWindow()
    MainUI.setWindowTitle("Random")
    ui = Ui_MainUI()
    ui.setupUi(MainUI)
    
    MainUI.show()
    sys.exit(app.exec_())
