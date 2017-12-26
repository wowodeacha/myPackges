# coding=utf-8
from Qt import QtCore, QtWidgets

import sys


class Progress(QtWidgets.QDialog):
    def __init__(self, progressDic=None,parent=None):
        super(Progress, self).__init__(parent=None)
        if progressDic==None:
            return
        self.setWindowTitle(self.tr(progressDic["title"]))

        typeLabel = QtWidgets.QLabel(self.tr(progressDic["displayType"]))

        self.progressBar = QtWidgets.QProgressBar()

        GLayout = QtWidgets.QGridLayout()
        GLayout.addWidget(typeLabel, 0, 0,1,1)

        GLayout.addWidget(self.progressBar, 1, 0, 1, 1)

        GLayout.setMargin(15)
        GLayout.setSpacing(10)

        self.setLayout(GLayout)



    def slotStart(self,num):

        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(num)

        # for i in range(num):
        #     self.progressBar.setValue(i)
        #     QtCore.QThread.msleep(100)




#
# progress = Progress(progressDic={"title":"pro","displayType":"newprogress"})
# progress.show()
