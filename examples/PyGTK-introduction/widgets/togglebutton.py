#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk


def button_callback(widget=None, data=None):
	print "%s was toggled %s" % (data, ("off", "on")[widget.get_active()])

def main():
	win = gtk.Window(gtk.WINDOW_TOPLEVEL)
	win.connect("delete_event", lambda wid, we: gtk.main_quit())
	vbox = gtk.VBox(True, 2)
	win.add(vbox)

	button1 = gtk.ToggleButton("Toggle Button 1")
	button2 = gtk.ToggleButton("Toggle Button 2")

	button1.connect("toggled", button_callback, "Button 1")
	button2.connect("toggled", button_callback, "Button 2")

	vbox.pack_start(button1, True, True, 2)
	vbox.pack_start(button2, True, True, 2)

	win.show_all()
	
if __name__ == "__main__":
	main()
	gtk.main()
