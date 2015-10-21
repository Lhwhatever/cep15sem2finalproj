import base64
import hashlib
from django.db import models


def get_hash(obj):
    b = obj.to_bytes(2, byteorder='big')
    m = hashlib.sha256()
    m.update(b)
    x = m.digest(b)
    return base64.b64encode(x).decode('utf-8')


"""
# Create your models here.
class ObfuscatedPkModel(models.Model):
    numeric_id = models.AutoField()
    primary_key = models.BinaryField(primary_key=True)

    def __init__(self, *args, **kwargs):
        super(ObfuscatedPkModel, self).__init__(*args, **kwargs)
        self.primary_key = get_hash(self.numeric_id)
"""
