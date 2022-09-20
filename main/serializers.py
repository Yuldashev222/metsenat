from rest_framework import serializers


from . import models


class AgreementSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = models.Agreement
        fields = "__all__"
        
        
    def create(self, validated_data):
        
        return super().create(validated_data)
    
      
    
    def validate(self, data):
        agreement = models.Agreement(**data)
        
        errors = dict()
        
        amount = data.get('amount')
        student = data.get('student')
        sponsor = data.get('sponsor')
        
        
        if student.allocated_amount == student.univer.contract_amount:
            errors['student'] = 'bu studentga yetarli pul tikilgan'
        
        elif not amount:
            errors['amount'] = 'pulni korsating'
            

        elif sponsor not in student.sponsors.all():
            errors['sponsor'] = 'bu sponsor: << {} >>, student: << {} >> sponsorlari ro\'yxatida yo\'q'.format(sponsor.full_name, student.full_name)
        
        
        elif amount > sponsor.payment_amount:
            
            if not sponsor.payment_amount:
                errors['sponsor'] = 'bu sponsorni puli qomagan'
            else:
                errors['amount'] = 'bu << {} >> tolov miqdori sponsor pulidan << {} >> ga ko\'p'.format(amount, amount - sponsor.payment_amount)
        
        
        
        if errors:
            raise serializers.ValidationError(errors)
        
        student.allocated_amount = amount
        student.save()
        sponsor.payment_amount = sponsor.payment_amount - amount
        sponsor.save()
        
        
        return super(AgreementSerializer, self).validate(data)