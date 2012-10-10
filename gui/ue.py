# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ue.ui'
#
# Created: Wed Oct 10 17:53:49 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_UEarea(object):
    def setupUi(self, UEarea):
        UEarea.setObjectName(_fromUtf8("UEarea"))
        UEarea.resize(609, 531)
        self.verticalLayout_7 = QtGui.QVBoxLayout(UEarea)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.scrollAreaUE = QtGui.QScrollArea(UEarea)
        self.scrollAreaUE.setWidgetResizable(True)
        self.scrollAreaUE.setObjectName(_fromUtf8("scrollAreaUE"))
        self.scrollAreaUEWidgetContents = QtGui.QWidget()
        self.scrollAreaUEWidgetContents.setGeometry(QtCore.QRect(0, 0, 589, 511))
        self.scrollAreaUEWidgetContents.setObjectName(_fromUtf8("scrollAreaUEWidgetContents"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaUEWidgetContents)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.usageExample = QtGui.QWidget(self.scrollAreaUEWidgetContents)
        self.usageExample.setObjectName(_fromUtf8("usageExample"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.usageExample)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.uepart1 = QtGui.QLabel(self.usageExample)
        self.uepart1.setObjectName(_fromUtf8("uepart1"))
        self.horizontalLayout_8.addWidget(self.uepart1)
        self.uepart2 = QtGui.QLabel(self.usageExample)
        self.uepart2.setObjectName(_fromUtf8("uepart2"))
        self.horizontalLayout_8.addWidget(self.uepart2)
        self.uepart3 = QtGui.QLabel(self.usageExample)
        self.uepart3.setObjectName(_fromUtf8("uepart3"))
        self.horizontalLayout_8.addWidget(self.uepart3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout_4.addWidget(self.usageExample)
        self.usageExample_line = QtGui.QFrame(self.scrollAreaUEWidgetContents)
        self.usageExample_line.setFrameShape(QtGui.QFrame.HLine)
        self.usageExample_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.usageExample_line.setObjectName(_fromUtf8("usageExample_line"))
        self.verticalLayout_4.addWidget(self.usageExample_line)
        self.usageExample_2 = QtGui.QWidget(self.scrollAreaUEWidgetContents)
        self.usageExample_2.setObjectName(_fromUtf8("usageExample_2"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.usageExample_2)
        self.horizontalLayout_10.setMargin(0)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.uepart1_2 = QtGui.QLabel(self.usageExample_2)
        self.uepart1_2.setObjectName(_fromUtf8("uepart1_2"))
        self.horizontalLayout_10.addWidget(self.uepart1_2)
        self.uepart2_2 = QtGui.QLabel(self.usageExample_2)
        self.uepart2_2.setObjectName(_fromUtf8("uepart2_2"))
        self.horizontalLayout_10.addWidget(self.uepart2_2)
        self.uepart3_2 = QtGui.QLabel(self.usageExample_2)
        self.uepart3_2.setObjectName(_fromUtf8("uepart3_2"))
        self.horizontalLayout_10.addWidget(self.uepart3_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.usageExample_2)
        self.usageExample_line_2 = QtGui.QFrame(self.scrollAreaUEWidgetContents)
        self.usageExample_line_2.setFrameShape(QtGui.QFrame.HLine)
        self.usageExample_line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.usageExample_line_2.setObjectName(_fromUtf8("usageExample_line_2"))
        self.verticalLayout_4.addWidget(self.usageExample_line_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.scrollAreaUE.setWidget(self.scrollAreaUEWidgetContents)
        self.verticalLayout_7.addWidget(self.scrollAreaUE)

        self.retranslateUi(UEarea)
        QtCore.QMetaObject.connectSlotsByName(UEarea)

    def retranslateUi(self, UEarea):
        UEarea.setWindowTitle(QtGui.QApplication.translate("UEarea", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.uepart1.setText(QtGui.QApplication.translate("UEarea", "part1", None, QtGui.QApplication.UnicodeUTF8))
        self.uepart2.setText(QtGui.QApplication.translate("UEarea", "part2", None, QtGui.QApplication.UnicodeUTF8))
        self.uepart3.setText(QtGui.QApplication.translate("UEarea", "part3", None, QtGui.QApplication.UnicodeUTF8))
        self.uepart1_2.setText(QtGui.QApplication.translate("UEarea", "part1", None, QtGui.QApplication.UnicodeUTF8))
        self.uepart2_2.setText(QtGui.QApplication.translate("UEarea", "part2", None, QtGui.QApplication.UnicodeUTF8))
        self.uepart3_2.setText(QtGui.QApplication.translate("UEarea", "part3", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    UEarea = QtGui.QWidget()
    ui = Ui_UEarea()
    ui.setupUi(UEarea)
    UEarea.show()
    sys.exit(app.exec_())

