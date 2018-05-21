from py2neo import Node, Relationship, Graph, authenticate
from py2neo.ogm import GraphObject, Label, Property, RelatedFrom, RelatedTo
# from py2neo import Database


# basic Node, Relationship constructor
a = Node("Freelancer", 
        name="dono", 
        email="dono@gmail.com",
        noTelp="081081081081"
        )
print(a)

b = Node("Freelancer", 
        name="kasino", 
        email="kasino@gmail.com",
        noTelp="081081081081"
        )
print(b)

c = Node("Freelancer", 
        name="indro",
        email="indro@gmail.com",
        noTelp="081081081081"
        )
print(c)

ab = Relationship(a,"Knows", b)

# print(ab)

# construct relationship with class
class StudyWith(Relationship): pass

ac = StudyWith(a, c)
# print(ac.type())

# Subgraph
s = ab | ac
print(s)
# print(s.nodes())
# print(s.relationships())


w = ab + Relationship(b, "in debt with", c) + ac 
print(w)

print("                 ")
print("-----------------")
print("                 ")
print("-----------------")



# database connection
# graph_db = Graph()
authenticate("localhost:7474", "neo4j", "titiran7")
graph_db = Graph("bolt://localhost:7687")
print(graph_db)

# structure
class Role(GraphObject):
        __primarykey__ = "role_name"

        role_name = Property()

        freelance = RelatedFrom('Freelancer','worked_in')        

class Freelancer(GraphObject):

        __primarykey__ = "name"

        name = Property()
        email= Property()
        notelp= Property()

        role = RelatedTo(Role, 'work_as')
