from django.forms import model_to_dict
from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from base.models    import Todo

class TodoSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='todo-detail',
        lookup_field='pk',
    )   
    class Meta:
        model = Todo
        fields = [
            'pk',
            'user',
            'title',
            'description',
            'completed',
            'url',
        ]
        read_only_fields = ['pk','user']