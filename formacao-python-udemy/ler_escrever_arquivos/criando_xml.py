import xml.etree.ElementTree as xml #importando biblioteca xml.
import os

no_raiz = xml.Element("DadosPessoais") # criando um nó raiz com um elemento
no_pessoa = xml.Element("Pessoa",attrib={'Nome':'Rodrigo'}) # criando elemento com atributo
no_cpf = xml.SubElement(no_pessoa,'CPF') # criando sub elemento de um elemento
no_cpf.text = '123456789'

no_raiz.append(no_pessoa) # passando nó pessoa para o nó raiz

arvore = xml.ElementTree(no_raiz) # transformando nó raiz em um xml com elementTree