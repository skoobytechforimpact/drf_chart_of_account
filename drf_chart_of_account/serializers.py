"""Chart of Accounts Models Serializers Classes."""
from rest_framework import serializers
from .models import (LayersBaseModel, LayerOneModel, LayerTwoModel,
                     LayerThreeModel, LayerFourModel, LayerFiveModel)


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

    def update(self, instance, validated_data):
        """Update the instance with custom update validation checking."""
        if instance.validate_update(related_object_name='layer_one_child'):
            return super(LayerOneModelSerializer, self).update(instance, validated_data)


class LayerTwoModelSerializer(LayersModelBaseSerializer):
    """LayerTwoModel class serializer."""

    class Meta(LayersModelBaseSerializer.Meta):
        """Meta data class for the LayerTwoModelSerializer."""

        model = LayerTwoModel

    def update(self, instance, validated_data):
        """Update the instance with custom update validation checking."""
        if instance.validate_update(related_object_name='layer_two_child'):
            return super(LayerTwoModelSerializer, self).update(instance, validated_data)


class LayerThreeModelSerializer(LayersModelBaseSerializer):
    """LayerThreeModel class serializer."""

    class Meta(LayersModelBaseSerializer.Meta):
        """Meta data class for the LayerThreeModelSerializer."""

        model = LayerThreeModel

    def update(self, instance, validated_data):
        """Update the instance with custom update validation checking."""
        if instance.validate_update(related_object_name='layer_three_child'):
            return super(LayerThreeModelSerializer, self).update(instance, validated_data)


class LayerFourModelSerializer(LayersModelBaseSerializer):
    """LayerFourModel class serializer."""

    class Meta(LayersModelBaseSerializer.Meta):
        """Meta data class for the LayerFourModelSerializer."""

        model = LayerFourModel

    def update(self, instance, validated_data):
        """Update the instance with custom update validation checking."""
        if instance.validate_update(related_object_name='layer_four_child'):
            return super(LayerFourModelSerializer, self).update(instance, validated_data)


class LayerFiveModelSerializer(LayersModelBaseSerializer):
    """LayerFiveModel class serializer."""

    class Meta(LayersModelBaseSerializer.Meta):
        """Meta data class for the LayerFiveModelSerializer."""

        model = LayerFiveModel

    def update(self, instance, validated_data):
        """Update the instance with custom update validation checking."""
        if instance.validate_update(related_object_name='layer_five_child'):
            return super(LayerFiveModelSerializer, self).update(instance, validated_data)
