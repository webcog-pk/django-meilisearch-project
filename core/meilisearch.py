import meilisearch
from core.models import Person

client = meilisearch.Client('http://localhost:7700')

def index_person_content():
    persons = Person.objects.all()
    documents = []

    for person in persons:
        documents.append({
            'id':person.id,
            'name':person.name,
            'address':person.address
        })
    
    client.index('persons').add_documents(documents)
    print("Done!")
