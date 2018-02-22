import MySQLdb

#fazendo conexão com o banco de dados
conexao = MySQLdb.connect(host='127.0.0.1', user='admin', passwd='Mudar@123', db='mercado')

cur = conexao.cursor()
'''
#adicionar um novo item no banco
cur.execute("insert into produtos(nome, quantidade, valor_unit) values('arroz', '57', '14,00')")

conexao.commit()

print ('produto inserido com sucesso!')


cur.execute("select * from produtos")

#retorna o primeiro objeto
print (cur.fetchone())

#retorna todos
#print (cur.fetchall())

#acessar apenas um indice 
#print (cur.fetchall()[1])
print (cur.fetchall()[1][1])
'''
#caso voce digite alguma string que não esta no banco (se tiver algum erro retorna como "none")
try:
    cur.execute("select *from produto")
    print (cur.fetchone())
    print (cur.fetchall())
except Exception as e:
    conexao.rollback()
    print ('Ocorreu um erro ao executar o comando')

