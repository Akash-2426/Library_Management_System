from rest_framework import serializers
from .models import Add_a_book,Delete_a_book,Get_all_book,Update_an_entry_of_a_book

class Get_all_bookSerializer(serializers.Serializer):
    bname=serializers.CharField(max_length=50)
    bcode=serializers.IntegerField()
    add_date=serializers.DateField()


    def create(self,validated_data):
        return Get_all_book.objects.create(**validated_data)

class Update_an_entry_of_a_bookSerializer(serializers.Serializer):
    bname = serializers.CharField(max_length=50, name=False)
    bcode = serializers.IntegerField(default=0)
    issuedate = serializers.DateField()

    def create(self, validated_data):
        return Update_an_entry_of_a_book.objects.create(**validated_data)

class Delete_a_bookSerializer(serializers.Serializer):
    bname = serializers.CharField(max_length=50, name=False)
    bcode = serializers.IntegerField(default=0)

    def create(self, validated_data):
        return Delete_a_bookSerializer.objects.create(**validated_data)

class Add_a_bookSerializer(serializers.Serializer):
    bname = serializers.CharField(max_length=50, name=False)
    bcode = serializers.IntegerField(default=0)
