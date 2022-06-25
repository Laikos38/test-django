from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import QuerySet

from djangoresttest.api.models.item_models import Item
from djangoresttest.api.utils.exceptions.not_found_exception import NotFoundException


class ItemPolitics:
    @staticmethod
    def get_queryset(user_id: int) -> QuerySet[Item]:
        return Item.objects.filter(owner_id=user_id)

    @staticmethod
    def get_or_raise_not_found(id: int, owner_id: int) -> Item:
        try:
            object = Item.objects.get(id=id, owner_id=owner_id)
        except ObjectDoesNotExist:
            raise NotFoundException(msg="Item was not found.")
        return object
