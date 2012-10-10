# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'meaningArea.ui'
#
# Created: Wed Oct 10 15:50:01 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_meaningArea(object):
    def setupUi(self, control, meaningArea):
        meaningArea.setObjectName(_fromUtf8("meaningArea"))
        meaningArea.resize(400, 300)
        self.control = control
        self.verticalLayout = QtGui.QVBoxLayout(meaningArea)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.meaningEntry = QtGui.QWidget(meaningArea)
        self.meaningEntry.setObjectName(_fromUtf8("meaningEntry"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.meaningEntry)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.meaningButton = QtGui.QPushButton(self.meaningEntry)
        self.meaningButton.setObjectName(_fromUtf8("meaningButton"))
        self.horizontalLayout_2.addWidget(self.meaningButton)
        self.meaningLabel = QtGui.QLabel(self.meaningEntry)
        self.meaningLabel.setObjectName(_fromUtf8("meaningLabel"))
        self.horizontalLayout_2.addWidget(self.meaningLabel)
        self.verticalLayout.addWidget(self.meaningEntry)
        self.meaningEntry_2 = QtGui.QWidget(meaningArea)
        self.meaningEntry_2.setObjectName(_fromUtf8("meaningEntry_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.meaningEntry_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.meaningButton_2 = QtGui.QPushButton(self.meaningEntry_2)
        self.meaningButton_2.setObjectName(_fromUtf8("meaningButton_2"))
        self.horizontalLayout_3.addWidget(self.meaningButton_2)
        self.meaningLabel_2 = QtGui.QLabel(self.meaningEntry_2)
        self.meaningLabel_2.setObjectName(_fromUtf8("meaningLabel_2"))
        self.horizontalLayout_3.addWidget(self.meaningLabel_2)
        self.verticalLayout.addWidget(self.meaningEntry_2)

        self.retranslateUi(meaningArea)
        
        QtCore.QObject.connect(self.meaningButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.test("meaning button1"))
        QtCore.QObject.connect(self.meaningButton_2, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.test("meaning button2"))
        
        QtCore.QObject.connect(self.meaningButton, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.wordMeanings("word meaning id"))
        QtCore.QObject.connect(self.meaningButton_2, QtCore.SIGNAL(_fromUtf8("released()")), lambda: self.control.wordMeanings("word meaning id"))

        
        QtCore.QMetaObject.connectSlotsByName(meaningArea)

    def retranslateUi(self, meaningArea):
        meaningArea.setWindowTitle(QtGui.QApplication.translate("meaningArea", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.meaningButton.setText(QtGui.QApplication.translate("meaningArea", "先生", None, QtGui.QApplication.UnicodeUTF8))
        self.meaningLabel.setText(QtGui.QApplication.translate("meaningArea", "teacher; master; doctor;", None, QtGui.QApplication.UnicodeUTF8))
        self.meaningButton_2.setText(QtGui.QApplication.translate("meaningArea", "先生", None, QtGui.QApplication.UnicodeUTF8))
        self.meaningLabel_2.setText(QtGui.QApplication.translate("meaningArea", "teacher; master; doctor;", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    meaningArea = QtGui.QWidget()
    ui = Ui_meaningArea()
    ui.setupUi(meaningArea)
    meaningArea.show()
    sys.exit(app.exec_())

