#!/usr/bin/python 

from gi.repository import Gio 
import ConfigParser
import pynotify
import os
import mimetypes

inifile = '/home/emmanuel/changewallpaper.ini'
SCHEMA = 'org.gnome.desktop.background' 
KEY = 'picture-uri' 
OPTIONS = 'picture-options'
folder= '/home/emmanuel/Papel tapiz'


cfg = ConfigParser.RawConfigParser()
cfg.read(inifile)
try:
	FILENO=cfg.getint('options','filenumber')
	FILENO=int(FILENO) + 1
except:
	FILENO='0'
files = []
for item in os.listdir(folder):
        mimetype = mimetypes.guess_type (item)[0]
        if mimetype and mimetype.split ('/')[0] == "image":
                files.append (item)
files.sort()
if int(FILENO) >= len(files):
	FILENO='0'
gsettings = Gio.Settings.new(SCHEMA) 
gsettings.set_string(KEY, "file://" + folder + "/" + files[int(FILENO)])
gsettings.set_string(OPTIONS, "scaled")
gsettings.apply() 
cfg.set('options','filenumber', int(FILENO))
cfg.set('options','file', files[int(FILENO)])
pynotify.init (str(FILENO))
Hello=pynotify.Notification ("ChangeWallpaper", message=files[int(FILENO)],icon=folder + '/' + files[int(FILENO)])

Hello.show ()
with open(inifile, 'wb') as configfile:
    cfg.write(configfile)

