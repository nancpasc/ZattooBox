##################################
# ZattooBox Folder item
# 
# (c) 2014-2015 Pascal Nançoz
##################################

from resources.lib.core.zbdirectoryitem import ZBDirectoryItem
import xbmcgui

class ZBFolderItem(ZBDirectoryItem):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.IsFolder = True

	def get_listItem(self):
		return xbmcgui.ListItem(self.Title, iconImage=self.Image)