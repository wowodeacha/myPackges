# coding=utf-8
# Author : yangjie
# data: 20170706
# version: 0.001


import pymel.core as pm
from pymel import versions
import maya.OpenMayaUI as apiUI
from Qt import QtWidgets, QtCore
import shutil
import sys
import os

import PicPathOut

reload(PicPathOut)

version = str(versions.current())
iv = int(version[0:4])

if iv < 2017:
    import shiboken
else:
    import shiboken2


def getMayaWindow():
    ptr = apiUI.MQtUtil_mainWindow()
    if ptr is not None:
        if iv < 2017:
            return shiboken.wrapInstance(long(ptr), QtWidgets.QWidget)
        else:
            return shiboken2.wrapInstance(long(ptr), QtWidgets.QWidget)


class PicPathOutSet(QtWidgets.QDialog, PicPathOut.Ui_sec_Follice_Form):
    def __init__(self, parent=getMayaWindow()):
        super(PicPathOutSet, self).__init__(parent)
        self.close_duplicateWindow(parent)

        self.setupUi(self)

        self.languageSet()
        self.signal_init()
        self.resize(self.sizeHint())

    # close double window 关闭重复窗口
    def close_duplicateWindow(self, parent):
        for widget in parent.findChildren(QtWidgets.QDialog):
            if widget is not self:
                if widget.objectName() == self.objectName():
                    widget.close()

    # button text set 按键文字设置
    def languageSet(self):
        self.loadPC_pushButton.setText(u"导入")
        self.MergePC_pushButton.setText(u"合并")
        self.MergePC_pushButton.hide()
        self.exportPC_pushButton.setText(u"导出")

    # signal init 信号初始化
    def signal_init(self):
        self.loadPC_pushButton.clicked.connect(lambda: self.texFile_loadList())
        self.exportPC_pushButton.clicked.connect(lambda: self.exportFile_loadList())

    # load shaderNode to ui导入场景的材质节点
    def texFile_loadList(self):
        listWidget = self.pic_listWidget
        listWidget.clear()
        # 获取场景中的file节点列表
        fileNodeList = pm.ls(et="file")
        psdFileNodeList = pm.ls(et="psdFileTex")
        all_list = fileNodeList + psdFileNodeList

        for i in all_list:
            qtItem = QtWidgets.QListWidgetItem(listWidget)
            qtItem.setText(str(i))

        return fileNodeList, psdFileNodeList

        # 合并场景中重复的材质节点

    # 导出场景中材质节点
    def exportFile_loadList(self):
        file_path_dig = QtWidgets.QFileDialog.getExistingDirectory(parent=self, caption="Chose_Path")
        listWidget = self.pic_listWidget
        items = []
        # print listWidget.count()
        for index in xrange(listWidget.count()):
            curItem = str(listWidget.item(index).text())
            itemPN = pm.PyNode(curItem)
            AttrName = itemPN.fileTextureName
            AttrGet = AttrName.get()
            file_name = os.path.split(AttrGet)[-1]
            curPath = file_path_dig + "\\" + file_name
            if os.path.exists(AttrGet) and os.path.abspath(AttrGet) != os.path.abspath(curPath):
                print "why you copy here"
                shutil.copy(AttrGet, file_path_dig)

                AttrSet = AttrName.set(curPath)
                print curPath, "copyed"
                items.append(listWidget.item(index).text())
            else:
                if os.path.abspath(AttrGet) == os.path.abspath(curPath):
                    print "same file do not copy"
                pass
                # print items
