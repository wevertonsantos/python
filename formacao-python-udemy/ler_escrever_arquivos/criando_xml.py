import xml.etree.ElementTree as xml #importando biblioteca xml.
import os

no_raiz = xml.Element("DadosPessoais") # criando um nó raiz com um elemento
no_pessoa = xml.Element("Pessoa",attrib={'nome':'Rodrigo'}) # criando elemento com atributo