#!/usr/bin/env python
# -*- coding: utf-8 -*-
import operator
import gi
import json
import matplotlib.pyplot as plt

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

def open_file_life(nombre_carcel):
    try:
        with open(str(nombre_carcel)+'prisionerosvida.json', 'r') as file:
            data1 = json.load(file)
    except IOError:
        data1 = []

    return data1

def save_file_life(data1, nombre_carcel):
    print("Save File")

    with open(str(nombre_carcel)+'prisionerosvida.json', 'w') as file:
        json.dump(data1, file, indent=4)

def open_file(nombre_carcel):
    try:
        with open(str(nombre_carcel)+'prisioneros.json', 'r') as file:
            data = json.load(file)
    except IOError:
        data = []

    return data

def save_file(data, nombre_carcel):
    print("Save File")

    with open(str(nombre_carcel)+'prisioneros.json', 'w') as file:
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
        with open('datoscarceles.json', 'r') as file:
            data3 = json.load(file)
    except IOError:
        data3 = []

    return data3

def save_file_carcel(data3):
    print("Save File")

    with open('datoscarceles.json', 'w') as file:
        json.dump(data3, file, indent=4)

def open_file_capacidad(nombrecarcel):
    try:
        with open(str(nombrecarcel)+'capacidad.json', 'r') as file:
            data4 = json.load(file)
    except IOError:
        data4 = []

    return data4

def save_file_capacidad(data4, nombrecarcel):
    print("Save File")

    with open(str(nombrecarcel)+'capacidad.json', 'w') as file:
        json.dump(data4, file, indent=4)

def obtener_valor_combobox(combo):
    try:
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            seleccion = model[tree_iter][0]

        return seleccion
    except UnboundLocalError:
        error = 'error'
        return error

def llenar_combo(combo, carceles):

    lista = Gtk.ListStore(str)

    for i in carceles:
        lista.append([i])

    combo.set_model(lista)
    renderer_text = Gtk.CellRendererText()
    combo.pack_start(renderer_text, True)
    combo.add_attribute(renderer_text, "text", 0)

def graficar(nombre_carcel):
    data4 = open_file_capacidad(nombre_carcel)[0]
    data2 = open_file(nombre_carcel)

    capacidad = len(data4)
    x = []

    for i in range(1, capacidad+1):
         x.append(i)

    for i in range(0, capacidad):
         x[i] = str(x[i])

    data3 = open_file_carcel()
    data_3 = []

    for i in range(0,len(data3)):
        if data3[i][0] == nombre_carcel:
            data_3.append(data3[i][2])

    presos = data_3[0]

    datos = []
    for i in range(0,capacidad):
        datos.append(i)

    for i in range(0,capacidad):
        nada = 0
        prisioneros = 0
        for j in range(0,len(data2)):
            if  data2[j]["celda"] == str(i+1) and data2[j]["estado"] == "Prisionero":
                nada = nada + 1
                prisioneros = prisioneros + 1
        datos[i] = prisioneros
        if nada != 0:
            datos[i] = prisioneros

    plt.bar(x, datos, color=(0,1,0), align='center')
    plt.ylabel("Numero de prisioneros")
    plt.xlabel("Numero de celda")
    plt.title('Grafica de '+ nombre_carcel)

    plt.show()


class InicioSesion():

    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file("iniciosesion.glade")

        self.window = self.builder.get_object("window")
        self.window.set_title("Inicio de Sesión")
        self.window.connect("destroy", Gtk.main_quit)

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


        self.window.show_all()


    def crear_cuenta(self, event):
        p = CrearCuenta()

    def revisar_cuenta(self, btn=None):
        usuario = self.usuario.get_text()
        contraseña = self.contraseña.get_text()

        flag = 0
        data2 = open_file_cuentas()
        for i in range(len(data2)):
            if usuario == data2[i]['usuario'] and contraseña == data2[i]['contraseña']:
                rango = data2[i]['rango']
                v = VentanaIngresarCarcel(rango)
                flag = 1
        if flag == 0:
            error = 'usr_pass_error'
            self.usuario.set_text("")
            self.contraseña.set_text("")
            p = VentanaPermiso(error)

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


        if len(usuario) <= 4 or len(contraseña) <= 4:
            self.v_crearcuenta.destroy()
            error = 'usr_no_valido'
            v = VentanaPermiso(error)
            v = CrearCuenta()


        else:
            rango = obtener_valor_combobox(combo)
            if rango == 'error':
                error = 'combobox_error'
                p = VentanaPermiso(error)
            else:
                data = open_file_cuentas()
                repetida = 0

                for i in range(len(data)):
                    if data[i]["usuario"] == usuario:
                        error = 'cuenta_repetida'
                        p = VentanaPermiso(error)
                        repetida = 1

                if repetida == 0:
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
        self.rango = rango
        self.error = ""
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

        self.ventana_carcel = self.builder.get_object("VentanaCarcel")
        self.ventana_carcel.set_title("Inicio de Carcel")

        self.crear_carcel = self.builder.get_object("CrearCarcel")
        self.crear_carcel.connect("clicked", self.formulariocarcel)

        self.combo_carceles = self.builder.get_object("ComboCarceles")

        self.okvcarcel = self.builder.get_object("OkVentanaCarcel")
        self.okvcarcel.connect("clicked", self.ok)

        self.ventana_carcel.show_all()

        carceles = []
        data3 = open_file_carcel()

        for i in range(len(data3)):
            nombrecarcel = data3[i][0]
            carceles.append(nombrecarcel)

        llenar_combo(self.combo_carceles, carceles)

    def formulariocarcel(self, event):
        if self.rango == 'Alcaide':
            self.ventana_carcel.destroy()
            p = FormularioCarcel(self.rango)
        else:
            self.error = "dato_repetido"
            p = VentanaPermiso(self.error)

    def ok(self, event):
        nombre_carcel = obtener_valor_combobox(self.combo_carceles)

        if nombre_carcel != 'error':
            p = VentanaMain(nombre_carcel, self.rango)
        elif nombre_carcel == 'error':
            error = 'seleccionar_carcel'
            p = VentanaPermiso(error)


class FormularioCarcel():
    def __init__(self, rango):
        self.rango = rango
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

        self.formulario_carcel = self.builder.get_object("FormularioCarcel")
        self.formulario_carcel.set_title("FormularioCarcel")

        self.nombre_carcel = self.builder.get_object("EntryNombreCarcel")
        self.nombre_carcel.connect("changed", self.revisar_dato)
        self.numero_celda = self.builder.get_object("SpinNumeroCelda")
        self.capacidad_celda = self.builder.get_object("SpinCapacidadCelda")
        self.aceptar_formulario = self.builder.get_object("OkFormularioCarcel")
        self.aceptar_formulario.connect("clicked", self.datos_carcel)
        self.cancelar_formulario = self.builder.get_object("CancelarFormularioCarcel")
        self.cancelar_formulario.connect("clicked", self.cancelar_vformulario)

        self.formulario_carcel.show_all()

    def datos_carcel(self, event):
        rango = self.rango
        nombrecarcel = self.nombre_carcel.get_text()
        numerocelda = self.numero_celda.get_value_as_int()
        capacidadcelda = self.capacidad_celda.get_value_as_int()

        datos = [nombrecarcel, numerocelda, capacidadcelda]

        data3 = open_file_carcel()
        data3.append(datos)
        save_file_carcel(data3)

        dic = {}

        for i in range(numerocelda):
            dic[str(i+1)] = capacidadcelda

        data4 = open_file_capacidad(nombrecarcel)
        data4.append(dic)
        save_file_capacidad(data4, nombrecarcel)


        self.formulario_carcel.destroy()

        p = VentanaIngresarCarcel(rango)

    def cancelar_vformulario(self, event):
        rango = self.rango
        self.formulario_carcel.destroy()
        p = VentanaIngresarCarcel(rango)


    def revisar_dato(self, event):
        self.error = 'dato_repetido'
        nombrecarcel = self.nombre_carcel.get_text()
        data3 = open_file_carcel()

        for i in range(len(data3)):
            if data3[i][0] == nombrecarcel:
                p = VentanaPermiso(self.error)
                self.nombre_carcel.set_text("")

class VentanaMain():

    def __init__(self, nombre_carcel, rango):
        self.error = 'permiso_denegado'
        self.rango = rango
        self.nombre_carcel = nombre_carcel

        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

        window2 = self.builder.get_object("window2")
        window2.set_default_size(600, 400)
        window2.set_title("Menú")

        #BOTON AGREGAR
        self.boton_agregar = self.builder.get_object("Agregar")
        self.boton_agregar.connect("clicked", self.dialogo_add)

        #BOTON VER TODO
        self.boton_buscar_todo = self.builder.get_object("VerTodo")
        self.boton_buscar_todo.connect("clicked", self.dialogo_ver_todo)

        #BOTON BUSCAR
        self.boton_buscar = self.builder.get_object("BotonBuscar")
        self.boton_buscar.connect("clicked", self.dialogo_buscar)

        self.boton_grafico = self.builder.get_object("BotonGrafico")
        self.boton_grafico.connect("clicked", self.grafico)

        window2.show_all()

    def dialogo_add(self, btn=None):

        if (self.rango != 'Guardia'):
            d = VentanaAdd(self.nombre_carcel)
        elif(self.rango == 'Guardia'):
            d = VentanaPermiso(self.error)

    def dialogo_ver_todo(self, btn=None):
        d = VentanaVerTodo(self.nombre_carcel)

    def dialogo_buscar(self, btn=None):
        self.rut_buscar = self.builder.get_object("Buscar")
        rut = self.rut_buscar.get_text()
        d = VentanaBuscar(rut, self.rango, self.nombre_carcel)

    def grafico(self, btn=None):
        nombre_carcel = self.nombre_carcel
        d = graficar(nombre_carcel)


class VentanaAdd():

    def __init__(self, nombre_carcel):
        self.nombre_carcel = nombre_carcel
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

        self.dialogo_prisionero = self.builder.get_object("DialogoPrisionero")
        self.dialogo_prisionero.set_title("Información de Prisionero")

        self.nombre = self.builder.get_object("Nombre")
        self.apellido = self.builder.get_object("Apellido")
        self.rut = self.builder.get_object("Rut")
        self.nacionalidad = self.builder.get_object("Nacionalidad")
        self.combo_celda = self.builder.get_object("ComboCelda")
        self.sentencia = self.builder.get_object("Sentencia")
        self.combo_estado = self.builder.get_object("ComboEstado")
        self.descripcion = self.builder.get_object("Descripción")

        self.botonOK = self.builder.get_object("OK")
        self.botonOK.connect("clicked", self.guardar_información)
        self.botonCANCELAR = self.builder.get_object("CANCEL")
        self.botonCANCELAR.connect("clicked", self.cancelar_dialogo)

        self.dialogo_prisionero.show_all()

        #DE ESTA MANERA SOLO SE LLENA EL COMBOBOX CON
        #LAS CELDAS QUE TIENE CAPACIDAD
        data4 = open_file_capacidad(self.nombre_carcel)
        celdas = []
        for i in range(len(data4[0])):
            if data4[0][str(i+1)] != 0:
                celdas.append(str(i+1))
        llenar_combo(self.combo_celda, celdas)


    def guardar_información(self, btn=None):

        nombre = self.nombre.get_text()
        apellido = self.apellido.get_text()
        rut = self.rut.get_text()
        nacionalidad = self.nacionalidad.get_text()
        celda = obtener_valor_combobox(self.combo_celda)
        sentencia = self.sentencia.get_text()
        estado = obtener_valor_combobox(self.combo_estado)
        descripcion = self.descripcion.get_text()

        if celda == "error" or estado == "error":
            error = 'faltan_datos'
            p = VentanaPermiso(error)

        else:
            largo = len(rut)

            exito = 0


            if largo >= 11:
                if rut[largo-2] == '-' and rut[largo-6] == '.' and rut[largo-10] == '.':
                    exito = 1
                else:
                    exito = 0

            elif largo < 11:
                exito = 0

            data_rut = open_file(self.nombre_carcel)

            repetido = 1

            error = 'rut_repetido'
            for i in range(len(data_rut)):
                if data_rut[i]["rut"] == rut:
                    p = VentanaPermiso(error)
                    self.rut.set_text('')
                    repetido = 0

            if exito == 1 and repetido == 1:
                #DISMINUIR CAPACIDAD DE LA CELDA ELIJIDA

                data4 = open_file_capacidad(self.nombre_carcel)
                celda_selec = data4[0][str(celda)]
                celda_selec = celda_selec - 1
                data4[0][str(celda)] = celda_selec
                save_file_capacidad(data4, self.nombre_carcel)

                #SE CREA UN JSON CON LA HOJA DE VIDA DE UN PRISIONERO
                data1 = open_file_life(self.nombre_carcel)
                data1.append({str(rut):[]})

                for i in range(len(data1)):
                    x = data1[i].keys()
                    if(rut == (list(x)[0])):
                        data1[i][str(rut)].append(descripcion)

                save_file_life(data1, self.nombre_carcel)


                dic = {"nombre": nombre,
                        "apellido": apellido,
                        "rut": rut,
                        "nacionalidad": nacionalidad,
                        "celda": celda,
                        "sentencia": sentencia,
                        "estado": estado,
                        "descripcion": descripcion}

                data = open_file(self.nombre_carcel)
                data.append(dic)
                save_file(data, self.nombre_carcel)

                self.dialogo_prisionero.destroy()

            elif exito == 0:
                error = 'rut_no_valido'
                d = VentanaPermiso(error)

    def cancelar_dialogo(self, btn=None):
        self.dialogo_prisionero.destroy()

class VentanaVerTodo():

    def __init__(self, nombre_carcel):
        self.nombre_carcel = nombre_carcel
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

        self.lista_prisionero = self.builder.get_object("ListaPrisionero")
        self.lista_prisionero.set_default_size(600, 400)
        self.lista_prisionero.set_title("Lista de Prisionero")

        self.listmodel = Gtk.ListStore(str, str, str, str, str, str, str, str)
        self.treeResultado = self.builder.get_object("TreeResultado")
        self.treeResultado.set_model(model=self.listmodel)
        cell = Gtk.CellRendererText()


        title = ("Nombre", "Apellido", "Rut", "Nacionalidad", "Celda", "Sentencia", "Estado", "Descripcion")

        for i in range(len(title)):
            col = Gtk.TreeViewColumn(title[i], cell, text=i)
            self.treeResultado.append_column(col)

        self.mostrar_data()

        self.lista_prisionero.show_all()

    def mostrar_data(self):

        data = open_file(self.nombre_carcel)

        for i in data:
            x = [x for x in i.values()]
            print(x)
            self.listmodel.append(x)

class VentanaBuscar():

    def __init__(self, rut, rango, nombre_carcel):
        self.error = "permiso_denegado"
        self.nombre_carcel = nombre_carcel
        self.rango = rango
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


        title = ("Nombre", "Apellido", "Rut", "Nacionalidad", "Celda", "Sentencia", "Estado", "Descripcion")

        for i in range(len(title)):
            col = Gtk.TreeViewColumn(title[i], cell, text=i)
            self.treeResultado1.append_column(col)

        self.mostrar_data()

        self.lista_prisionero1.show_all()

    def mostrar_data(self):

        data = open_file(self.nombre_carcel)

        for i in range(len(data)):
            if(self.rut == data[i]['rut']):
                busqueda = data[i].values()
                self.listmodel.append(busqueda)

        self.lista_prisionero1.show_all()

    def liberar_prisionero(self, event):

        if(self.rango == 'Alcaide'):
            data = open_file(self.nombre_carcel)
            for i in range(len(data)):
                if(self.rut == data[i]['rut']):
                    it = i
                    data[it]['estado'] = 'Liberado'
                    save_file(data, self.nombre_carcel)
                    self.lista_prisionero1.destroy()
                    d = VentanaBuscar(self.rut, self.rango, self.nombre_carcel)

        elif(self.rango != 'Alcaide'):
            d = VentanaPermiso(self.error)
    def dialogo_hojavida(self, event):

        d = VentanaHojaVida(self.rut, self.nombre_carcel)

    def encerrar_prisionero(self, event):

        if(self.rango == 'Alcaide'):
            data = open_file(self.nombre_carcel)
            for i in range(len(data)):
                if(self.rut == data[i]['rut']):
                    it = i
                    data[it]['estado'] = 'Prisionero'
                    save_file(data, self.nombre_carcel)
                    self.lista_prisionero1.destroy()
                    d = VentanaBuscar(self.rut, self.rango, self.nombre_carcel)

        elif(self.rango != 'Alcaide'):
            d = VentanaPermiso(self.error)

    def editar_descripcion(self, event):
        if(self.rango != 'Guardia'):
            self.lista_prisionero1.destroy()
            d = VentanaEdicionDescripcion(self.rut, self.nombre_carcel)
            d = VentanaBuscar(self.rut, self.rango, self.nombre_carcel)

        elif(self.rango == 'Guardia'):
            d = VentanaPermiso(self.error)


class VentanaEdicionDescripcion():

    def __init__(self, rut, nombre_carcel):
        self.nombre_carcel = nombre_carcel
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


        data = open_file(self.nombre_carcel)
        data1 = open_file_life(self.nombre_carcel)

        for i in range(len(data)):
            if(self.rut == data[i]['rut']):
                it = i
                data[it]['descripcion'] = nueva_descripcion
                data[it]['sentencia'] = nueva_sentencia
                save_file(data, self.nombre_carcel)

        for i in range(len(data1)):
            x = data1[i].keys()
            if(self.rut == (list(x)[0])):
                data1[i][str(self.rut)].append(nueva_descripcion)
                save_file_life(data1, self.nombre_carcel)
        self.editar.destroy()


    def cancelar_edicion(self, event):
        self.editar.destroy()

class VentanaHojaVida():

    def __init__(self, rut, nombre_carcel):
        self.nombre_carcel = nombre_carcel
        self.rut = rut
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")


        self.dialogo_hoja_vida = self.builder.get_object("DialogoHojaVida")
        self.dialogo_hoja_vida.set_default_size(600, 400)
        self.dialogo_hoja_vida.set_title("Hoja de Vida")

        self.resultado_hoja_vida = self.builder.get_object("ResultadoHojaVida")

        data1 = open_file_life(self.nombre_carcel)

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
    def __init__(self, error):
        self.error = error
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")

        self.ventana_permiso = self.builder.get_object("VentanaPermiso")

        self.label_dialogo = self.builder.get_object("LabelDialogo")
        self.botonOKA = self.builder.get_object("BotonOKA")
        self.botonOKA.connect("clicked", self.cerrar)

        if self.error == 'dato_repetido':
            self.label_dialogo.set_text("Este dato esta repetido, ingresar otro")
        elif self.error == 'permiso_denegado':
            self.label_dialogo.set_text("Permiso denegado")
        elif self.error == 'dato_no_valido':
            self.label_dialogo.set_text("Dato no valido")
        elif self.error == 'rut_no_valido':
            self.label_dialogo.set_text("Rut no valido")
        elif self.error == 'rut_repetido':
            self.label_dialogo.set_text("Rut repetido")
        elif self.error == 'usr_no_valido':
            self.label_dialogo.set_text("Usuario/Contraseña incorrectos, minimo 5 digitos")
        elif self.error == 'combobox_error':
            self.label_dialogo.set_text("Por favor elija un rango")
        elif self.error == 'usr_pass_error':
            self.label_dialogo.set_text("Usuario/Contraseña incorrecta")
        elif self.error == 'cuenta_repetida':
            self.label_dialogo.set_text("Usuario ya existente")
        elif self.error == 'faltan_datos':
            self.label_dialogo.set_text("Faltan datos por especificar")
        elif self.error == 'seleccionar_carcel':
            self.label_dialogo.set_text("Seleccione una carcel por favor")
        self.ventana_permiso.show_all()

    def cerrar(self, event):
        self.ventana_permiso.destroy()



if __name__ == '__main__':

    w = InicioSesion()
    Gtk.main()
