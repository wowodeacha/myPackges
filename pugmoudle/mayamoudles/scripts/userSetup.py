# coding=utf-8
#
# Author : jaime yong
#


import maya.utils
import os
import json
import inspect
import sys


class MayaUserSetUp():
    def __init__(self):
        # rootPath = os.path.dirname(os.path.dirname(
        #     os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

        filename = inspect.getframeinfo(inspect.currentframe()).filename
        # path = os.path.dirname(os.path.abspath(filename))


        self.rootPath = os.path.abspath(filename).rsplit('\\', 4)[0]
        configPath = os.path.join(self.rootPath,
                                  "pugmoudle/mayamoudles/scripts/pathConfig.json")
        with open(configPath,"r") as f:
            self.pathDic = json.load(f)

        self.add_sysPath()

        # initial tool icon
        maya.utils.executeDeferred('import sideicontool')



        # # maya.utils.executeDeferred("sys.path.append(
        # # 'S:\\kaka\\worldScript\\maya_plugins');import demiiris")
        # # self.scr_init()
        # self.add_sysPath()
        # # self.init_modSet()
        # # maya.utils.executeDeferred('self.tool_setUp()')
        # # 延迟运行命令  载入工具窗口 并且导入添加模块
        # maya.utils.executeDeferred(
        #     'import KAKAToll.KAKA_Tool as KAKA_Tool;KAKA_Tool.KAKA_Tool('
        #     ');import MODULE_TOOL')
        # maya.utils.executeDeferred('import side_icon_TOOL')

    def add_sysPath(self):
        pythonPathList = self.pathDic["pythonPath"]
        for i in pythonPathList:
            sys.path.append(i.format(rootPath=self.rootPath))
            print i.format(rootPath=self.rootPath)

        globalModulePathList = self.pathDic["globalModulePath"]
        for i in globalModulePathList:
            sys.path.append(i.format(rootPath=self.rootPath))
            print i.format(rootPath=self.rootPath)



        # sys.path.append('S:\\kaka\\worldScript\\scripts')
        # sys.path.append('S:\\kaka\\worldScript\\scripts\\python')
        # sys.path.append('S:\\kaka\\worldScript\\maya\\pug_modules\\CUSMODULE')

    # def scr_init(self):
    #     mm.eval(r'source "NPautoSave.mel;')
    #
    #     return

    # def akita_loadDeadLine(self):
    #     try:
    #         mm.eval(r'source "DeadlineMayaClient.mel";')
    #     except:
    #         sys.stderr.write("failed load deadline")
    #     return

    def tool_setUp(self):
        print "set new "


MayaUserSetUp()