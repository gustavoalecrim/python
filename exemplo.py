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
## Nome do Arquivo: teste.py
## Autor: Guedes, Maurilio<billguedes>
## Data da Criação: 26/07/2005
## Data da Modificação: 27/07/2005
## Finalidade: Testar o uso do arquivo minhabarra.py
##
##
##
###############################################################################

import pygtk
pygtk.require('2.0')
import gtk
import minhabarra

class Principal:
        '''Classe principal'''
        
        def __init__(self):
                '''Incialização padrão'''
                
                # Cria uma janela
                janela= gtk.Window()
                janela.connect("destroy", gtk.main_quit)
                
                # Cria um botão
                botao= gtk.Button("Executar")
                botao.connect("clicked", self.executar)
                janela.add(botao)
                
                # Mostra todas os widgets adicionados na janela
                janela.show_all()
                
        def executar(self, widget= None):
                '''Executa o código abaixo'''
                
                # Carrega a classe 'BarraProgresso'
                barra= minhabarra.BarraProgresso()
                barra.texto= "Começando o Processo..."
                
                # Muda a variável registro da classe 'BarraProgresso'
                barra.registro= 0
                
                # Muda a variável total_registro da classe 'BarraProgresso'
                barra.total_registro= 15000
                
                # Desenha os widgets da classe 'BarraProgresso'
                barra.desenhar()

                # Loop ilustrativo, mas poderia ser uma lista de clientes
                for i in range(barra.total_registro):
                        
                        # Depuração do código
                        print "Estou no for imprimindo %s\n" % i
                        
                        # Mostra mais informação ao usuário
                        barra.texto= "Estou Processando o Cliente '%05d'" % barra.registro
                        
                        # Muda novamente a variavel registro, ou melhor, acrescenta +1 na variável
                        barra.registro+= 1
                        
                        # Pausa o processo e espera a execução do "Timer"
                        gtk.mainiteration()
                        
# Chama a classe 'Principal'                    
p= Principal()

# Inicia o aplicativo
gtk.main()