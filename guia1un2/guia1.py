#!/usr/bin/env python
# -*- coding: utf-8 -*-


import operator
import gi
import json

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class main():

    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file("gladeguia1.glade")

        self.window = self.builder.get_object("Window")
        self.window.set_default_size(800, 600)
        self.window.connect("destroy", Gtk.main_quit)
        
        self.texto1 = self.builder.get_object("EntryTexto1")
        self.texto2 = self.builder.get_object("EntryTexto2")
        
        
        self.aceptar = self.builder.get_object("Aceptar")
        self.aceptar.connect("clicked", self.dialogo_resultado)
        
        self.reset = self.builder.get_object("Reset")
        self.reset.connect("clicked", self.dialogo_advertencia)
        
        self.spinbutton = self.builder.get_object("EntrySpinButton")
        
        for evento in ['activate', 'changed']:
            self.texto1.connect(evento, self.medirlargo)
            self.texto2.connect(evento, self.medirlargo)
        
        self.window.show_all()
        
    
    def medirlargo(self, event):
        texto1 = self.texto1.get_text()
        texto2 = self.texto2.get_text()
        
        suma = len(texto1) + len(texto2)
        
        self.spinbutton.set_text(str(suma))
        
    def dialogo_resultado(self, event):
        entry_texto1 = self.texto1
        entry_texto2 = self.texto2
        entry_sbutton = self.spinbutton
        texto1 = self.texto1.get_text()
        texto2 = self.texto2.get_text()
       
        p = DialogoResultado(texto1, texto2, entry_texto1, entry_texto2, entry_sbutton)
    
    def dialogo_advertencia(self, event):
        entry_texto1 = self.texto1
        entry_texto2 = self.texto2
        entry_sbutton = self.spinbutton
        p = DialogoAdvertencia(entry_texto1, entry_texto2, entry_sbutton)
        
class DialogoResultado():
    
    def __init__(self, texto1, texto2, entry_texto1, entry_texto2, entry_sbutton):
        
        self.entry_texto1 = entry_texto1
        self.entry_texto2 = entry_texto2
        self.entry_sbutton = entry_sbutton
        self.texto1 = texto1
        self.texto2 = texto2
        largo = len(self.texto1)+len(self.texto2)

        self.builder = Gtk.Builder()
        self.builder.add_from_file("gladeguia1.glade")

        self.ventana_resultado = self.builder.get_object("DialogoResultado")
        self.ventana_resultado.set_default_size(600, 400)
        
        self.label_texto1 = self.builder.get_object("LabelTexto1Dialogo")        
        self.label_texto2 = self.builder.get_object("LabelTexto2Dialogo")
        self.label_largo = self.builder.get_object("LabelLargoTextoDialogo")
        
        self.aceptar = self.builder.get_object("AceptarDialogo")
        self.aceptar.connect("clicked", self.reiniciar)
        
        self.aceptar = self.builder.get_object("CancelarDialogo")
        self.aceptar.connect("clicked", self.cerrar)

        self.label_texto1.set_text(self.texto1)
        self.label_texto2.set_text(self.texto2)
        self.label_largo.set_text(str(largo))
        
        self.ventana_resultado.show_all()
        
    def reiniciar(self, event):
        self.entry_texto1.set_text("")
        self.entry_texto2.set_text("")
        self.entry_sbutton.set_text("")
        self.ventana_resultado.destroy()
        
    def cerrar(self, event):
        self.ventana_resultado.destroy()

class DialogoAdvertencia():
    
    def __init__(self, entry_texto1, entry_texto2, entry_sbutton):
        
        self.entry_texto1 = entry_texto1
        self.entry_texto2 = entry_texto2
        self.entry_sbutton = entry_sbutton
        self.builder = Gtk.Builder()
        self.builder.add_from_file("gladeguia1.glade")

        self.dialogo_reset = self.builder.get_object("DialogoReset")
        self.dialogo_reset.set_default_size(600, 400)
        
        self.aceptar = self.builder.get_object("AceptarDialogoReset")
        self.aceptar.connect("clicked", self.aceptar_dialogo)
        
        self.cancelar = self.builder.get_object("CancelarDialogoReset")
        self.cancelar.connect("clicked", self.cancelar_dialogo)
        
        self.dialogo_reset.show_all()
        
    def aceptar_dialogo(self, event):
        
        self.entry_texto1.set_text("")
        self.entry_texto2.set_text("")
        self.entry_sbutton.set_text("")
        self.dialogo_reset.destroy()
    
    def cancelar_dialogo(self, event):
        
        self.dialogo_reset.destroy()
    
    
    
    
if __name__ == '__main__':
    
    p = main()
    Gtk.main()
