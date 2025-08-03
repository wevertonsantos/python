'''
- Crie um arquivo XML, nesse
arquivo XML haverá a tag raiz Root.
Dentro dessa raiz podem haver varias
tags Estado com atributo nome.
Dentro de cada estado pode haver a
tag Cidade mas nesse caso o valor da
tag (texto) devera ser o nome da
cidade. Crie um programa que gere
esse arquivo com alguns estados e
municípios.
'''

import xml.etree.ElementTree as xml
import os

def cria_estado(nome, cidades):
  element_estado = xml.Element("Estado", attrib={'nome' : nome})
  for cidade in cidades:
    elemento_cidade = xml.SubElement(element_estado,'Cidade')
    elemento_cidade.text = cidade
  return element_estado

raiz = xml.Element("Root")
no_estado = cria_estado('Rio Grande do Sul',['Santa Maria','Porto Alegre','Novo Hamburgo'])
no_estado2 = cria_estado('São Paulo',['Sorocaba','Campinas'])
raiz.append(no_estado)
raiz.append(no_estado2)

arvore = xml.ElementTree(raiz)

with open('exercicio9.xml','wb') as files:
  arvore.write(files)
