

import wx
import wx.xrc


#classe que representa o frame principal
class FormBox ( wx.Frame ):

    #Construtor da classe FormBox, que representa a janela desenhada
    #A partir da classe FormBox, iremos construir um objeto, que representa a janela
    #Em Python, todos os métodos de uma classe obrigatoriamente começam com self, que guardada as devidas
    #proporções representa o this do Java
	def __init__( self, parent ): #Parent aqui diz respeito a janela pai. Caso seja uma janela única, passaremos o valor None
        #Chama o superconstrutor da classe wx.Frame passando a informação da janela pai, título, posição, tamanho e estilo
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Demonstração", pos = wx.DefaultPosition,
                            size = wx.Size( 500,158 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        #Define os tamanho em que a janela não deve diminuir
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        #Cria um sizer do tipo BoxSizer com orientação vertical, empilhando os componentes
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
        #Cria um Sizer do tipo Grid, com 2 colunas e quantidade de linhas automáticas. Informa também que não haverá espaçamento entre as células (0,0)
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
        #cria um staticText com o rótulo Nome
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Nome:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 ) #Libera para quebrar linha
        #Adiciona o texto estático no sizer, com proporção 0, com desenho das bordas com largura 5
		gSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )
        #Cria um TextCtrl, com conteúodo vazio e proporção 0
		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		 #Adiciona o ctrlText (input) no sizer, com proporção 0, com desenho das bordas com largura 5
		gSizer2.Add( self.txtNome, 0, wx.ALL|wx.EXPAND, 5 )

        #Adicionar o GridSizer ao BoxSizer, informando que pode expandir para ocupar o espaço disponível
		bSizer1.Add( gSizer2, 0, wx.EXPAND, 5 )
        #A partir daqui segue procedimento semelhante ao comentando anteriormente.
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


		self.SetSizer( bSizer1 ) #Define que o primeiro BoxSizer irá gerenciar o layout do Frame
		self.Layout() #Aplica o Layout defino

		self.Centre( wx.BOTH ) #Centraliza a tela

	def __del__( self ):
		pass


