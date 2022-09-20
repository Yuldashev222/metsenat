from rest_framework import serializers

from django.contrib.auth.models import User
from . import models
from django.contrib.auth import password_validation, hashers
from django.core import exceptions



class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')
        
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    
    def validate(self, data):
        user = User(**data)
        
        errors = dict()     
        
    # password validations -----------------------------------------------
        password = data.get('password')
        if password:
            try:
                password_validation.validate_password(password=password, user=user)
            
            except exceptions.ValidationError as e:
                raise serializers.ValidationError({'password': list(e.messages)})
                
            
            data['password'] = hashers.make_password(data['password'])
    # --------------------------------------------------------------------

            
        return super(AdminSerializer, self).validate(data)
    



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