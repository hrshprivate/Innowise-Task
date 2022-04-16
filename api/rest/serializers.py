from rest_framework import serializers

from .models import Comment, Ticket


class FilterForComments(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    children = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        list_serializer_class = FilterForComments
        model = Comment
        fields = ('id', 'content', 'user', 'children')


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tickets = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
        depth = 0


class TicketUpdateSerializer(serializers.ModelSerializer):
    tickets = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ['user']
        depth = 0


class AddCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'ticket', 'parent']
