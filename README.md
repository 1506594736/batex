# Batex

批量导出选定对象为 FBX 的 Blender 插件（Batex 汉化分支）。

## 中文说明

### 功能
* 每个选定对象导出为一个独立的 fbx 文件
* 导出前把轴心移动到世界原点（对导入 UE 很有用）
* 导出前设置平滑方式（低模建议选「面」）
* **可选择导出文件的前向轴与向上轴（Unreal Engine / Unity 等）**
* 导出目录保存在 .blend 文件中，并支持一键打开
* 支持导出骨骼与动画

### 安装
1. 下载插件压缩包：https://github.com/1506594736/batex/archive/master.zip
2. 打开 Blender
3. 编辑 → 偏好设置 → 插件
4. 右上角下拉菜单选择「从磁盘安装」
5. 选中刚下载的 zip 文件
6. 勾选列表中的「Batex」启用插件

> 安装后的插件目录名为 `batex-master`（压缩包的顶层目录名），属正常现象。

### 使用
* 安装后，3D 视图右侧边栏（按 `N` 键显示/隐藏）会出现「Batex」标签页，面板名为 `Batex`（品牌名不翻译）
* 设置好选项后点击「导出」按钮即可批量导出

### 轴向转换

「前向轴 / 向上轴」决定写入 FBX 文件的坐标轴系。选择会保存在 Blender 用户偏好设置中，下次启动自动沿用。

导出器会保证文件自洽：模型正面朝向写入文件头的 `FrontAxis`，向上方向写入 `UpAxis`；因此凡是读取文件头的软件（Unreal Engine、Unity、Blender 自身）都会把模型还原成它在 Blender 中的朝向。

| 前向轴 | 向上轴 | 结果 |
| --- | --- | --- |
| `Y` | `Z` | 坐标与 Blender 完全一致，文件头声明 Z 轴向上、正面朝 -Y。**推荐 Unreal Engine**（Epic 官方 Blender 导 UE 工具用的就是这组）|
| `-Y` | `Z` | 同样是 Z 轴向上的文件，但模型绕竖轴旋转了 180° |
| `-Z` | `Y` | Blender 默认 FBX 导出设置，Y 轴向上（Unity）|
| `X` | `Z` | Z 轴向上的文件，模型绕竖轴旋转 90° |

导入后模型绕竖轴朝向不对，就切换「前向轴」的正负号（`Y` ↔ `-Y`）；如果模型是躺着的，说明「向上轴」选错了（Unreal Engine / Blender 用 `Z`，Unity 用 `Y`）。

前向轴与向上轴不能是同一条轴；选到冲突组合时，程序会自动把「向上轴」移到下一条轴。

### 更新插件
1. 重新下载上面的 zip（该链接始终打包 master 分支的最新提交）
2. 再次用「从磁盘安装」覆盖安装
3. **重启 Blender**（或在偏好设置里取消勾选再重新勾选插件）—— 覆盖文件后 Blender 不会自动重新注册面板，不重启就看不到新界面

### 致谢与许可

Batex 由 [jayanam](https://github.com/jayanam) 原创，基于 [GPL-3.0](LICENSE) 许可发布。本汉化分支由 [1506594736](https://github.com/1506594736) 维护。

---

## English

Batch export selected objects as fbx (Chinese localized fork of Batex).
The add-on user interface is in Chinese.

### Features
* One fbx file per selected object
* Set the pivot point to center before exporting (useful e.g. for Unreal Engine imports)
* Set the smoothing type before exporting (e.g. for low poly objects set it to FACE)
* **Choose the forward and up axis of the exported file (Unreal Engine, Unity, ...)**
* Define export folder, which is stored to .blend-file
* Open export folder with one click
* Export armature and animations

### Installing
1. Download zip file: https://github.com/1506594736/batex/archive/master.zip
2. Open Blender
3. Go to edit -> preferences -> addons
4. Pick "Install from Disk" from the dropdown in the top right
5. Select the zip file you downloaded
6. Check the box next to "Batex" to enable the add-on

> The installed folder is named `batex-master` (the top level folder of the
> archive), this is expected.

### Using
* After installing, the panel is added to the sidebar of the 3D view (press `n`
  to show/hide it), inside the "Batex" tab
* Change the options and press the export button

### Axis conversion

The Forward / Up pickers define the axis system that is written into the FBX
file. Values are stored in the Blender user preferences, so the last choice is
remembered the next time Blender is started.

The exporter keeps the file self consistent: the direction the front of the
model points is written to the file header (`FrontAxis`) and the up direction is
written to `UpAxis`, so any application that reads the header (Unreal Engine,
Unity, Blender itself) converts the asset back to the orientation it has in
Blender.

| Forward | Up | Result |
| --- | --- | --- |
| `Y` | `Z` | Coordinates are written exactly as they are in Blender, header says Z up / -Y front. **Recommended for Unreal Engine** (this is what Epic's own Blender to Unreal exporter uses) |
| `-Y` | `Z` | Same Z up file, but the model is rotated 180 degrees around the up axis |
| `-Z` | `Y` | Blender's default FBX export, Y up (Unity) |
| `X` | `Z` | Z up file rotated 90 degrees around the up axis |

If an imported asset is rotated around the up axis, flip the sign of Forward
(`Y` / `-Y`). If it lies on its side, Up is wrong (`Z` for Unreal Engine and
Blender, `Y` for Unity).

Forward and Up may never use the same axis - if you pick a colliding
combination, the Up value is moved to the next axis automatically.

### Updating
1. Download the zip again (the link above always packages the latest commit of
   the master branch)
2. Install it again with "Install from Disk" (it overwrites the existing folder)
3. **Restart Blender** (or disable and re-enable the add-on) - replacing the
   files does not re-register the panels, a restart is needed to see the new UI

### Credits
Batex was originally written by [jayanam](https://github.com/jayanam) and is
released under the [GPL-3.0](LICENSE) license. This fork is maintained by
[1506594736](https://github.com/1506594736).

