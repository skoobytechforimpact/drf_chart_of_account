"""Chart of Accounts Models Serializers Classes."""
from rest_framework import serializers
from .models import LayersBaseModel, LayerOneModel


class LayersModelBaseSerializer(serializers.ModelSerializer):
    """The base serializer class for all the layers model.

    All other serializer class with extend this base model.
    """

    class Meta:
        """Meta data class for the base serializer."""

        model = LayersBaseModel
        fields = '__all__'
        read_only_fields = ['id', 'ref_no', 'created_at', 'updated_at']


class LayerOneModelSerializer(LayersModelBaseSerializer):
    """LayerOneModel class serializer."""

    class Meta(LayersModelBaseSerializer.Meta):
        """Meta data class for the LayerOneModelSerializer."""

        model = LayerOneModel
