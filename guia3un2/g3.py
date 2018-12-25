#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
import re
from datetime import date    
today = date.today().isoformat()
AÑO = int(today[0]+today[1]+today[2]+today[3])
print(AÑO)


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def correo_verificador(correo):
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
        return 1

    else:
        error = 'correo_invalido'
        abrir = DialogoError(error)
        
def digito_verificador(rut):
    try:
        if len(rut) <= 8:
            value = 11 - sum([ int(a)*int(b)  for a,b in zip(str(rut).zfill(8), '32765432')])%11
            return 1
        else:
            error =  'rut_invalido'
            abrir = DialogoError(error)
            
    except:
        error =  'rut_invalido'
        abrir = DialogoError(error)
def revisar_campo_vacio(entrynombre):
        contador = 0
        text = entrynombre.get_text()
        for i in range(len(text)):
            if text[i] == '' or text[i] == ' ':
                contador = contador + 1
                if contador == len(text):
                    entrynombre.grab_focus_without_selecting()

class main():
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

        self.window = self.builder.get_object("main")
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_title("Formulario")
        
        self.entrynombre = self.builder.get_object("EntryNombre")
        self.label = self.builder.get_object("LabelOperacion")

        self.calendario = self.builder.get_object("Calendario")
        
        self.entrydire = self.builder.get_object("EntryDireccion")
        self.entrydire.connect("changed", self.revisar_campo_de_nombre)
        
        self.entryrut = self.builder.get_object("EntryRut")
        self.entrycorreo = self.builder.get_object("EntryCorreo")
        
        self.botonaceptar = self.builder.get_object("Aceptar")
        self.botonaceptar.connect("clicked", self.revisar_campos)
        
        self.window.show_all()
    
    def revisar_campo_de_nombre(self, event):
        revisar_campo_vacio(self.entrynombre)
    
    def revisar_campos(self, event):
        revisar_campo_vacio(self.entrynombre)
        rut = self.entryrut.get_text()
        correo = self.entrycorreo.get_text()
        error = digito_verificador(rut)
        error1 = correo_verificador(correo)
        
        if error1 == 1 and error == 1:
            label = self.label.get_text()
            fecha = self.calendario.get_date()
            añousr = fecha[0]
            operacion = AÑO - añousr
            label = label + str(operacion)
            self.label.set_text(label)

        
        
class DialogoError():
    def __init__(self, error):
        self.error = error
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

        self.window1 = self.builder.get_object("DialogoError")
        self.labelerror = self.builder.get_object("LabelDIalogo")
        self.ok = self.builder.get_object("OK")
        self.ok.connect("clicked", self.cerrar)

        
        if self.error == 'rut_invalido':
            self.labelerror.set_text('Rut invalido')
        elif self.error == 'correo_invalido':
            self.labelerror.set_text('Correo invalido')
        
        self.window1.show_all()
    
    def cerrar (self, event):
        self.window1.destroy()
        

if __name__ == '__main__':
    jaja = main()
    Gtk.main()
