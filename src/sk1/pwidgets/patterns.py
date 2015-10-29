# -*- coding: utf-8 -*-
#
#	Copyright (C) 2015 by Igor E. Novikov
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.

DEFAULT_PATTERN = 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAAA3NCSVQICAjb4U/gAAAABlBMVEUAAAD///+l2Z/dAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAALHRFWHRDcmVhdGlvbiBUaW1lAFRodSAyNSBOb3YgMjAxMCAxNToyMDoyNyAtMDUwMCkZmaYAAAAQSURBVAiZY2D4z4AV4RAGAH6/D/F9RRmSAAAAAElFTkSuQmCC'

PATTERN_PRESETS = ['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']
