from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.meilisearch import client
from core.models import Person

@receiver(post_save, sender=Person)
def update_maile_index(sender, instance, **kwargs):
    try:
        client.index('persons').add_documents([{
            'id':instance.id,
            'name':instance.name,
            'address':instance.address
        }])
    except Exception as e:
        print(f'there is error {e}') 


@receiver(post_delete, sender=Person)
def delete_maile_index(sender, instance, **kwargs):
    try:
        client.index('persons').delete_document(instance.id)
    except Exception as e:
        print(f'there is error {e}') 