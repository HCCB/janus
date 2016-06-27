from __future__ import unicode_literals

from django.db import models


GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]


class Person(models.Model):
    given_name = models.CharField(max_length=60)
    family_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60, blank=True, default='')
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    @property
    def fullname(self):
        namestr = "%s, %s" % (
            self.family_name.strip(),
            self.given_name.strip())
        if self.middle_name and self.middle_name.strip():
            namestr = namestr + " " + self.middle_name.strip()
        return namestr

    def __unicode__(self):
        return u"%s" % self.fullname

    class Meta:
        ordering = ('family_name', 'given_name', 'middle_name', )
