from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Stocks(BaseModel):
    stock_name = models.CharField(max_length=200)
    stock_url = models.URLField(max_length=200)