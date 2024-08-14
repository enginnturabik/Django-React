from django.db import models
from authentication.models import User
from mri_data.models import MRIData

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mri_data = models.OneToOneField(MRIData, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=255)
    analysis_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
