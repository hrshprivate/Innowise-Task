from rest_framework import generics, permissions, status
from rest_framework.response import Response

from api.tasks import put_email

from .models import Comment, Ticket
from .permissions import IsOwnerOrReadOnly
from .serializers import (AddCommentSerializer, CommentSerializer,
                          TicketSerializer, TicketUpdateSerializer)


class TicketsApiView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TicketsApiUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if instance.user != request.user:
            put_email.delay(instance.user.email)
        return Response(serializer.data)


class CommentApiView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentApiUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class AddComment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = AddCommentSerializer
    permission_classes = [permissions.IsAuthenticated]



