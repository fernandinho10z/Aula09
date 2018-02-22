Banco.py

import psycopg2

class Banco():
    def __init__(self):
        self.conexao = psycopg2.connect('host=127.0.0.1 dbname=entregas user=adm password=Mudar@123')      
        self.cur = self.conexao.cursor()

    def cadastrar entrega(self):
        nome = input('Digite o nome: ')
        endereco = input('Digite o endereco: ')
        produto = input('Digite o produto: ')
        self.cur.execute ("insert into entregas(nome, endereco, produto) values ('%s', '%s', '%s')" %(nome, endereco, produto))
    
    
    def alterar entrega(self):
        id_entrega = int(input('Digite o Id da entrega: ')
        endereco = input('Digite o novo endereco: ')
        self.cur.execute ("update entregas set endereco='%s' where id=%s" %(endereco, id_entrega)

    def bus car_entrega(self):
        self.cur.execute("select * from entregas")
        resultado = self.cur.fetchall()
        for item in resultado:
            print ('ID: ', item[0])
            print ('NOME: ',item[1])
            print ('ENDERECO :', item[2])
            print ('PRODUTO: ', item[3])
            
