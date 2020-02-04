from django.db import models


class Category(models.Model):
    # short alphanumeric code for the category
    code = models.CharField(max_length=10,)
    title = models.TextField()

    # keep track of date created
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    # keep track of updates
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('code',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{} - {}'.format(self.code, self.title[0:10])


class Diagnosis(models.Model):
    # category diagnosis falls under
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='diagnosis')

    # numerical code for the diagnosis
    # we could add checks to check the the code is unique to the diagnosis category
    code = models.IntegerField(null=True)

    # full alphanumeric code for the diagnosis
    full_code = models.CharField(max_length=10)

    # short description for the diagnosis
    abbreviated_description = models.TextField()

    # fully describe the diagnosis
    full_description = models.TextField()

    # compatible with the previous version
    backward_compatible = models.BooleanField(default=True)

    # keep track of date created
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    # keep track of updates
    updated = models.DateTimeField(auto_now=True)
