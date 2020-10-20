from django.db import models

from ckeditor import fields

# Create your models here.
class Topic(models.Model):
    """ A topic or question the user wants to talk about. """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    body_text = fields.RichTextField()

    def __str__(self):
        """ Return a string representation of the model. """
        return self.text


class Entry(models.Model):
    """ An entry for a topic. """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = fields.RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """ Return a string representation of the model. """
        if len(self.text) > 50:
            return f'{self.text[:50]}...'

