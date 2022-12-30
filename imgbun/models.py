from django.db import models
import uuid


class imgdb(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    img_format = models.CharField(max_length=3)
    text = models.TextField(max_length=500)
    color = models.IntegerField()
    background = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    imagebun_link = models.URLField(max_length=200, default="https//127.0.0.1:8000")

    def to_dict(self):
        return {
            "your_submit_id": self.id,
            "img_format": self.img_format,
            "text": self.text,
            "clor": self.color,
            "background": self.background,
            # "Status": self.status
        }
