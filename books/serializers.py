from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Book


class BookSerialzer(serializers.ModelSerializer):
    class Meta:
        fields = ['title', 'author', 'updated', 'timestamp', 'content','published']
        model = Book