# coding=utf-8
from Qt import QtWidgets, QtCore
import mayamainwinwrap
# import deletedubcatewidget



class ToolManageUI(QtWidgets.QMainWindow):
    def __init__(self,parent=mayamainwinwrap.getMayaWindow()):
        super(ToolManageUI, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        #
        menuBar = self.initMenuBar()

        #
        mainTabWidget = self.initTabWidget()

        #
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)
        #
        return
        #
    # main menubar
    def initMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("File")
        return menuBar
    # main tabWidget
    def initTabWidget(self):
        mainTabWidget = QtWidgets.QTabWidget(self)
        w1 = QtWidgets.QWidget()
        mainTabWidget.addTab(w1,"first")
        return mainTabWidget


if __name__ == "__main__":
    import sys

    # app = QtWidgets.QApplication(sys.argv)
    ui = ToolManageUI()
    ui.show()
    # app.exec_()
