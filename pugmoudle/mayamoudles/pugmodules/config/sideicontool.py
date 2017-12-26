# coding=utf-8
# Author : yangjie
# data : 20170711

import maya.cmds as cmds


def side_icon_TOOL():
    par_form = cmds.iconTextButton('statusFieldButton', q=1, p=1)
    if cmds.iconTextCheckBox("toolManager", q=1, ex=1):
        cmds.deleteUI("toolManager")

    cmds.iconTextButton("toolManager", image1="mayaTool.png", p=par_form,
                        c='')


side_icon_TOOL()



