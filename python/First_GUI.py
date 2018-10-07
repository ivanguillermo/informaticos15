#!/usr/bin/python
# -*- coding: utf-8 -*-

#importando repositorio de GUI
from gi.repository import Gtk

#Creando la clase del GUI
class ourwindow(Gtk.Window):


#Programa init de la clase
    def __init__(self):
        Gtk.Window.__init__(self, title="Simpson Method")
        Gtk.Window.set_default_size(self, 800,650)
        Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)

        age = input("What is your age? ")
        button1 = Gtk.Button(age)
        button1.connect("clicked", self.whenbutton1_clicked)

        self.add(button1)
        
    def whenbutton1_clicked(self, button):
    	print age
		


#creando objeto de clase ourwindow 
window = ourwindow()        

window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
