# coding=utf-8

import maya.OpenMayaUI as apiUI
from Qt import QtWidgets

try:
    import shiboken
except:
    import shiboken2

def getMayaWindow(*args, **kw):
    ptr = apiUI.MQtUtil_mainWindow()
    if ptr is not None:
        try:
            return shiboken.wrapInstance(long(ptr), QtWidgets.QWidget)
        except:
            return shiboken2.wrapInstance(long(ptr), QtWidgets.QWidget)



