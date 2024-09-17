#instalar package
#pip install mysql-connector-python

#importar package
import mysql.connector
from faker import Faker

fake = Faker(locale='pt_BR')

# criar conn

conn = mysql.connector.connect(
    host="10.211.55.15",
    user="root",
    password="12345678",
    database="IEFP_py"
)

# cirar curr
cur = conn.cursor(dictionary=True)

#cirar tabelas

cur.execute("""
create table if not exists aula_py (
    id Int auto_increment, 
    nome varchar(255),
    idade INT,
    primary key (id)
);


""")

conn.commit()

#inserir dados


cur.execute("""
insert into aula (nome, idade) values ('Goncalo_py', 30)
""")
#commit
conn.commit()

#for i in range(25):
#    cur.execute( f"""
#    insert  into ContactoV2(nome, morada, teledone, email) value (
#    "{fake.name()}",
#    "{fake.address()}",
#    "{fake.phone_number()}",
#    "{fake.email()}")
#    """)

#    conn.commit()

#ler dados

print("--------------myData = cur.fetchall()------------")
cur.execute("select * from ContactoV2")

myData = cur.fetchall()
print(myData)

print("-------------myData = cur.fetchone()-------------")
cur.execute("select * from ContactoV2")

myData = cur.fetchone()
print(myData)

myData = cur.fetchone()
print(myData)

print("-------------myData = cur.fetchmany()-------------")

myData = cur.fetchmany(5)
print(myData)


"""
[(3, 'Filipe Andrade', 'Travessa de Neves, 61\n7323-125 Vila Real de Santo António', '(351) 262 427 540', 'henriquesluana@example.org'), 
(4, 'Diogo da Macedo', 'Av Martim Garcia, 35\n7402-651 Gafanha da Nazaré', '(351) 291 949 907', 'nunesmario@example.org'), 
(5, 'Maria Moura', 'Avenida Henriques, 38\n1375-802 Oliveira de Azeméis', '(351) 969 543 250', 'assuncaobrian@example.net'),
(6, 'Benjamim Martins', 'Alameda Neves, 96\n8360-448 Santarém', '+351967416083', 'figueiredokevim@example.org'),
(7, 'Joel Torres', 'Rua da Rua Duque de Palmela, 88\n2288-857 Santana', '+351969354527', 'dominguesmiriam@example.net')]

"""
"""
{'id': 1, 
'nome': 'Wilson Mendes', 
'morada': 'Praça de Pires, 20\n8102-527 Beja', 
'teledone': '+351921948824', 
'email': 'lcarvalho@example.net'
}

"""
print("---------for ct in myData:---------")

for ct in myData:
    print(ct["nome"])


# fechar ligaçao


conn.close()


"""

conta1 
iban - 123
saldo - 1000


conta2
iban - 321
saldo - 0


retirar 500 conta1 
adicionar 500 conta2


---------- 
retirar 500 conta1 
servir cai


---------- 
saldo total = conta2 + conta1

retirar 500 conta1 
adicionar 500 conta2

verificar saldo total = conta2 + conta1





---------- 
saldo total = conta2 + conta1

retirar 500 conta1 
servir cai


---------- 

transação 

    retirar 500 conta1 
    adicionar 500 conta2
    commit (tudo e executado)

---------- 

transação 

    retirar 500 conta1 
    servir cai




"""






