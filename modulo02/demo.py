# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FormBox
###########################################################################

class FormBox ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Demonstração", pos = wx.DefaultPosition, size = wx.Size( 500,158 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Nome:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		gSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.txtNome, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( gSizer2, 0, wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"E-mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.txtEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.txtEmail, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( gSizer3, 0, wx.EXPAND, 5 )

		gSizer4 = wx.GridSizer( 0, 4, 0, 0 )

		self.buttonNovo = wx.Button( self, wx.ID_ANY, u"Novo", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.buttonNovo, 0, wx.ALL, 5 )

		self.buttonSalvar = wx.Button( self, wx.ID_ANY, u"Salvar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.buttonSalvar, 0, wx.ALL, 5 )

		self.buttonExcluir = wx.Button( self, wx.ID_ANY, u"Excluir", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.buttonExcluir, 0, wx.ALL, 5 )

		self.buttonSair = wx.Button( self, wx.ID_ANY, u"Sair", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.buttonSair, 0, wx.ALL, 5 )


		bSizer1.Add( gSizer4, 0, wx.EXPAND, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


