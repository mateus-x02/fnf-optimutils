# Isso aqui só serve pra quando tu substitui um spritesheet por um sprite 1x1.
# Essa ferramenta faz o xml não ficar "bugado". Assim, ele não vai procurar por tamanho/posição que não existe na imagem.
import re
import pathlib

inputmuitolegal = input('Nome do arquivo (nao precisa de extensao): ')
xml = inputmuitolegal + '.xml'

caminhoarquivo = pathlib.Path() / xml # fazer isso aqui via escrever pelo terminal

substituicao = 'x="0" y="0" width="1" height="1" frameX="0" frameY="0" frameWidth="1" frameHeight="1"/>'


with open(caminhoarquivo, 'r') as file:
    arquivo = file.read()
    
estruturaxml = re.compile(r'x="\d+" y="\d+" width="\d+" height="\d+" frameX="-?\d+" frameY="-?\d+" frameWidth="\d+" frameHeight="\d+"/>')

conteudomodificado = re.sub(estruturaxml, substituicao, arquivo)

with open(caminhoarquivo, 'w') as file:
    file.write(conteudomodificado)
