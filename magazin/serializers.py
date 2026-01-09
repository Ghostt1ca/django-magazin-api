from rest_framework import serializers
from .models import Produs, Categorie

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'nume']

class ProdusSerializer(serializers.ModelSerializer):
    status_stoc = serializers.SerializerMethodField()
    categorie = CategorieSerializer(read_only=True)
    categorie_id = serializers.PrimaryKeyRelatedField(
        queryset=Categorie.objects.all(), source='categorie', write_only=True
    )

    class Meta:
        model = Produs
        fields = ['id', 'nume', 'pret', 'cantitate', 'categorie', 'categorie_id', 'status_stoc']

    def get_status_stoc(self, obj):
        if obj.cantitate == 0:
            return "Indisponibil"
        elif obj.cantitate < 5:
            return "Stoc Critic"
        return "In Stoc"