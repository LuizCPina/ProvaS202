from database import Database


db = Database("bolt://3.89.90.44:7687", "neo4j", "apples-pad-surrenders")
db.drop_all()

#questão 1
print(db.execute_query("MATCH(t:Teacher{name: 'Renzo'}) RETURN t.ano_nasc, t.cpf"))

print(db.execute_query("MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS Name, t.cpf AS CPF"))

print(db.execute_query("MATCH (c:City) RETURN c.name"))

print(db.execute_query("MATCH (s:School) WHERE s.number>=150 and s.number<=550 RETURN s.name, s.number, s.addres"))

#questão 2
print(db.execute_query("MATCH (t:Teacher) Return MIN(t.ano_nasc),MAX(t.ano_nasc)"))

print(db.execute_query("MATCH (c:City) WITH c, SUM(c.population) AS somaPopulation RETURN AVG(somaPopulation)"))

print(db.execute_query("MATCH (c:City) WHERE c.cep = '37540-000' WITH c, c.name AS originalName WITH c, replace(originalName, 'a', 'A') AS upperA RETURN upperA)"))

print(db.execute_query("MATCH (t:Teacher) WITH t, LEFT(t.name, 4) AS carac RETURN RIGHT(carac,1)"))


db.close()