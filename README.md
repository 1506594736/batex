# Batex
Export selected objects as fbx in batch operation.

### Features
* One fbx file per selected object
* Set the pivot point to center before exporting (useful e.g. for Unreal Engine 4 imports)
* Set the smoothing type before exporting (e.g. for low poly objects set it to FACE)
* **Choose the forward and up axis of the exported file (Unreal Engine, Unity, ...)**
* Define export folder, which is stored to .blend-file
* Open export folder with one click
* Export armature and animations

### Installing
1. Download zip file: https://github.com/1506594736/batex/archive/master.zip
2. Open Blender
3. Go to edit -> preferences -> addons
4. Click install button
5. Select the zip file you downloaded
6. Check the box next to "inport-Export: Batex" to enable plugin

### Using
* After installing Batex panel is added to the sidebar (below item/tool/view, right side of 3d viewport)
* Sidebar can be shown/hidden with the 'n' key.
* Change options and use the 'Export' button to export

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

