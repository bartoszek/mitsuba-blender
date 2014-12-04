# -*- coding: utf8 -*-
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
# --------------------------------------------------------------------------
# Blender Mitsuba Add-On
# --------------------------------------------------------------------------
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
# ***** END GPL LICENSE BLOCK *****
#
import bpy
import bl_ui

from ... import MitsubaAddon


@MitsubaAddon.addon_register_class
class MitsubaTexture_PT_presets(bl_ui.properties_texture.TextureButtonsPanel, bpy.types.Panel):
    '''
    Texture Editor UI Panel
    '''

    bl_label = 'Mitsuba Texture Presets'
    bl_options = {'DEFAULT_CLOSED'}
    COMPAT_ENGINES = {'MITSUBA_RENDER'}

    @classmethod
    def poll(cls, context):
        '''
        Only show Mitsuba panel with the correct context
        '''
        tex = context.texture
        return  tex and (context.scene.render.engine in cls.COMPAT_ENGINES)

    def draw(self, context):
        row = self.layout.row(align=True)
        row.menu("MITSUBA_MT_presets_texture", text=bpy.types.MITSUBA_MT_presets_texture.bl_label)
        row.operator("mitsuba.preset_texture_add", text="", icon="ZOOMIN")
        row.operator("mitsuba.preset_texture_add", text="", icon="ZOOMOUT").remove_active = True
