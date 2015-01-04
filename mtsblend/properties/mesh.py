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
from .. import MitsubaAddon

from ..extensions_framework import declarative_property_group


@MitsubaAddon.addon_register_class
class mitsuba_mesh(declarative_property_group):
    ef_attach_to = ['Mesh', 'SurfaceCurve', 'TextCurve', 'Curve']

    controls = [
        'mesh_type',
        'normals'
    ]

    visibility = {
    }

    properties = [
        {
            'type': 'enum',
            'attr': 'mesh_type',
            'name': 'Export as',
            'items': [
                ('global', 'Use default setting', 'global'),
                ('serialized', 'Serialized Mesh', 'serialized'),
                ('binary_ply', 'Binary PLY', 'binary_ply')
            ],
            'default': 'global'
        },
        {
            'type': 'enum',
            'attr': 'normals',
            'name': 'Normal mode',
            'description': 'Specifies how Mitsuba obtains normal information',
            'items': [
                ('dihedralangle', 'Smooth vertex normals (using angle constraint)', 'dihedralangle'),
                ('vertexnormals', 'Smooth vertex normals (using connectivity)', 'vertexnormals'),
                ('facenormals', 'Flat face normals', 'facenormals'),
                ('default', 'Use normals from Blender', 'default')
            ],
            'default': 'default'
        }
    ]
