from rest_framework import serializers
from .models import IELTSExam,Book,Test


class ExamSerializer(serializers.ModelSerializer):

    exam_type = serializers.CharField(source='type')

    books=serializers.CharField(source='book')
    class Meta:
        model=IELTSExam
        fields = ['exam_type','books']
        # fields = '__all__' 

        
        
        
class BookSerializer(serializers.ModelSerializer):
    # category_name=serializers.CharField(source='name')
    class Meta:
        model=Book
        fields = '__all__' 
        
