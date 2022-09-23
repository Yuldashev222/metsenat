from rest_framework import serializers


from . import models, enums


class SponsorSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = models.Sponsor
        exclude = ('spent_amount', )
    
    
    def create(self, validated_data):
        
        validated_data['status'] = enums.SponsorStatus.new.value
<<<<<<< HEAD
        return super().create(validated_data)
=======
        return super().create(validated_data)
>>>>>>> refs/remotes/origin/main
