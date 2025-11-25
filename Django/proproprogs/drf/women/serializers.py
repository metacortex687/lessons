from rest_framework import serializers
from .models import Women
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'cat_id')

class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 255)
    content = serializers.CharField()
    time_created = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default = True)
    cat_id = serializers.IntegerField()


# def encode():
#     model = WomenModel('Angelina Joly', 'Content: Angelina Joly')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json, type(json), sep='\n')

# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Joly","content":"Content!: Angelina Joly"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)

    