from py2neo import Node, Relationship, Graph, authenticate
from py2neo.ogm import GraphObject, Label, Property, RelatedFrom, RelatedTo

# database connection
# graph_db = Graph()
authenticate("localhost:7474", "neo4j", "titiran7")
graph_db = Graph("bolt://localhost:7687")
print(graph_db)

# structure
class Role(GraphObject):
        __primarykey__ = "name"

        name = Property()

        freelance = RelatedFrom("Freelancer","worked_in")        

class Freelancer(GraphObject):

        __primarykey__ = "name"

        name = Property()
        email= Property()
        notelp= Property()

        role = RelatedTo(Role,"worked_at")

backend = Role()
backend.name = "backend"
frontend = Role()
frontend.name= "frontend"

dono = Freelancer()
dono.name = "dono"
dono.email= "dono@gmail.com"
dono.notelp= "081"
dono.role=backend
dono.role=frontend

kasino = Freelancer()
kasino.name = "kasino"
kasino.email= "kasino@gmail.com"
kasino.notelp= "082"
kasino.role=backend
kasino.role=frontend

graph_db.create(backend)
graph_db.create(frontend)
graph_db.create(dono)
graph_db.create(kasino)