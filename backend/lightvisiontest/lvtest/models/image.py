import os
import uuid
from django.db import models
from lvtest.common.base_model import BaseModel


class Image(BaseModel):
    image = models.ImageField(upload_to='images/')
    text_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    source = models.TextField()
    filetype = models.CharField(max_length=10)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            print(self.image.path)
            os.remove(self.image.path)

        super(Image, self).delete(*args, **kwargs)