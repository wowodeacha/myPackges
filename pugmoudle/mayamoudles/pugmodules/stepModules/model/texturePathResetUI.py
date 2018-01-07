# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'texturePathResetUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCore, QtGui, QtWidgets

class Ui_texturePathReset(object):
    def setupUi(self, texturePathReset):
        texturePathReset.setObjectName("texturePathReset")
        texturePathReset.resize(300, 205)
        texturePathReset.setStyleSheet("QWidget{color: rgb(255, 255, 255);background-color:#424242;font:bold 11pt \"Lucida Calligraphy\" ;}\n"
"\n"
"QListWidget{background-color:#9E9E9E}\n"
"\n"
"QPushButton{font-weight: lighter;color: #263238;background-color:#B0BEC5  /* Light blue */;border-style: solid ;border-width:2px;border-color:#ecf0f1;border-radius:10px;}\n"
"QPushButton:hover{border:5px solid  transparent;background-color:#FAFAFA;}\n"
"QPushButton:pressed{font:bold italic ;border:2px solid  #18FFFF;background-color:#C5CAE9;}\n"
"\n"
"\n"
"")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(texturePathReset)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.List_frame = QtWidgets.QFrame(texturePathReset)
        self.List_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.List_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.List_frame.setObjectName("List_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.List_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pic_listWidget = QtWidgets.QListWidget(self.List_frame)
        self.pic_listWidget.setObjectName("pic_listWidget")
        self.horizontalLayout_6.addWidget(self.pic_listWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.loadPC_pushButton = QtWidgets.QPushButton(self.List_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadPC_pushButton.sizePolicy().hasHeightForWidth())
        self.loadPC_pushButton.setSizePolicy(sizePolicy)
        self.loadPC_pushButton.setObjectName("loadPC_pushButton")
        self.verticalLayout_2.addWidget(self.loadPC_pushButton)
        self.exportPC_pushButton = QtWidgets.QPushButton(self.List_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportPC_pushButton.sizePolicy().hasHeightForWidth())
        self.exportPC_pushButton.setSizePolicy(sizePolicy)
        self.exportPC_pushButton.setObjectName("exportPC_pushButton")
        self.verticalLayout_2.addWidget(self.exportPC_pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addWidget(self.List_frame)

        self.retranslateUi(texturePathReset)
        QtCore.QMetaObject.connectSlotsByName(texturePathReset)

    def retranslateUi(self, texturePathReset):
        _translate = QtCore.QCoreApplication.translate
        texturePathReset.setWindowTitle(_translate("texturePathReset", "texture path reset"))
        self.loadPC_pushButton.setText(_translate("texturePathReset", "LOAD"))
        self.exportPC_pushButton.setText(_translate("texturePathReset", "EXPORT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    texturePathReset = QtWidgets.QWidget()
    ui = Ui_texturePathReset()
    ui.setupUi(texturePathReset)
    texturePathReset.show()
    sys.exit(app.exec_())

