"""Subclass of FormOperacoes, which is generated by wxFormBuilder."""

import wx
from modulo02.operacoesbook import operacoes

# Implementing FormOperacoes
class ProjetoOperacoesFormOperacoes( operacoes.FormOperacoes ):
	def __init__( self, parent ):
		operacoes.FormOperacoes.__init__( self, parent )

	# Handlers for FormOperacoes events.
	def realizarOperacao( self, event ):
		#Captura a opção do Combobox
		a=int(self.txtNumeroA.GetValue())
		b=int(self.txtNumeroB.GetValue())
		resultado=0
		if (self.cboOperacoes.GetValue()=='+'):
			resultado=a+b
		elif(self.cboOperacoes.GetValue()=='-'):
			resultado=a-b
		elif(self.cboOperacoes.GetValue()=='*'):
			resultado=a*b
		elif(self.cboOperacoes.GetValue()=='/'):
			resultado=a/b
		self.txtResultado.SetValue(str(resultado))
app=wx.App()
formOperacoes=ProjetoOperacoesFormOperacoes(None)
formOperacoes.Show(True)
app.MainLoop()

