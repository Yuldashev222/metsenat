from rest_framework import serializers


from . import models, enums


class SponsorSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = models.Sponsor
        exclude = ('spent_amount', )
    
    
    def create(self, validated_data):
        
        validated_data['type'] = enums.SponsorType.new.value
        return super().create(validated_data)
