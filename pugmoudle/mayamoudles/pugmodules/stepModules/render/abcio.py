# coding=utf-8
#

'''
PipeExportAbc(listType = "all",timeRange = None,Material = 1 ,type = "split")
'''
import pymel.core as pm
import json


# config



class ExportModelSgData():
    '''
    this class just export input meshes sg Data
    '''

    def __init__(self):

        self.flag = ['allList']

    # 1: get shape data list
    def getShapeDic(self, allList=None):
        shapeDataDic = {}
        if allList == None:
            allList = pm.ls(o=1, type='transform', ap=1)
            geoAllList = self.screenGeoList(allList)
            if not allList:
                return
        cleanList = list(set(geoAllList))
        for sh in cleanList:
            shapes = pm.listRelatives(sh, s=1, pa=1)
            shData = {}
            # shData["objectName"] = sh
            shData["name"] = sh.name()
            # shData["fullName"] = shapes[0]
            shData["shape"] = shapes[0].split('|')[-1]
            shData["polyCount"] = pm.polyEvaluate(shapes[0], f=1)
            shData["shaderSg"] = self.getShapeSg(shapes[0])
            if shData["shaderSg"]:
                shapeDataDic[shData["name"]] = (shData)

        # # ToDo : set the data path
        # with open("d:/oShapeData.json", "w") as f:
        #     f.write(json.dumps(shapeDataDic, sort_keys=True, indent=4))
        return shapeDataDic

    # 1.5 screen  list to geo list
    def screenGeoList(self, inputList):
        if not inputList:
            return
        outputList = []
        for i in inputList:
            iNode = pm.PyNode(i).getShape()
            # Check if given node is Mesh or NurbsSurface or ...
            if isinstance(iNode,
                          (pm.nodetypes.Mesh, pm.nodetypes.NurbsSurface)):
                outputList.append(i)
        return outputList

    # 2: get shape shader

    def getShapeSg(self, inShape):
        shaderSg = pm.listConnections(inShape, type='shadingEngine')
        sgCheckList = [x.name() for x in shaderSg if
                       x.name() not in ['initialParticleSE',
                                        'initialShadingGroup']]
        sgDic = {x: self.getSgSetList(x, inShapeName=inShape.name()) for x in
                 sgCheckList}
        return sgDic

    # 2.5: get sg set members
    def getSgSetList(self, inSg, inShapeName):
        setList = [i.name() for i in pm.ls(pm.sets(inSg, q=1), fl=1)]
        setListClean = self.cleanSetList(inSetList=setList,
                                         inShapeName=inShapeName)
        return setListClean

    # 2.5.F:
    def cleanSetList(self, inSetList, inShapeName):
        cleanList = []
        for i in inSetList:
            if "." in i:
                if i.split(".")[0] == inShapeName:
                    cleanList.append(i)
            else:
                if i == inShapeName:
                    cleanList.append(i)
        return cleanList

    # 3 export materials
    def sg_select_export(self, sgList, oPath):
        pm.select(cl=1)
        pm.select(sgList, noExpand=1)
        # ToDo : check this command
        pm.file(oPath, op='v=0', f=1, es=1, type="mayaBinary")

# export sg
'''
ExportSgNetwork(mode = "all")

'''
class ExportSgNetwork():
    # 0: sg out
    def exportSgNetwork(self,sgData,exportType,rootPath):
        if exportType == "all":
            sgList = [self.sgListReset(inSgData=sgData)]
        if exportType == "step":
            sgList = [[i] for i in sgData]
        for i in sgList:
            self.sgSelExport(sgList=i,oPath=oPath)





    # 1: sg list reset:
    def sgListReset(self,inSgData):
        inSgDataDic = inSgData
        modList = inSgDataDic.keys()
        outData = []
        print "export all sg list "
        outData = [inSgDataDic[x]["shaderSg"] for x in modList ]
        allList = []
        for i in outData:
            allList = allList + i
        outData = list(set(allList))
        return outData

    # 2.5: sg list export
    def sgSelExport(self,sgList,oPath):
        pm.select(cl=1)
        pm.select(sgList,noExpand=1)
        # ToDo : check this command
        pm.exportSelected(oPath,op="v=0",f=1,es=1,type="mayaBinary")

x





'''
# import maya.cmds as cmds
#
# class AssignShapeMtl():
#     def __init__(self):
#         self.all_shapes = []
#         self.shaded_shapes = []
#         self.default_shapes = []
#
#     def selectShapes(self, all_list):  # received allPaths
#         clean_list = list(set(all_list))
#         # print 'clean_list', clean_list
#         for sh in clean_list:
#             shapes = cmds.listRelatives(sh, s=1, pa=1)
#             sdata = shapeData()
#             sdata.full_name = sh
#             sdata.name = sh.split('|')[-1]
#             sdata.full_shape = shapes[0]
#             sdata.shape = shapes[0].split('|')[-1]
#
#             sdata.polyCount = cmds.polyEvaluate(shapes[0], f=1)
#             sha_list = self.getAllShader(shapes[0])
#
#             sdata.shader_list = sha_list
#             sdata.isDefualt = self.checkIsDefault(sha_list)
#
#             if sdata.isDefualt:
#                 self.default_shapes.append(sdata)
#             else:
#                 self.shaded_shapes.append(sdata)
#
#             self.all_shapes.append(sdata)
#
#     def getAllShader(self, sha):
#         shadingGrps = cmds.listConnections(sha, type='shadingEngine')
#         shaders = list(
#             set(cmds.ls(cmds.listConnections(shadingGrps), materials=1)))
#         clean_list = list(set(shaders))
#         return clean_list
#
#     def checkIsDefault(self, sha_list):
#         if not sha_list:
#             return True
#
#         sha_check_list = [x for x in sha_list if x not in ['lambert1']]
#         if len(sha_check_list):
#             return False
#         else:
#             return True
#
#     def getDefaultList(self):
#         return self.default_shapes
#
#     def getShadedList(self):
#         return self.shaded_shapes
#
#     def getShadedCount(self):
#         return len(self.shaded_shapes)
#
#     def findSameCountFaces(self, sdata):
#         rnt_list = [x for x in self.default_shapes if
#                     x.polyCount == sdata.polyCount]
#         return rnt_list
#
#     def assignShadeToDefault(self, shaded_, default_):
#         for sh in shaded_.shader_list:
#             cmds.hyperShade(o=sh)
#
#             sel_list = cmds.ls(sl=1, allPaths=1)
#             if not sel_list:
#                 return
#
#             clean_list = []
#
#             if [x for x in sel_list if '.f[' in x]:
#                 print 'f mode'
#                 clean_list = [x.replace(shaded_.full_name, default_.full_name)
#                               for x in sel_list if shaded_.name]
#             else:
#                 print 'g mode'
#                 clean_list = [x.replace(shaded_.full_shape,
# default_.full_shape)
#                               for x in sel_list if shaded_.shape in x]
#             # print 'clean', clean_list
#             cmds.select(clean_list)
#             cmds.hyperShade(assign=sh)
#
#     def checkNameInName(self, shade_shape, default_shade):
#         if ':' in shade_shape:
#             sh_name = shade_shape.split(':')[-1]
#             if sh_name in default_shade:
#                 return True
#         else:
#             if shade_shape in default_shade:
#                 return True
#
#         if ':' in default_shade:
#             de_name = default_shade.split(':')[-1]
#             if de_name in shade_shape:
#                 return True
#         else:
#             if default_shade in shade_shape:
#                 return True
#
#         return False
#
#
# class AssignMtlCtl(AssignShapeMtl):
#     def __init__(self):
#         AssignShapeMtl.__init__(self)
#
#     def selectAllCtl(self):
#         all_list = cmds.ls(sl=1, o=1, type='transform', ap=1)
#         if not all_list:
#             return
#
#         assign_list = []
#         self.selectShapes(all_list)
#
#         for sh in self.shaded_shapes:
#             f_sdata_list = self.findSameCountFaces(sh)
#             if f_sdata_list:
#                 if len(f_sdata_list) > 0:
#                     for sha in f_sdata_list:
#
#                         if self.checkNameInName(sh.name, sha.name):
#                             assign_list.append(sh.full_name)
#
#                             self.assignShadeToDefault(sh, sha)
#         cmds.select(assign_list, r=1)


'''





#         # 导出数据信息
#         dic_data = self.sceneModelSG_data()
#         if dic_data == {}:
#             return
#         # print dic_data,199
#         #
#         self.writeData(data_path, dic_data)
#
#         mesh_list = self.scenemodellist_get()
#         shape_list = mcmd.listRelatives(mesh_list, allDescendents=1, path=1,
#                                         type='mesh')
#         print shape_list, 225
#         # print shape_list
#         sg_list = list(
#             set(mcmd.listConnections(shape_list, type='shadingEngine')))
#         print sg_list, 225
#         self.abc_o(abc_path)
#         self.sg_select_export(sg_list, ex_path)
#
#         # TODO: 添加abc导出的命令
#
#     # 导出abc
#     def abc_o(self, path_in):
#         if self.ts_radioButton.checked():
#             f_star = self.starFrame_doubleSpinBox.value()
#             f_end = self.endFrame_doubleSpinBox.value()
#         else:
#             f_star = mcmd.currentTime(query=True)
#             f_end = mcmd.currentTime(query=True)
#
#         list_sel = mcmd.ls(sl=1, l=1)
#         sel_str = ''
#         path_str = path_in
#
#         for i in list_sel:
#             sel_str = sel_str + " -root " + i
#
#         pm.AbcExport(
#             j="-frameRange %d %d -uvWrite -attr UUIDCreate -writeVisibility "
#               "-dataFormat hdf %s -file %s" % (
#                   f_star, f_end, sel_str, path_str))
#
#     # 材质文件导出
#     def sg_select_export(self, sg_list, ex_path):
#         mcmd.select(cl=1)
#         mcmd.select(sg_list, noExpand=1)
#
#         # _exportFile = self._inPath + '/' + self._FileExportName + '/' +
#         # matName
#         mcmd.file(ex_path, op='v=0', f=1, es=1, type="mayaBinary")
#
#     def sceneModelSG_data(self):
#         model_list = self.scenemodellist_get()
#         fin_dic = {}
#         for i in model_list:
#             cur_sgList = self.modelsg_get(i)
#             cur_dir = self.singlemodelsgdir_get(i, cur_sgList)
#             fin_dic = dict(fin_dic.items() + cur_dir.items())
#         return fin_dic
#
#     # 场景模型的筛选
#     def scenemodellist_get(self):
#         shape_list = mcmd.ls(g=1, ap=1)
#         geo_list = []
#         for i in shape_list:
#             geo = mcmd.listRelatives(i, p=1, f=1)[0]
#             geo_list.append(geo)
#         outgeo_list = list(set(geo_list))
#         return outgeo_list
#
#     # 获取单个模型的SG列表
#     def modelsg_get(self, in_model):
#         shapeList = mcmd.listRelatives(in_model, s=1, pa=1)
#         if shapeList == None:
#             print in_model, "do not have shape!!!!!"
#             return
#
#         for i in shapeList:
#             iIntermediateObject = i + '.intermediateObject'
#             iIntermediateObjectAttr = mcmd.getAttr(iIntermediateObject)
#             if not iIntermediateObjectAttr:
#                 shape = i
#             else:
#                 pass
#         ConnectedNodeList = mcmd.listConnections(shape, t="shadingEngine")
#         if ConnectedNodeList == None:
#             return None
#         else:
#             ConnectedNodeList = list(set(ConnectedNodeList))
#             return ConnectedNodeList
#
#     # 获取单个模型SG字典
#     def singlemodelsgdir_get(self, in_model, in_sgList):
#         uuid = self.model_UUID_add(in_model)
#         sg_dic = {}
#         model_dir = {uuid: sg_dic}
#         for i in in_sgList:
#             list_detial = mcmd.sets(i, q=True)
#             list_detial = mcmd.ls(list_detial, fl=1)
#             # print uuid,in_model
#             model_list_detial = self.list_screen(in_model, list_detial)
#             sg_dic[i] = model_list_detial
#         return model_dir
#
#     # 筛选包含指定模型的列表
#     def list_screen(self, in_model, in_list):
#         in_model = mcmd.ls(in_model, sn=1)[0]
#         out_list = []
#         for i in in_list:
#             if in_model in i:
#                 out_list = out_list + [i]
#             else:
#                 pass
#         return out_list
#
#     # 添加uuid属性到对像
#     def model_UUID_add(self, model_in):
#         if not mcmd.objExists(model_in + '.UUIDCreate'):
#             mcmd.addAttr(model_in, ln='UUIDCreate', dt='string')
#             UUID = "uuid_" + mcmd.ls(model_in, ap=1)[0]
#             mcmd.setAttr(model_in + '.UUIDCreate', UUID, type='string')
#
#         else:
#             UUID = mcmd.getAttr(model_in + '.UUIDCreate')
#
#         return UUID
#
#     # 数据写入
#     def writeData(self, data_path, data_in):
#         json.dump(data_in, open(data_path, 'w'))
#
#     # combox 设置
#     def combox_item_add(self, dir_type, type_in, combox_in):
#         if dir_type == 0:
#             dir_path = self.importDir_lineEdit.text()
#         if dir_type == 1:
#             dir_path = QtWidgets.QFileDialog.getExistingDirectory(parent=self,
#
# caption="Chose_File",
#
# directory=QtCore.QDir.currentPath())
#         file_list = self.getTarTypeFileFromDir(dir_path, type_in)
#         # print file_list
#         if file_list == None:
#             return
#         combox_in.clear()
#         for i in file_list:
#             combox_in.addItem(i)
#
#     # 获取目录某一类型文件、
#     def getTarTypeFileFromDir(self, dir_path, type_in):
#         dir_list = os.listdir(dir_path)
#         if len(dir_list) == 0:
#             return None
#         # print dir_list
#         tarFileList = []
#         for i in dir_list:
#             file_path = dir_path + "/" + i
#             # print file_path, 347
#             if os.path.isfile(file_path):
#                 print file_path, "is 349"
#                 file_path = str(file_path)
#                 try:
#                     extrName = os.path.splitext(file_path)[-1]
#                     # print extrName
#                     if extrName == type_in:
#                         tarFileList.append(i)
#                 except:
#                     pass
#             if os.path.isdir(file_path):
#                 pass
#             else:
#                 pass
#         return tarFileList
#
#     # 导入材质 并 连接材质
#     def abc_import(self):
#
#         pre = "shader_in"
#         root_path = str(self.importDir_lineEdit.text())
#         shader_path = root_path + "/" + str(
#             self.shaderName_comboBox.currentText())
#         json_path = root_path + "/" + str(
# self.jsonName_comboBox.currentText())
#         abc_path = root_path + "/" + str(self.abcName_comboBox.currentText())
#
#         pm.AbcImport(abc_path, mode="import")
#
#         dic = json.load(open(json_path, 'r'))
#         model_list = self.scenemodellist_get()
#         self.shader_import(pre, shader_path)
#
#         for i in model_list:
#             self.editSets(i, pre, dic)
#             self.feedBack_listWidget.addItem(i)
#
#     # 材质导入
#     def shader_import(self, pre, shader_path):
#         mcmd.file(shader_path, i=1, options="v=0;", mergeNamespacesOnClash=0,
#                   ns=pre)
#         return
#
#     # 单个模型材质连接
#     def editSets(self, model_in, pre, dic):
#         model_uuid_attr = model_in + ".UUIDCreate"
#         if not mcmd.objExists(model_uuid_attr):
#             return
#         key_uuid = mcmd.getAttr(model_uuid_attr)
#         shader_dic = dic[key_uuid]
#         shader_list = shader_dic.keys()
#
#         for i in shader_list:
#             if len(shader_dic[i]) >= 1:
#                 shader_chrd = shader_dic[i]
#                 exit_i = pre + ":" + i
#                 if mcmd.objExists(exit_i):
#                     mcmd.sets(shader_chrd, e=1, forceElement=exit_i)
#                 else:
#                     pass
#             else:
#                 pass
#         return
