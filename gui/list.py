# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list.ui'
#
# Created: Mon Oct  8 17:54:58 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_List(object):
    def setupUi(self, List):
        self.text = ""
        List.setObjectName(_fromUtf8("List"))
        List.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(List)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ListNameEdit = QtGui.QLineEdit(List)
        self.ListNameEdit.setObjectName(_fromUtf8("ListNameEdit"))
        self.verticalLayout.addWidget(self.ListNameEdit)
        self.Listendview = QtGui.QWidget(List)
        self.Listendview.setObjectName(_fromUtf8("Listendview"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.Listendview)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.line_2 = QtGui.QFrame(self.Listendview)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        self.line = QtGui.QFrame(self.Listendview)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.label = QtGui.QLabel(self.Listendview)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.Listendview)
        
        self.retranslateUi(List)
        self.namechange()
        QtCore.QObject.connect(self.ListNameEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), lambda: self.displaytext())
        QtCore.QMetaObject.connectSlotsByName(List)

    def retranslateUi(self, List):
        List.setWindowTitle(QtGui.QApplication.translate("List", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("List", self.text, None, QtGui.QApplication.UnicodeUTF8))


    def namechange(self):
        self.Listendview.hide()
        self.ListNameEdit.show()
    
    def displaytext(self):
        self.ListNameEdit.hide()
        self.Listendview.show()
        self.text = self.ListNameEdit.text()
        self.label.setText(QtGui.QApplication.translate("List", self.text, None, QtGui.QApplication.UnicodeUTF8))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    List = QtGui.QWidget()
    ui = Ui_List()
    ui.setupUi(List)
    List.show()
    sys.exit(app.exec_())

