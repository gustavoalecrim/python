#-*- encoding: utf8 -*-

##
# Esse programa é livre, você pode distribuir e/ou modifica-lo sob os
# termos da licença geral publica GNU publicada pela fundação de software
# livre (Free Software Foundation),  contida na segunda versão da licença
# ou (em sua opinião) outra versão mais recente.
# Esse programa é distribuído na esperança de ser útil e satisfatório,
# mas DESTITUÍDO DE QUALQUER GARANTIA, destituído igualmente da
# COMPATIBILIDADE DE MÁQUINA ou CONVENIÊNCIA PARA PROPÓSITOS
# PARTICULARES. Veja a licença geral publica GNU para opter mais detalhes.
# http://www.gnu.org/copyleft/gpl.html
##

###############################################################################
## Nome do Arquivo: minhabarra
## Autor: Guedes, Maurilio<billguedes>
## Data da Criação: 26/07/2005
## Data da Modificação: 27/07/2005
## Finalidade: Mostrar uma barra de progresso
##
##
##
###############################################################################

import pygtk
pygtk.require('2.0')
import gtk, gobject

class BarraProgresso:
        '''Classe principal'''

        def __init__(self):
                '''Incialização padrão'''
                
                self.texto= "";
                self.registro= 1;
                self.total_registro= 500;
                
        def desenhar(self):
                '''Desenha os widgets'''
                
                # Cria uma janela comum
#               self.janela = gtk.Window()
#               self.janela = gtk.Window(gtk.WINDOW_TOPLEVEL)
                self.janela = gtk.Window(gtk.WINDOW_POPUP)
                self.janela.set_resizable(False)
                self.janela.connect("destroy", self.fechar_janela)
                self.janela.set_title("Barra de Progresso")
                self.janela.set_border_width(0)
                self.janela.set_position(gtk.WIN_POS_CENTER)

                # Cria uma caixa vertical
                vbox = gtk.VBox(False, 5)
                vbox.set_border_width(10)
                self.janela.add(vbox)

                # Cria uma barra de progresso
                self.barra_progresso = gtk.ProgressBar()
                vbox.pack_start(self.barra_progresso, False, False, 0)
                
                # Chamar o método desenhar_progresso a da 5 milisegundos
                self.tempo = gobject.timeout_add(5, self.desenhar_progresso, self.barra_progresso)

                # Cria uma separador
                separador = gtk.HSeparator()
                vbox.pack_start(separador, False, False, 0)

                # Cria uma etiqueta
                self.etiqueta= gtk.Label()
                self.etiqueta.set_label(self.texto)
                vbox.pack_start(self.etiqueta, False, False, 0)
                
                # Mostra todas os widgets adicionados na janela
                self.janela.show_all()
                
        def escrever_texto(self, widget= None):
                '''Escreve o texto na etiqueta'''
                
                self.etiqueta.set_label(self.texto)
                
        def desenhar_progresso(self, widget= None):
                '''Desenha ou atualiza a barra de progressso'''
                
                self.escrever_texto()
                
                # Calculo flacionário para adequação da barra de progresso
                valor= (float(self.registro) / self.total_registro)
                
                 # Caso seja 1 ou maior (100%) feche a tela
                if valor >= 1: self.fechar_janela()
                        
                # Valor válido 0.0 à 1.0
                self.barra_progresso.set_fraction(valor) 
                
                 # Exibe a porcentagem
                self.barra_progresso.set_text("%.2f%%" % (valor * 100))
                return True
                
        def fechar_janela(self, widget= None):
                '''Fecha o aplicativo'''
                
                # Remove a função relativa ao tempo (Timer)
                gobject.source_remove(self.tempo)
                 gtk.main_quit()