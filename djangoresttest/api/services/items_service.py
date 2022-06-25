from django.db.models.query import QuerySet
from django.utils import timezone

from djangoresttest.api.models.item_models import Item
from djangoresttest.api.politics.item_politics import ItemPolitics
from djangoresttest.api.schemas.item_schemas import ItemInSchema


def get_all_user_items(user_id: int) -> QuerySet[Item]:
    return Item.objects.filter(owner_id=user_id)


def register_item(item_data: ItemInSchema, owner_id: int) -> int:
    return Item.objects.create(name=item_data.name, description=item_data.description, owner_id=owner_id).id


def get_item_by_id(item_id: int, owner_id: int) -> Item:
    return ItemPolitics.get_or_raise_not_found(item_id, owner_id)


def delete_item(item_id: int, owner_id: int) -> bool:
    item = ItemPolitics.get_or_raise_not_found(item_id, owner_id)
    item.deletion_datetime = timezone.now()
    item.save()
    return True
