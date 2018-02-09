# - *- coding: utf- 8 - *-
import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "Hello World!"
line2 = "First test successfully executed"
line3 = "Using Python"


xbmcgui.Dialog().ok(addonname, line1, line2, line3)

xbmcgui.Dialog().select('Wähle irgendwas aus...', ['1','2','3'])