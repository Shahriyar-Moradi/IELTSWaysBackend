from django.db import models

EXAM_CHOICES = (
    ("ACADEMIC", "Academic"),
    ("GENERAL", "General"),
)
TEST_CHOICES = (
    ("READING", "Reading"),
    ("LISTENING", "Listening"),
    ("SPEAKING", "Speaking"),
    ("WRITING", "Writing"),
)
class Test(models.Model):
    title=models.CharField(max_length=100)
    type=models.CharField(max_length=10,choices=TEST_CHOICES)
    
    def __str__(self):
        return f'{self.title}/{self.type}'
    
    
class Book(models.Model):
    title=models.CharField(max_length=100)
    test=models.ForeignKey(Test,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title}/{self.test}'
    

class IELTSExam(models.Model):
    type=models.CharField(max_length=10,choices=EXAM_CHOICES)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.book}/{self.type}'