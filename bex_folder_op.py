import bpy

from bpy.types import Operator

class BATEX_OT_OpenFolder(Operator):
  
  bl_idname = "object.bex_ot_openfolder"
  bl_label = "打开文件夹"
  bl_description = "打开导出目录" 
  bl_options = {'REGISTER'}

  def execute(self, context):
    bpy.ops.wm.path_open(filepath=context.scene.export_folder)
    return {'FINISHED'}
