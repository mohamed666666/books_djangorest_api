from .models import Books ,Pages

from rest_framework import serializers

class bookSerlizer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields='__all__'


class pageSerlizer(serializers.ModelSerializer):
    class Meta:
        model=Pages
        fields='__all__'