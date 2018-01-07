# coding=utf-8
import maya.cmds as cmds

def init_uiSetup(inObjectName):
    if cmds.window(inObjectName, exists=True):
        cmds.deleteUI(inObjectName)