from rest_framework import serializers


from . import models
from main.models import Agreement


class StudentSerializer(serializers.ModelSerializer):
    
    # univer = serializers.CharField(source='univer.name')
    
    class Meta:
        model = models.Student
        fields = "__all__"
        
    
    def update(self, instance, validated_data):
        
        new_sponsors = validated_data.get('sponsors')
        agreement_sponsors_id = list(map(lambda tpl: tpl[0], Agreement.objects.filter(student_id=instance.id).values_list('sponsor_id')))



        if new_sponsors:
            if len(new_sponsors) > len(instance.sponsors.all()) and instance.allocated_amount == instance.univer.contract_amount:
                raise serializers.ValidationError({'sponsors': f'Bu talabaga yetarlicha pul yigilgan sponsor qoshib utirmang'})

            for sponsor in instance.sponsors.all():
                if sponsor not in new_sponsors and sponsor.id in agreement_sponsors_id:
                    raise serializers.ValidationError({'sponsors': f'siz sponsor: << {sponsor.full_name} >> ni' 
                                                       ' o\'zgartira olmaysiz chunki'
                                                       ' student va bu sponsor tomonidan shartnoma tuzilgan'})
        
        
        
        
        return super().update(instance, validated_data)
        




class UniverSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = models.Univer
        fields = "__all__"