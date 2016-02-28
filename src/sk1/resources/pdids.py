# -*- coding: utf-8 -*-
#
# 	Copyright (C) 2013 by Igor E. Novikov
#
# 	This program is free software: you can redistribute it and/or modify
# 	it under the terms of the GNU General Public License as published by
# 	the Free Software Foundation, either version 3 of the License, or
# 	(at your option) any later version.
#
# 	This program is distributed in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# 	GNU General Public License for more details.
#
# 	You should have received a copy of the GNU General Public License
# 	along with this program.  If not, see <http://www.gnu.org/licenses/>.

import wx

#----- Canvas modes
SELECT_MODE = wx.NewId()
SHAPER_MODE = wx.NewId()
ZOOM_MODE = wx.NewId()
FLEUR_MODE = wx.NewId()
LINE_MODE = wx.NewId()
CURVE_MODE = wx.NewId()
RECT_MODE = wx.NewId()
ELLIPSE_MODE = wx.NewId()
POLYGON_MODE = wx.NewId()
TEXT_MODE = wx.NewId()
GRADIENT_MODE = wx.NewId()

FILL_MODE = wx.NewId()
STROKE_MODE = wx.NewId()

ZOOM_OUT_MODE = wx.NewId()
MOVE_MODE = wx.NewId()
COPY_MODE = wx.NewId()

COPY_FILL = wx.NewId()
COPY_STROKE = wx.NewId()

MOVE_UP = wx.NewId()
MOVE_DOWN = wx.NewId()
MOVE_LEFT = wx.NewId()
MOVE_RIGHT = wx.NewId()

#----- File menu
ID_NEW_FROM_TEMPLATE = wx.NewId()
ID_SAVE_SEL = wx.NewId()
ID_SAVEALL = wx.NewId()
ID_IMPORT = wx.NewId()
ID_EXPORT = wx.NewId()
ID_CLEAR_LOG = wx.NewId()
ID_VIEW_LOG = wx.NewId()
#----- Edit menu
ID_CLEAR_UNDO = wx.NewId()
ID_DESELECT = wx.NewId()
ID_INV_SELECT = wx.NewId()
ID_DUPLICATE = wx.NewId()
#----- View menu
ID_STROKE_VIEW = wx.NewId()
ID_DRAFT_VIEW = wx.NewId()
ID_PREV_ZOOM = wx.NewId()
ID_ZOOM_PAGE = wx.NewId()
ID_SHOW_GRID = wx.NewId()
ID_SHOW_GUIDES = wx.NewId()
ID_SHOW_SNAP = wx.NewId()
ID_SHOW_PAGE_BORDER = wx.NewId()
ID_SNAP_TO_GRID = wx.NewId()
ID_SNAP_TO_GUIDE = wx.NewId()
ID_SNAP_TO_OBJ = wx.NewId()
ID_SNAP_TO_PAGE = wx.NewId()
#----- Layout menu
ID_INSERT_PAGE = wx.NewId()
ID_DELETE_PAGE = wx.NewId()
ID_GOTO_PAGE = wx.NewId()
ID_NEXT_PAGE = wx.NewId()
ID_PREV_PAGE = wx.NewId()
ID_GUIDES_AT_CENTER = wx.NewId()
ID_PAGE_FRAME = wx.NewId()
ID_PAGE_GUIDE_FRAME = wx.NewId()
ID_REMOVE_ALL_GUIDES = wx.NewId()
#----- Arrange menu
ID_CLEAR_TRANSFORM = wx.NewId()
ID_POSITION_PLGN = wx.NewId()
ID_RESIZE_PLGN = wx.NewId()
ID_SCALE_PLGN = wx.NewId()
ID_ROTATE_PLGN = wx.NewId()
ID_SHEAR_PLGN = wx.NewId()
ID_ROTATE_LEFT = wx.NewId()
ID_ROTATE_RIGHT = wx.NewId()
ID_MIRROR_H = wx.NewId()
ID_MIRROR_V = wx.NewId()
ID_ALIGN_PLGN = wx.NewId()
ID_COMBINE = wx.NewId()
ID_BREAK_APART = wx.NewId()
ID_RAISE_TO_TOP = wx.NewId()
ID_RAISE = wx.NewId()
ID_LOWER = wx.NewId()
ID_LOWER_TO_BOTTOM = wx.NewId()
ID_GROUP = wx.NewId()
ID_UNGROUP = wx.NewId()
ID_UNGROUPALL = wx.NewId()
ID_PATHS_EXCLUSION = wx.NewId()
ID_PATHS_FUSION = wx.NewId()
ID_PATHS_INTERSECTION = wx.NewId()
ID_PATHS_TRIM = wx.NewId()
ID_TO_CONTAINER = wx.NewId()
ID_FROM_CONTAINER = wx.NewId()
ID_TO_CURVES = wx.NewId()
ID_STROKE_TO_CURVES = wx.NewId()

#----- Paths menu
ID_BEZIER_SEL_ALL_NODES = wx.NewId()
ID_BEZIER_REVERSE_ALL_PATHS = wx.NewId()
ID_BEZIER_SEL_SUBPATH_NODES = wx.NewId()
ID_BEZIER_DEL_SUBPATH = wx.NewId()
ID_BEZIER_REVERSE_SUBPATH = wx.NewId()
ID_BEZIER_EXTRACT_SUBPATH = wx.NewId()
ID_BEZIER_ADD_NODE = wx.NewId()
ID_BEZIER_DELETE_NODE = wx.NewId()
ID_BEZIER_ADD_SEG = wx.NewId()
ID_BEZIER_DELETE_SEG = wx.NewId()
ID_BEZIER_JOIN_NODE = wx.NewId()
ID_BEZIER_SPLIT_NODE = wx.NewId()
ID_BEZIER_SEG_TO_LINE = wx.NewId()
ID_BEZIER_SEG_TO_CURVE = wx.NewId()
ID_BEZIER_NODE_CUSP = wx.NewId()
ID_BEZIER_NODE_SMOOTH = wx.NewId()
ID_BEZIER_NODE_SYMMETRICAL = wx.NewId()

#----- Bitmaps menu
ID_CONV_TO_CMYK = wx.NewId()
ID_CONV_TO_RGB = wx.NewId()
ID_CONV_TO_LAB = wx.NewId()
ID_CONV_TO_GRAY = wx.NewId()
ID_CONV_TO_BW = wx.NewId()
ID_INVERT_BITMAP = wx.NewId()
ID_REMOVE_ALPHA = wx.NewId()
ID_INVERT_ALPHA = wx.NewId()
ID_EXTRACT_BITMAP = wx.NewId()
#----- Text menu
ID_EDIT_TEXT = wx.NewId()
ID_UPPER_TEXT = wx.NewId()
ID_LOWER_TEXT = wx.NewId()
ID_CAPITALIZE_TEXT = wx.NewId()
#----- Tools menu
ID_TOOL_PAGES = wx.NewId()
ID_TOOL_LAYERS = wx.NewId()
ID_TOOL_OBJBROWSER = wx.NewId()
#----- Help menu
ID_REPORT_BUG = wx.NewId()
ID_APP_WEBSITE = wx.NewId()
ID_APP_FORUM = wx.NewId()
ID_APP_FBPAGE = wx.NewId()

