from rest_framework.serializers import ModelSerializer
from main.models import ToDo


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('title', 'memo', 'important', 'user')
        read_only_fields = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        return ToDo.objects.create(user=user, **validated_data)


class CurrentToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('title', 'memo')


class CompletedToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('title', 'created_at')


class UpdateToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('title', 'memo', 'important', 'completed')


class ToDoDetailSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('title', 'memo', 'important', 'completed')
