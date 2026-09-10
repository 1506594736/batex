import bpy

from bpy.props import EnumProperty
from bpy.types import AddonPreferences

# Both enums list the same six axes: the FBX exporter needs one axis for
# "forward" and a different one for "up", so the update callbacks below keep
# the two selections on different axes instead of limiting the item lists.
FORWARD_ITEMS = (
    ('X', "X 轴朝前", "模型正面朝 -X"),
    ('Y', "Y 轴朝前", "模型正面朝 -Y（保持 Blender 原始坐标，推荐 Unreal Engine）"),
    ('Z', "Z 轴朝前", "模型正面朝 -Z"),
    ('-X', "-X 轴朝前", "模型正面朝 +X"),
    ('-Y', "-Y 轴朝前", "模型正面朝 +Y（整体绕竖轴旋转 180°）"),
    ('-Z', "-Z 轴朝前", "模型正面朝 +Z（Unity）"),
    )

UP_ITEMS = (
    ('X', "X 轴朝上", "向上轴为 +X"),
    ('Y', "Y 轴朝上", "向上轴为 +Y（Unity、Blender 默认 FBX 导出）"),
    ('Z', "Z 轴朝上", "向上轴为 +Z（Blender、Unreal Engine）"),
    ('-X', "-X 轴朝上", "向上轴为 -X"),
    ('-Y', "-Y 轴朝上", "向上轴为 -Y"),
    ('-Z', "-Z 轴朝上", "向上轴为 -Z"),
    )


def get_prefs(context=None):
  """Returns this addon's preferences, or None if they are not available yet."""
  context = context or bpy.context
  addon = context.preferences.addons.get(__package__)
  return addon.preferences if addon else None


def ensure_distinct_axes(prefs):
  """
  Keeps forward and up on two different axes.

  bpy_extras.io_utils.axis_conversion raises an exception when both use the
  same axis, so the second one is nudged to the next axis (the FBX exporter
  itself does the same thing via axis_conversion_ensure).
  """
  if prefs.axis_forward[-1] != prefs.axis_up[-1]:
    return

  next_axis = 'XYZ'[('XYZ'.index(prefs.axis_up[-1]) + 1) % 3]
  prefs.axis_up = prefs.axis_up[0:-1] + next_axis


def update_axis_forward(self, context):
  ensure_distinct_axes(self)


def update_axis_up(self, context):
  ensure_distinct_axes(self)


class BATEX_AddonPreferences(AddonPreferences):
  bl_idname = __package__

  # Stored in the user preferences, so the choice is remembered the next time
  # Blender is started.
  axis_forward: EnumProperty(
      name="前向轴",
      description="导出 FBX 文件时作为前向的轴",
      items=FORWARD_ITEMS,
      default='Y',
      update=update_axis_forward,
      )

  axis_up: EnumProperty(
      name="向上轴",
      description="导出 FBX 文件时作为向上的轴",
      items=UP_ITEMS,
      default='Z',
      update=update_axis_up,
      )


def get_axis_settings(context):
  """
  Returns a validated (axis_forward, axis_up) tuple for the FBX exporter.

  Falls back to Z up / Y forward (Epic's Blender to Unreal default) when the
  preferences cannot be reached.
  """
  prefs = get_prefs(context)
  if prefs is None:
    return 'Y', 'Z'

  ensure_distinct_axes(prefs)
  return prefs.axis_forward, prefs.axis_up
