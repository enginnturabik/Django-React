from django.db import models
from authentication.models import User

class MRIData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='mri_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    anonymous_file_path = models.CharField(max_length=255, blank=True, null=True)

