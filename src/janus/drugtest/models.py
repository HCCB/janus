from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]


def mkfld_name(**kargs):
    kargs.setdefault('max_length', 60)
    kargs.setdefault('blank', False)
    kargs.setdefault('default', '')
    return models.CharField(**kargs)


class Person(models.Model):
    given_name = mkfld_name()
    family_name = mkfld_name()
    middle_name = mkfld_name(blank=True)

    def _get_mi(self):
        return u"%c." % self.middle_name[0] if self.middle_name.strip() else ""

    @property
    def fullname(self):
        namestr = "%s, %s %s" % (
            self.family_name.strip(),
            self.given_name.strip(),
            self._get_mi(),
        )
        return namestr.strip()

    def __unicode__(self):
        return u"%s" % self.fullname

    class Meta:
        ordering = ('family_name', 'given_name', 'middle_name', )
        abstract = True


class Patient(Person):
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


class Physician(Person):
    def __unicode__(self):
        return "Dr. %s" % self.family_name


class Staff(Person):
    designation = models.CharField(max_length=60)
    suffix = models.CharField(max_length=20)
    username = models.OneToOneField(User)

    def _get_suffix(self):
        return u", %s" % self.suffix if self.suffix.strip() else u""

    def __unicode__(self):
        return "%s %s %s %s" % (
            self.given_name,
            self._get_mi(),
            self.family_name,
            self._get_suffix())
