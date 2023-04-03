from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    GET: Retrieve the current user's subscription
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.subscription
