#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gio, GLib

bus = Gio.bus_get_sync(Gio.BusType.SESSION, None)

res = bus.call_sync(
	bus_name = 'org.fcitx.Fcitx',
	object_path = '/inputmethod',
	interface_name = 'org.fcitx.Fcitx.InputMethod',
	method_name = 'GetCurrentIM',
	parameters = None,
	reply_type = GLib.VariantType('(s)'),
	flags = Gio.DBusCallFlags.NONE,
	timeout_msec = -1,
	cancellable = None
)

if res != None:
	current_im = res.unpack()[0]
	print("CurrentIM: {current_im}".format(current_im=current_im))
