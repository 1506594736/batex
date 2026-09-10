bl_info = {
    "name" : "Batex",
    "author" : "1506594736",
    "description" : "批量导出选定对象为 FBX",
    "version" : (1, 1, 0, 0),
    "blender" : (2, 80, 0),
    "location" : "3D 视图侧边栏 (N 键) - Batex",
    "warning" : "",
    "doc_url" : "https://github.com/1506594736/batex",
    "tracker_url" : "https://github.com/1506594736/batex/issues",
    "category" : "Import-Export"
}

import bpy
from bpy.props import *

from . bex_prefs import BATEX_AddonPreferences
from . bex_panel import *
from . bex_op import *
from . bex_folder_op import *

bpy.types.Scene.export_folder = StringProperty(name="导出文件夹", 
               subtype="DIR_PATH", 
               description="导出 FBX 文件的目标目录")

bpy.types.Scene.center_transform = BoolProperty(name="居中变换",
                default=True,
                description="导出前把物体轴心移动到世界原点")

bpy.types.Scene.apply_transform = BoolProperty(name="应用变换",
                default=True,
                description="应用缩放与变换（实验性）")

bpy.types.Scene.export_smoothing = EnumProperty(
    name="平滑方式",
    description="导出时写入的平滑信息",
    items=(
        ('EDGE', '边', '写入边平滑',0),
        ('FACE', '面', '写入面平滑',1),
        ('OFF', '仅法向', '仅写入法向',2)
        ),
    default='OFF'
    )

bpy.types.Scene.export_animations = BoolProperty(name="导出骨骼与动画",
                default=False,
                description="同时导出骨骼与动画")

bpy.types.Scene.one_material_ID = BoolProperty(name="单一材质 ID",
                default=True,
                description="每个物体只导出一个材质")

classes = ( BATEX_AddonPreferences, BATEX_PT_Panel, BATEX_OT_Operator, BATEX_OT_OpenFolder )

register, unregister = bpy.utils.register_classes_factory(classes)
    
if __name__ == "__main__":
    register()
