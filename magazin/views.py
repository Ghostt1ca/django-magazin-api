from rest_framework import generics, permissions
from .models import Produs
from .serializers import ProdusSerializer

class ProdusListCreate(generics.ListCreateAPIView):
    serializer_class = ProdusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Produs.objects.all()
        
        stoc_mic = self.request.query_params.get('stoc_mic')
        
        if stoc_mic == '1':
            queryset = queryset.filter(cantitate__lt=5)
            
        return queryset
    
class ProdusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produs.objects.all()
    serializer_class = ProdusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]