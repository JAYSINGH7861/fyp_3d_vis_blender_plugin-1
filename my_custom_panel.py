import bpy
import os



class OpenFilebrowser(bpy.types.Operator):
    bl_idname = "test.open_filebrowser"
    bl_label = "Select a file"
    
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        print("Selected file:", self.filepath)
        context.scene.my_file_path = self.filepath  # Store the filepath in the scene property
        return {'FINISHED'}
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class VIEW3D_PT_my_custom_panel(bpy.types.Panel): 
   
    bl_space_type = "VIEW_3D"  
    bl_region_type = "UI"  

    bl_category = "3D Visualization"  
    bl_label = "3D Visualization Toolkit"  

    def draw(self, context):
        """define the layout of the panel"""
        row = self.layout.row()
        row.operator("test.open_filebrowser", text="Open CSV File")
        row = self.layout.row()
        row.label(text="Selected file:")
        row = self.layout.row()
        row.label(text=context.scene.my_file_path)
        row = self.layout.row()
        row.operator("mesh.primitive_ico_sphere_add", text="Add Icosphere")
        row = self.layout.row()
        row.operator("object.shade_smooth", text="Shade Smooth")


def register():
    bpy.utils.register_class(OpenFilebrowser)
    bpy.utils.register_class(VIEW3D_PT_my_custom_panel)
    bpy.types.Scene.my_file_path = bpy.props.StringProperty(
        name="File Path",
        description="Path of the selected file",
        default=""
    )

def unregister():
    del bpy.types.Scene.my_file_path
    bpy.utils.unregister_class(OpenFilebrowser)
    bpy.utils.unregister_class(VIEW3D_PT_my_custom_panel)

if __name__ == "__main__":
    register()