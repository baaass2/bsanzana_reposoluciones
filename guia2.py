#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
import json

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

def open_file():
    try:
        with open('compuestos.json', 'r') as file:
            data = json.load(file)
    except IOError:
        data = []
        
    return data


def save_file(data):
    print("Save File")
    
    with open('compuestos.json', 'w') as file:
        json.dump(data, file, indent=4)


def obtener_valor_combobox(combo):
    try:
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            seleccion = model[tree_iter][0]
        return seleccion
    except UnboundLocalError:
        error = 1
        return error


def llenar_combo(combo):
    
    clasificacion = ['Organico', 'Inorganico']
    lista = Gtk.ListStore(str)
    
    for i in clasificacion:
        lista.append([i])

    combo.set_model(lista)
    renderer_text = Gtk.CellRendererText()
    combo.pack_start(renderer_text, True)
    combo.add_attribute(renderer_text, "text", 0)
    
    
    
class main():
    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

        self.window = self.builder.get_object("main")
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_title("Base de datos de compuestos")

        self.add = self.builder.get_object("Add")
        self.add.connect("clicked", self.agregar_compuesto)
        self.delete = self.builder.get_object("Delete")
        self.delete.connect("clicked", self.elimnar_compuesto)
        self.edit = self.builder.get_object("Edit")
        self.edit.connect("clicked", self.editar_compuesto)
        
        self.entrynombre = self.builder.get_object("EntryNombre")
        self.entrymolecula = self.builder.get_object("EntryMolecula")
        self.combo_clasificacion = self.builder.get_object("Combobox")
        llenar_combo(self.combo_clasificacion)
        
        self.treeview = self.builder.get_object("Treeview")
        
        self.listmodel = Gtk.ListStore(str, str, str)
        
        self.treeview.set_model(model=self.listmodel)
        cell = Gtk.CellRendererText()
        
        title = ("Nombre", "Nombre molecular", "Clasificación")
        
        for i in range(len(title)):
            col = Gtk.TreeViewColumn(title[i], cell, text=i)
            self.treeview.append_column(col)
        
        self.actualizar_tree()

        self.window.show_all()
        
    def actualizar_tree(self):
        data = open_file()
    
        for i in range(len(data)):
            compuestos = []
            nombre = data[i]['nombre']
            molecula = data[i]['molecula']
            clasificacion = data[i]['clasificacion']
            compuestos.append(nombre)
            compuestos.append(molecula)
            compuestos.append(clasificacion)
            self.listmodel.append(compuestos)
            
            
    def agregar_compuesto(self, event):
        data = open_file()
        nombre = self.entrynombre.get_text()
        molecula = self.entrymolecula.get_text()
        self.sel_clasificacion = obtener_valor_combobox(self.combo_clasificacion)
        
        if nombre == '' or molecula == '':
            error = 2
            abrir = VentanaError(error)
        if self.sel_clasificacion != 1: 
            dic = {'nombre': nombre,
                    'molecula': molecula,
                    'clasificacion': self.sel_clasificacion}
            data.append(dic)
            save_file(data)
        
            ult_compuesto = [nombre, molecula, self.sel_clasificacion]
            self.listmodel.append(ult_compuesto)
        else: 
            abrir = VentanaError(self.sel_clasificacion)
            
            
    def elimnar_compuesto(self, event):
        abrir = VentanaEliminar(self.treeview)
            

    def editar_compuesto(self, event):
        abrir = VentanaEditar(self.treeview)
        

class VentanaError():
    def __init__(self, error):
        self.error = error

        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

        self.dialogo_error = self.builder.get_object("DialogoError")
        
        self.ok2 = self.builder.get_object("OK2")
        self.ok2.connect("clicked", self.cerrar_dialog_error)
        self.label = self.builder.get_object("Label")
        
        if error == 1:
            self.label.set_text("No se ha escojido clasificacion")
        
        elif error == 2:
            self.label.set_text("No se ha ingresado nombre o molecula")

        
        self.dialogo_error.show_all()
        
    def cerrar_dialog_error(self, event):
        self.dialogo_error.destroy()


class VentanaEditar():
    def __init__(self, treeview):
        self.treeview = treeview

        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

        self.veditar= self.builder.get_object("VentanaEditar")
        self.veditar.set_title("Base de datos de compuestos")
        
        self.entrynombre1 = self.builder.get_object("EntryNombre1")
        self.entrymolecula1 = self.builder.get_object("EntryMolecula1")
        self.combobox1 = self.builder.get_object("Combobox1")
        
        llenar_combo(self.combobox1)
        
        data = open_file()
        model, it = self.treeview.get_selection().get_selected()
        if model is None or it is None:
            self.veditar.destroy()
            return
        for i in range(len(data)):
            if data[i]['nombre'] == model.get_value(it, 0):
                self.iterador = i
                nombre = data[i]['nombre']
                molecula = data[i]['molecula']
                clasificacion = data[i]['clasificacion']
                self.entrynombre1.set_text(nombre)
                self.entrymolecula1.set_text(molecula)
        
        self.ok3 = self.builder.get_object("OK3")
        self.ok3.connect("clicked", self.edit_compuesto)
        
        self.cancelar2 = self.builder.get_object("Cancelar2")
        self.cancelar2.connect("clicked", self.cerrar_veditar)
    
        self.veditar.show_all()
        
    def cerrar_veditar(self, event):
        self.veditar.destroy()
    
    
    def edit_compuesto(self, event):
        nombre = self.entrynombre1.get_text()
        molecula = self.entrymolecula1.get_text()
        self.sel_clasificacion = obtener_valor_combobox(self.combobox1)
        data = open_file()
        
        if nombre == '' or molecula == '':
            error = 2
            abrir = VentanaError(error)
        if self.sel_clasificacion != 1: 
            data[self.iterador]['nombre'] = nombre 
            data[self.iterador]['molecula'] = molecula 
            data[self.iterador]['clasificacion'] = self.sel_clasificacion
            save_file(data)
        else:
            error = 1
            v = VentanaError(error)
            
        self.veditar.destroy()
        
class VentanaEliminar():
    def __init__(self, treeview):
        self.treeview = treeview
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

        self.dialog_elim = self.builder.get_object("DialogoEliminar")
        
        self.ok = self.builder.get_object("OK")
        self.ok.connect("clicked", self.eliminar)
        self.cancelar = self.builder.get_object("Cancel")
        self.cancelar.connect("clicked", self.cancelar_elim)
        
        model, it = self.treeview.get_selection().get_selected()
        if model is None or it is None:
            self.dialog_elim.destroy()
            return
            
        self.dialog_elim.show_all()
        
    def eliminar(self, event):
        data = open_file()
        model, it = self.treeview.get_selection().get_selected()
        for i in range(len(data)):
            if data[i]['nombre'] == model.get_value(it, 0):
                data.pop(i)
                break
        save_file(data)
       
        self.dialog_elim.destroy()

    
    def cancelar_elim(self, event):
        print("Se ha cancelado la eliminación")
        self.dialog_elim.destroy()

if __name__ == '__main__':
    jaja = main()
    Gtk.main()
