import bpy

from bpy.types import Operator

from . bex_export import BatEx_Export
	
class BATEX_OT_Operator(Operator):
    bl_idname = "object.bex_ot_operator"
    bl_label = "批量导出"
    bl_description = "将选定对象导出为 FBX" 
    bl_options = {'REGISTER'}
    
    def execute(self, context):

        bat_export = BatEx_Export(context)
        bat_export.do_export()
        
        self.report({'INFO'}, "已导出到 " + context.scene.export_folder)
        return {'FINISHED'}


