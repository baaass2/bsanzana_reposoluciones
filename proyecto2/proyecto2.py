#!/usr/bin/env python
# -*- coding: utf-8 -*-
import operator
import gi
import json

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

def open_file_life():
    try:
        with open('prisionerosvida.json', 'r') as file:
            data1 = json.load(file)
    except IOError:
        data1 = []
        
    return data1

def save_file_life(data1):
    print("Save File")
    
    with open('prisionerosvida.json', 'w') as file:
        json.dump(data1, file, indent=4)

def open_file():
    try:
        with open('prisioneros.json', 'r') as file:
            data = json.load(file)
    except IOError:
        data = []
        
    return data

def save_file(data):
    print("Save File")
    
    with open('prisioneros.json', 'w') as file:
        json.dump(data, file, indent=4)

def open_file_cuentas():
    try:
        with open('cuentas.json', 'r') as file:
            data2 = json.load(file)
    except IOError:
        data2 = []
        
    return data2

def save_file_cuentas(data2):
    print("Save File")
    
    with open('cuentas.json', 'w') as file:
        json.dump(data2, file, indent=4)

def open_file_carcel():
    try:
        with open('carceles.json', 'r') as file:
            data3 = json.load(file)
    except IOError:
        data3 = []
        
    return data3

def save_file_carcel(data3):
    print("Save File")
    
    with open('carceles.json', 'w') as file:
        json.dump(data3, file, indent=4)

def obtener_valor_combobox(self, combo):
    tree_iter = combo.get_active_iter()
    if tree_iter is not None:
        model = combo.get_model()
        seleccion = model[tree_iter][0]

    return seleccion
        
class InicioSesion():

    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file("iniciosesion.glade")

        window = self.builder.get_object("window")
        window.set_title("Inicio de Sesión")
        window.connect("destroy", Gtk.main_quit)

        #USUARIO
        self.usuario = self.builder.get_object("Usuario")
        #CONTRASEÑA
        self.contraseña = self.builder.get_object("Contraseña")

        #RESULTADO DE SESIÓN
        self.resultado = self.builder.get_object("Resultado")
        # BOTON OK
        self.botonOK = self.builder.get_object("OK")
        self.botonOK.connect("clicked", self.revisar_cuenta)
        
        self.crearcuenta = self.builder.get_object("CrearCuenta")
        self.crearcuenta.connect("clicked", self.crear_cuenta)


        window.show_all()

    
    def crear_cuenta(self, event):
        p = CrearCuenta()
        
    def revisar_cuenta(self, btn=None):
        usuario = self.usuario.get_text()
        contraseña = self.contraseña.get_text()
        
        data2 = open_file_cuentas()
        for i in range(len(data2)):
            if usuario == data2[i]['usuario'] and contraseña == data2[i]['contraseña']:
                rango = data[i]['rango']
                v = VentanaIngresarCarcel(rango)
            else:    
                self.resultado.set_text("Usuario o contraseña incorrectos")

class CrearCuenta():
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("iniciosesion.glade")
        self.v_crearcuenta = self.builder.get_object("VentanaCrearCuenta")
        self.v_crearcuenta.set_title("Crear Cuenta")
        
        self.usuario = self.builder.get_object("EntryUsuario")
        self.contraseña = self.builder.get_object("EntryContrasena")
        self.comborango = self.builder.get_object("ComboRango")
        self.cancelar_crearcuenta = self.builder.get_object("CancelarCrearCuenta")
        self.cancelar_crearcuenta.connect("clicked", self.cancelarcrearcuenta)
        self.aceptar_crearcuenta = self.builder.get_object("OkCrearCuenta")
        self.aceptar_crearcuenta.connect("clicked", self.datos_cuenta)
        
        self.v_crearcuenta.show_all()
        
    def datos_cuenta(self, event):
        usuario = self.usuario.get_text()
        contraseña = self.contraseña.get_text()
        combo=self.comborango
        rango = obtener_valor_combobox(self, combo)
        
        data2 = open_file_cuentas()
        
        dic = {'usuario':usuario,
                'contraseña':contraseña,
                'rango':rango}
        data2.append(dic)
        
        save_file_cuentas(data2)

        self.v_crearcuenta.destroy()
    def cancelarcrearcuenta(self, event):
        self.v_crearcuenta.destroy()
        
        
class VentanaIngresarCarcel():
    def __init__(self, rango):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")
        
        self.ventana_carcel = self.builder.get_object("VentanaCarcel")
        self.ventana_carcel.set_title("Inicio de Carcel")
        
        self.crear_carcel = self.builder.get_object("CrearCarcel")
        self.crear_carcel.connect("clicked", self.formulariocarcel)
        
        self.ventana_carcel.show_all()
        
        
    def formulariocarcel(self, event):
        p = FormularioCarcel()
    
        
class FormularioCarcel():
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")
        
        self.formulario_carcel = self.builder.get_object("FormularioCarcel")
        self.formulario_carcel.set_title("FormularioCarcel")
        
        self.nombre_carcel = self.builder.get_object("EntryNombreCarcel")
        self.numero_celda = self.builder.get_object("SpinNumeroCelda")
        self.capacidad_celda = self.builder.get_object("SpinCapacidadCelda")   
        self.aceptar_formulario = self.builder.get_object("OkFormularioCarcel")
        self.aceptar_formulario.connect("clicked", self.datos_carcel)
        self.cancelar_formulario = self.builder.get_object("CancelarFormularioCarcel")
        self.cancelar_formulario.connect("clicked", self.cancelar_vformulario)     
        
        self.formulario_carcel.show_all()
        
    def datos_carcel(self, event):
        nombrecarcel = self.nombre_carcel.get_text()
        numerocelda = self.numero_celda.get_value()
        capacidadcelda = self.capacidad_celda.get_value()
        
        dic = {str(nombrecarcel):[numerocelda,capacidadcelda]}
        
        data3 = open_file_carcel()
        data3.append(dic)
        
        save_file_carcel(data3) 
        
        self.formulario_carcel.destroy()
    
    def cancelar_vformulario(self, event):
        self.formulario_carcel.destroy()

    
    
class VentanaMain():
    
    def __init__(self, usuario):
        
        self.usuario = usuario
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")
        
        window2 = self.builder.get_object("window2")
        window2.set_default_size(600, 400)
        window2.set_title("Menú")
        window2.connect("destroy", Gtk.main_quit)
        
        #BOTON AGREGAR
        
        self.boton_agregar = self.builder.get_object("Agregar")
        self.boton_agregar.connect("clicked", self.dialogo_add)
        
        #BOTON VER TODO
        self.boton_buscar_todo = self.builder.get_object("VerTodo")
        self.boton_buscar_todo.connect("clicked", self.dialogo_ver_todo)
        
        #BOTON BUSCAR
        
        self.boton_buscar = self.builder.get_object("BotonBuscar")
        self.boton_buscar.connect("clicked", self.dialogo_buscar)
        
        window2.show_all()
    
    def dialogo_add(self, btn=None):
        
        if (self.usuario != 'Guardia'):
            d = VentanaAdd()
        elif(self.usuario == 'Guardia'):
            d = VentanaPermiso()
        
    def dialogo_ver_todo(self, btn=None):
        d = VentanaVerTodo()
    
    def dialogo_buscar(self, btn=None):
        self.rut_buscar = self.builder.get_object("Buscar")
        rut = self.rut_buscar.get_text()
        d = VentanaBuscar(rut, self.usuario)    
        
class VentanaAdd():
    
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")
            
        self.dialogo_prisionero = self.builder.get_object("DialogoPrisionero")
        self.dialogo_prisionero.set_title("Información de Prisionero")
        
        self.nombre = self.builder.get_object("Nombre")
        self.apellido = self.builder.get_object("Apellido")
        self.rut = self.builder.get_object("Rut")
        self.nacionalidad = self.builder.get_object("Nacionalidad")
        self.celda = self.builder.get_object("Celda")
        self.sentencia = self.builder.get_object("Sentencia")
        self.estado = self.builder.get_object("Estado")
        self.descripcion = self.builder.get_object("Descripción")
        
        self.botonOK = self.builder.get_object("OK")
        self.botonOK.connect("clicked", self.guardar_información)
        self.botonCANCELAR = self.builder.get_object("CANCEL")
        self.botonCANCELAR.connect("clicked", self.cancelar_dialogo)
        
        self.dialogo_prisionero.show_all()
        
    def guardar_información(self, btn=None):
        
        nombre = self.nombre.get_text()
        apellido = self.apellido.get_text()
        rut = self.rut.get_text()
        nacionalidad = self.nacionalidad.get_text()
        celda = self.celda.get_text()
        sentencia = self.sentencia.get_text()
        estado = self.estado.get_text()
        descripcion = self.descripcion.get_text()
        
        
        data1 = open_file_life()
        
        data1.append({str(rut):[]})
        
        for i in range(len(data1)):
            x = data1[i].keys()
            if(rut == (list(x)[0])):
                data1[i][str(rut)].append(descripcion)
        
        save_file_life(data1)
    
        
        dic = {"nombre": nombre,
                "apellido": apellido,
                "rut": rut,
                "nacionalidad": nacionalidad,
                "celda": celda,
                "sentencia": sentencia,
                "estado": estado,
                "descripcion": descripcion}
        
        data = open_file()
        data.append(dic)
        save_file(data)
        
        d = VentanaExito()
        
        self.dialogo_prisionero.destroy()
        
    def cancelar_dialogo(self, btn=None):
        self.dialogo_prisionero.destroy()
                
class VentanaVerTodo():
    
    def __init__(self):
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")
            
        self.lista_prisionero = self.builder.get_object("ListaPrisionero")
        self.lista_prisionero.set_default_size(600, 400)
        self.lista_prisionero.set_title("Lista de Prisionero")
        
        self.listmodel = Gtk.ListStore(str, str, str, str, str, str, str, str)
        self.treeResultado = self.builder.get_object("TreeResultado")
        self.treeResultado.set_model(model=self.listmodel)
        cell = Gtk.CellRendererText()
        
        
        title = ("Nombre", "Apellido", "Rut", "Nacionalidad", "Sentencia", "Celda", "Estado", "Descripcion")
        
        for i in range(len(title)):
            col = Gtk.TreeViewColumn(title[i], cell, text=i)
            self.treeResultado.append_column(col)
        
        self.mostrar_data()

        self.lista_prisionero.show_all()
        
    def mostrar_data(self):
        
        data = open_file()
    
        for i in data:
            x = [x for x in i.values()]
            print(x)
            self.listmodel.append(x)

class VentanaBuscar():
    
    def __init__(self, rut, usuario):
        self.usuario = usuario
        self.rut = rut
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

            
        self.lista_prisionero1 = self.builder.get_object("ListaPrisionero1")
        self.lista_prisionero1.set_default_size(600, 400)
        self.lista_prisionero1.set_title("Lista de Prisionero")
    
        
        self.listmodel = Gtk.ListStore(str, str, str, str, str, str, str, str)
        self.treeResultado1 = self.builder.get_object("TreeResultado1")
        self.treeResultado1.set_model(model=self.listmodel)
        cell = Gtk.CellRendererText()
        
        self.liberar = self.builder.get_object("Liberar")
        self.liberar.connect("clicked", self.liberar_prisionero)
        
        self.encerrar = self.builder.get_object("Encerrar")
        self.encerrar.connect("clicked", self.encerrar_prisionero)
        
        self.hoja_de_vida = self.builder.get_object("HojaVida")
        self.hoja_de_vida.connect("clicked", self.dialogo_hojavida)
        
        self.e_descripcion = self.builder.get_object("EditarDescripción")
        self.e_descripcion.connect("clicked", self.editar_descripcion)
        
        
        title = ("Nombre", "Apellido", "Rut", "Nacionalidad", "Sentencia", "Celda", "Estado", "Descripcion")
        
        for i in range(len(title)):
            col = Gtk.TreeViewColumn(title[i], cell, text=i)
            self.treeResultado1.append_column(col)
        
        self.mostrar_data()

        self.lista_prisionero1.show_all()
        
    def mostrar_data(self):
        
        data = open_file()
        
        for i in range(len(data)):
            if(self.rut == data[i]['rut']):
                busqueda = data[i].values()
                self.listmodel.append(busqueda)
                
        self.lista_prisionero1.show_all()
    
    def liberar_prisionero(self, event):
        
        if(self.usuario == 'Alcaide'):
            data = open_file()
            for i in range(len(data)):
                if(self.rut == data[i]['rut']):
                    it = i
                    data[it]['estado'] = 'Liberado'
                    save_file(data)
                    d = VentanaExito()
                    
        elif(self.usuario != 'Alcaide'): 
            d = VentanaPermiso()               
    def dialogo_hojavida(self, event):
        
        d = VentanaHojaVida(self.rut)
        
    def encerrar_prisionero(self, event):

        if(self.usuario == 'Alcaide'):
            data = open_file()
            for i in range(len(data)):
                if(self.rut == data[i]['rut']):
                    it = i
                    data[it]['estado'] = 'Prisionero'
                    save_file(data)
                    d = VentanaExito()
                    
        elif(self.usuario != 'Alcaide'): 
            d = VentanaPermiso() 

    def editar_descripcion(self, event):
        
        if(self.usuario != 'Guardia'):
            d = VentanaEdicionDescripcion(self.rut)
        elif(self.usuario == 'Guardia'):
            d = VentanaPermiso()
                
class VentanaEdicionDescripcion():
        
    def __init__(self, rut):
        self.rut = rut
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

            
        self.editar = self.builder.get_object("Editar")
        self.editar.set_default_size(600, 400)
        self.editar.set_title("Edición de Descripción")
    
        self.boton_OK_editar = self.builder.get_object("BotonOKEditar")
        self.boton_OK_editar.connect("clicked", self.editar_descripcion)
        
        self.boton_cancelar1 = self.builder.get_object("BotonCancelarEditar")
        self.boton_cancelar1.connect("clicked", self.cancelar_edicion)
        
        self.entry_descripcion = self.builder.get_object("EntryDescripcion")
        self.entry_sentencia = self.builder.get_object("EntrySentencia")
        
        
        self.editar.show_all()
        
    def editar_descripcion(self, event):
        nueva_descripcion = self.entry_descripcion.get_text()
        nueva_sentencia = self.entry_sentencia.get_text()
        
        
        data = open_file()
        data1 = open_file_life()
        
        for i in range(len(data)):
            if(self.rut == data[i]['rut']):
                it = i
                data[it]['descripcion'] = nueva_descripcion
                data[it]['sentencia'] = nueva_sentencia
                save_file(data)
        
        for i in range(len(data1)):
            x = data1[i].keys()
            if(self.rut == (list(x)[0])):
                data1[i][str(self.rut)].append(nueva_descripcion)
                save_file_life(data1)
        d = VentanaExito()
        
        self.editar.destroy()
        
        
    def cancelar_edicion(self, event):
        self.editar.destroy()

class VentanaHojaVida():
    
    def __init__(self, rut):
        
        self.rut = rut
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

            
        self.dialogo_hoja_vida = self.builder.get_object("DialogoHojaVida")
        self.dialogo_hoja_vida.set_default_size(600, 400)
        self.dialogo_hoja_vida.set_title("Hoja de Vida")
    
        self.resultado_hoja_vida = self.builder.get_object("ResultadoHojaVida")
        
        data1 = open_file_life()
        
        for i in range(len(data1)):
            x = data1[i].keys()
            if(self.rut == (list(x)[0])):
                k = i
                for k in range(len(data1[i][str(self.rut)])):
                    texto = data1[i][str(self.rut)][k]
                    
                    texto_label = self.resultado_hoja_vida.get_text()
                    
                    texto_label += '\n' + texto

                    self.resultado_hoja_vida.set_text(texto_label)
        
        self.dialogo_hoja_vida.show_all()

class VentanaPermiso():
    
    def __init__(self):
        
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")
        
        self.ventana_permiso = self.builder.get_object("VentanaPermiso")
        self.ventana_permiso.set_title("Usted no tiene permiso para ingresar a esta opción")
        
        self.botonOKA = self.builder.get_object("BotonOKA")
        self.botonOKA.connect("clicked", self.cerrar)
        
        self.ventana_permiso.show_all()
        
    def cerrar(self, event):
        self.ventana_permiso.destroy()

class VentanaExito():
    
    def __init__(self):
        
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")
        
        self.ventana_exito = self.builder.get_object("VentanaExito")
                
        self.botonOKA1 = self.builder.get_object("BotonOKA1")
        self.botonOKA1.connect("clicked", self.cerrar)
        
        self.ventana_exito.show_all()
        
    def cerrar(self, event):
        self.ventana_exito.destroy()
    
if __name__ == '__main__':

    w = InicioSesion()
    Gtk.main()
