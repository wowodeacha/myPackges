# coding=utf-8
from Qt import QtCore, QtWidgets

import time


class Progress(QtWidgets.QDialog):
    def __init__(self, progressDic=None, parent=None):
        super(Progress, self).__init__(parent=None)
        if progressDic == None:
            return
        self.setWindowTitle(self.tr(progressDic["title"]))
        self.setObjectName(progressDic["objectName"])

        typeLabel = QtWidgets.QLabel(self.tr(progressDic["displayType"]))

        self.progressBar = QtWidgets.QProgressBar()

        GLayout = QtWidgets.QGridLayout()
        self._layout = GLayout
        GLayout.addWidget(typeLabel, 0, 0, 1, 1)

        GLayout.addWidget(self.progressBar, 1, 0, 1, 1)

        self.setLayout(GLayout)

        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(progressDic["num"])

# progress = Progress(progressDic={"title":"pro","displayType":"newprogress"})
# progress.show()
