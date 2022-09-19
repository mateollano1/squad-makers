from tortoise import fields
from tortoise.fields.base import SET_NULL
from tortoise.models import Model


class Joke(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField(
        "models.User",
        related_name="user_joke",
        on_delete=SET_NULL,
        null=True,
    )
    joke_text = fields.CharField(max_length=520, null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    last_modified = fields.DatetimeField(auto_now=True)
