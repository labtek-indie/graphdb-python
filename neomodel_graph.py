from neomodel import (config, StructuredNode, StringProperty, IntegerProperty, 
                    UniqueIdProperty, RelationshipTo, RelationshipFrom)

config.DATABASE_URL = 'bolt://neo4j:titiran7@localhost:7687'

# Cypher shortcut to delete database
# MATCH (n:Role) MATCH (r:Freelancer) DETACH DELETE r,n

# upload model to database
# neomodel_install_labels neomodel_graph.py --db bolt://neo4j:titiran7@localhost:7687
# remove model in database
# neomodel_remove_labels --db bolt://neo4j:titiran7@localhost:7687

# to use class in this file
# from neomodel_graph import Freelancer, Role
# from from neomodel import (config, StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo, RelationshipFrom)

class Freelancer(StructuredNode):
    name = StringProperty ()
    email = StringProperty ()
    notelp = StringProperty ()

    role = RelationshipTo('Role', 'WORKING_AS')
    perf = RelationshipTo('Performance', 'PERFORMANCE')

class Role(StructuredNode):
    name = StringProperty() 

class Avaibility(StructuredNode):
    domisili = StringProperty()

    

dono = Freelancer(name='dono', email='dono@gmail.com', notelp='081').save()
kasino = Freelancer(name='kasino', email='kasinp@gmail.com', notelp='082').save()
indro = Freelancer(name="indro", email="indro@gmail.com",notelp='083').save()



backend = Role(name='backend').save()
frontend = Role(name='frontend').save()
gamedev = Role(name='gamedev').save()

dono.role.connect(backend)
dono.role.connect(frontend)
kasino.role.connect(frontend)
kasino.role.connect(gamedev)
indro.role.connect(gamedev)
indro.role.connect(frontend)

