from rest_framework import viewsets
from .serializers import LanguageSerializer
from .models import Language


class LanguageViewSet(viewsets.ModelViewSet):
    '''
    Este viewset fornece automaticamente ações em 'list' e 'detail'.
    '''
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
