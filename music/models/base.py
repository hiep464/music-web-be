from django.db.models import Manager
from django.db import models


# We use custom query to filter which is declared by Manager in Django.
# We declared custom manager in ./backend/models/base.py
# source: https://docs.djangoproject.com/en/4.0/topics/db/managers/
class CustomManager(Manager):
    #  We create a custom filter by Manager. This custom_filter method will ommit all values that are None.
    def custom_filter(self, *args, **kwargs):
        updated_kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return super().filter(*args, **updated_kwargs)


class ModelBase(models.Model):
    class Meta:
        abstract = True

    # By default, Django adds a Manager with the name objects to every Django model class.
    # However, if you want to use objects as a field name, or if you want to use a name other than objects for the Manager, you can rename it on a per-model basis.
    # To rename the Manager for a given class, define a class attribute of type models.Manager() on that model.
    objects = CustomManager()

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=('created at'))
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)
