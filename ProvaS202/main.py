from database import Database
from teacher_crud import TeacherCRUD

#conexao com db
db = Database('bolt://3.89.90.44:7687', 'neo4j', 'apples-pad-surrenders')
db.drop_all()


teacher_db = TeacherCRUD(db)

#criando, pesquisando e atualizado novo prof
teacher_db.create("Chris Lima", 1956, "189.052.396-66")

print(teacher_db.read("Chris Lima"))

teacher_db.update("Chris Lima", "162.052.777-77")


#menu de CLI
print("Bem vindo ao banco de dados")

var = 0;

while(var != 5):
  #flag de escolha para menu
  var = input("O que deseja fazer:"
            "1 - Criar um professor"
            "2-  Atualizar um cpf de professor"
            "3 - Deletar um professor"
            "4 - Resgatar dados de um professor"
            "5 - Sair")


  if(var == 1):
    aux_nome = input("Nome:")
    aux_data = input("Ano de nascimento:")
    aux_cpf = input("CPF:")
    teacher_db.create(aux_nome,aux_data,aux_cpf)

  if(var == 2):
    aux_nome = input("Nome:")
    aux_cpf = input("CPF:")
    teacher_db.update(aux_nome,aux_cpf)

  if(var == 3):
    aux_nome = input("Nome:")
    teacher_db.delete(aux_nome)

  if(var == 4):
    aux_nome = input("Nome:")
    print(teacher_db.read(aux_nome))




db.close()