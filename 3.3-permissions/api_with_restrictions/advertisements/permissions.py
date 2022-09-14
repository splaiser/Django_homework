from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        elif request.method in ['DELETE', 'POST', 'PATCH']:
            return request.user == obj.creator

    def perform_create(self, serializer):
        if self.request.authenticators:
            serializer.save(creator=self.request.user)
        else:
            return False
