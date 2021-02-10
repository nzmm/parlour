from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import FieldFile


class TWJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, FieldFile):
            return obj.url if obj else ""
        # let the base class default method raise the TypeError
        return super(TWJSONEncoder, self).default(obj)