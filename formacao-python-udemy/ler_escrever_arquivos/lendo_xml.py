import xml.etree.ElementTree as xml
tree = xml.parse("dados_pessoais3.xml") # construindo estrutura de árvore com arquivo xml
root = tree.getroot() #metodo que acessa a raiz do arquivo
print(root.tag) # impressão pela raiz
for pessoa in root:
    print(' ',pessoa.tag,pessoa.attrib['Nome']) # imprimindo pessoa raiz, o nome da pessoa
    for dado in pessoa: # percorrendo tag pessoa
        print(' ', dado.tag,dado.text)