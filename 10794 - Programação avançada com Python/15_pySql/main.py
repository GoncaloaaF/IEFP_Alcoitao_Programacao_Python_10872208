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
cur = conn.cursor()

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
insert into aula (nome, idade) values ("Goncalo_py", 30)
""")
#commit
conn.commit()

for i in range(25):
    cur.execute( f"""
    insert  into ContactoV2(nome, morada, teledone, email) value (
    "{fake.name()}",
    "{fake.address()}", 
    "{fake.phone_number()}",
    "{fake.email()}")
    
    """)

    conn.commit()

#ler dados




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






