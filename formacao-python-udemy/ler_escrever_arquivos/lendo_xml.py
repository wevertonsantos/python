import xml.etree.ElementTree as xml
tree = xml.parse("dados_pessoais3.xml") # construindo estrutura de árvore com arquivo xml
root = tree.getroot() #metodo que acessa a raiz do arquivo