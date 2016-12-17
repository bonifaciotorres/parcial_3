#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import call,Popen,PIPE
import wx,os

# wx.TextCtrl()
# wx.StaticText()

class MiAplicacion(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent=parent,title=title,size=(600,800))
        sz = wx.BoxSizer(wx.VERTICAL)
        
        # Controles
        self.static_text = wx.StaticText(self, 0, "Ingrese URL: ",pos=(100,200))
        self.static_textololo = wx.StaticText(self, 0, "Formato a descargar: ",pos=(100,270))
        self.static_texto = wx.StaticText(self, 0, "Descargar video simple: ",pos=(100,350))
        self.static_texto1 = wx.StaticText(self, 0, "Extra: descarga en formato mp3 ",pos=(100,420))
        
        self.input_text = wx.TextCtrl(self,value="", pos=(100, 50), size=(400,400))
        boton = wx.Button(self, label="Descargar", pos=(260,380))
        self.cb1 = wx.CheckBox(self, label = 'mp4 (720x1280)',pos = (240,290)) 
        self.cb2 = wx.CheckBox(self, label = 'webm (720x1280)',pos = (240,310)) 
        self.cb3 = wx.CheckBox(self, label = 'mp4 (360x640)',pos = (240,330)) 
        self.cb4 = wx.CheckBox(self, label = 'MP3',pos = (240,460))
        
        # Creamos el submenú Archivo
        menuArchivo = wx.Menu() 
        menuActualizar = menuArchivo.Append(0, "&Actualizar"," Actualizar Programa")
        menuArchivo.AppendSeparator()
        menuAcercaDe = menuArchivo.Append(wx.ID_ABOUT, "A&cerca de"," Información del programa")
        menuAyuda = menuArchivo.Append(wx.ID_HELP,"&Ayuda"," Como utilizar la aplicación")
         
        # Creamos la barra del menú
        menuBar = wx.MenuBar()
        menuBar.Append(menuArchivo,"&Archivo") 
             
        self.SetMenuBar(menuBar) 
        
        # Modificando fuente
        font1 = self.input_text.GetFont()
        font1.SetPointSize(16)
        self.input_text.SetFont(font1)
        self.static_text.SetFont(font1)
        self.static_textololo.SetFont(font1)
        self.static_texto.SetFont(font1)
        self.static_texto1.SetFont(font1)
        
        # Modificando color de fondo
        self.static_text.SetBackgroundColour("#FFFFAA")
        self.static_textololo.SetBackgroundColour("#FFFFAA")
        self.static_texto.SetBackgroundColour("#FFFFAA")
        self.static_texto1.SetBackgroundColour("#FFFFAA")
        
        # Modificando el color de fuente
        self.static_text.SetForegroundColour("#FF0000")
        self.static_textololo.SetForegroundColour("#FF0000")
        self.static_texto.SetForegroundColour("#FF0000")
        self.static_texto1.SetForegroundColour("#FF0000")       
       
        
        # Eventos
        self.Bind(wx.EVT_MENU, self.OnUpdate, menuActualizar)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAcercaDe)
        self.Bind(wx.EVT_MENU, self.Onhelp, menuAyuda)
        self.Bind(wx.EVT_BUTTON, self.onClick)
        
        self.Bind(wx.EVT_CHECKBOX, self.onChecked_1, self.cb1)
        
        self.Bind(wx.EVT_CHECKBOX, self.onChecked_2, self.cb2)
        
        self.Bind(wx.EVT_CHECKBOX, self.onChecked_3, self.cb3)
        
        self.Bind(wx.EVT_CHECKBOX, self.onChecked_4, self.cb4)
        
        self.Centre()
        self.Show(True)
        
    def onChecked_1(self,event):
		txt = self.input_text.GetValue()
		descargass=["youtube-dl","-f","22",txt]
		call(descargass)
		
    def onChecked_2(self,event):
		txt = self.input_text.GetValue()
		descargass=["youtube-dl","-f","45",txt]
		call(descargass)

    def onChecked_3(self,event):
		txt = self.input_text.GetValue()
		descargass=["youtube-dl","-f","18",txt]
		call(descargass)
		
    def onChecked_4(self,event):
		txt = self.input_text.GetValue()
		descargass=["youtube-dl","--extract-audio","--audio-format","mp3",txt]
		call(descargass)
    
    def onClick(self,event):
		txt = self.input_text.GetValue()
		#self.static_text.SetLabelText(txt)
		descargass=["youtube-dl",txt]
		call(descargass)
	
    def OnAbout(self,e):
		# Creamos una ventana de diálogo con un botón de ok. wx.OK es una ID estàndard de wxWidgets.
        d = wx.MessageDialog( self, "aplicacion desde la cual se pueden descargar videos de youtube", "", wx.OK)
        d.ShowModal() # La mostramos
        d.Destroy() # Finalmente la destruimos
 
    def Onhelp(self,e):
		dka = wx.MessageDialog( self, "copie y pege el enlace de youtube y seleecione la opcion que quiera utilizar","",wx.OK)
		dka.ShowModal() 
		dka.Destroy()
         
    def OnUpdate(self,e):
		actualizar = Popen(["youtube-dl","-U"], stdout = PIPE)
		mostrar = actualizar.stdout.read()
		dlg = wx.MessageDialog(self, mostrar, "Actualizar software")
		dlg.ShowModal()
		dlg.Destroy()
	
	
		
if __name__=='__main__':
	app = wx.App()
	frame = MiAplicacion(None,u"youtube-dl")
	app.MainLoop()
