import xml.etree.ElementTree as xml #importando biblioteca xml.
import os

def cria_tag_pessoa(nome,cpf):
    no_pessoa = xml.Element("Pessoa",attrib={'Nome':nome}) # criando elemento com atributo

    no_cpf = xml.SubElement(no_pessoa,'CPF') # criando sub elemento de um elemento
    no_cpf.text = cpf

    return no_pessoa

raiz = xml.Element("DadosPessoais") # criando um nó raiz com um elemento
pessoa1 = cria_tag_pessoa('Rodrigo','12345678')
raiz.append(pessoa1) # passando nó pessoa para o nó raiz

arvore = xml.ElementTree(raiz) # transformando nó raiz em um xml com elementTree

with open('dados_exemplo.xml','wb') as file: #abrindo arquivo xml como escrita
    arvore.write(file) #escrevendo xml pela arvore