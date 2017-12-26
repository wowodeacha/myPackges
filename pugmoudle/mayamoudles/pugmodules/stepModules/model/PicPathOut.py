# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PicPathOut.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCore, QtGui, QtWidgets


class Ui_sec_Follice_Form(object):
    def setupUi(self, textureOutForm):
        textureOutForm.setObjectName("textureOutForm")
        textureOutForm.resize(200, 300)
        textureOutForm.setStyleSheet(
            "QWidget{color: rgb(255, 255, "
            "255);background-color:#757575;font:bold 11pt \"Lucida "
            "Calligraphy\" ;}\n"
            "\n"
            "QListWidget{background-color:#D7CCC8}\n"
            "\n"
            "QPushButton{font-weight: lighter;color: "
            "#263238;background-color:#B0BEC5  /* Light blue */;border-style: "
            "solid ;border-width:2px;border-color:#76FF03;border-radius:10px"
            ";}\n"
            "QPushButton:hover{border:5px solid  "
            "transparent;background-color:#00E676;}\n"
            "QPushButton:pressed{font:bold italic ;border:2px solid  "
            "#18FFFF;background-color:#C5CAE9;}\n"
            "\n"
            "\n"
            "")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(sec_Follice_Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.List_frame = QtWidgets.QFrame(sec_Follice_Form)
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
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.loadPC_pushButton = QtWidgets.QPushButton(self.List_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.loadPC_pushButton.sizePolicy().hasHeightForWidth())
        self.loadPC_pushButton.setSizePolicy(sizePolicy)
        self.loadPC_pushButton.setObjectName("loadPC_pushButton")
        self.verticalLayout_2.addWidget(self.loadPC_pushButton)
        self.MergePC_pushButton = QtWidgets.QPushButton(self.List_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.MergePC_pushButton.sizePolicy().hasHeightForWidth())
        self.MergePC_pushButton.setSizePolicy(sizePolicy)
        self.MergePC_pushButton.setObjectName("MergePC_pushButton")
        self.verticalLayout_2.addWidget(self.MergePC_pushButton)
        self.exportPC_pushButton = QtWidgets.QPushButton(self.List_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.exportPC_pushButton.sizePolicy().hasHeightForWidth())
        self.exportPC_pushButton.setSizePolicy(sizePolicy)
        self.exportPC_pushButton.setObjectName("exportPC_pushButton")
        self.verticalLayout_2.addWidget(self.exportPC_pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addWidget(self.List_frame)

        self.retranslateUi(sec_Follice_Form)
        QtCore.QMetaObject.connectSlotsByName(sec_Follice_Form)

    def retranslateUi(self, sec_Follice_Form):
        _translate = QtCore.QCoreApplication.translate
        sec_Follice_Form.setWindowTitle(
            _translate("sec_Follice_Form", "secCtrl_follice_win"))
        self.loadPC_pushButton.setText(_translate("sec_Follice_Form", "LOAD"))
        self.MergePC_pushButton.setText(
            _translate("sec_Follice_Form", "MERAGE"))
        self.exportPC_pushButton.setText(
            _translate("sec_Follice_Form", "EXPORT"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    sec_Follice_Form = QtWidgets.QWidget()
    ui = Ui_sec_Follice_Form()
    ui.setupUi(sec_Follice_Form)
    sec_Follice_Form.show()
    sys.exit(app.exec_())
