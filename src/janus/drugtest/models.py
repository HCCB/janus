from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from tinymce.models import HTMLField

RESULT_TYPE_CHOICE = (
    (1, 'Numeric'),
    (2, 'Text'),
)

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

    @property
    def age(self):
        """ compute patient's current age """
        today = datetime.today()
        born = self.birthdate
        return today.year - born.year - \
            ((today.month, today.day) < (born.month, born.day))


class Physician(Person):
    def __unicode__(self):
        return u"Dr. %s" % self.family_name


class Staff(Person):
    designation = models.CharField(max_length=60)
    suffix = models.CharField(max_length=20)

    def _get_suffix(self):
        return u", %s" % self.suffix if self.suffix.strip() else u""

    def __unicode__(self):
        return "%s %s %s %s" % (
            self.given_name,
            self._get_mi(),
            self.family_name,
            self._get_suffix())


class TestCategory(models.Model):
    name = models.CharField(max_length=60)
    alternate_name = models.CharField(max_length=60, blank=True, default='')

    def __unicode__(self):
        if self.alternate_name:
            return u"%s (%s)" % (self.name, self.alternate_name)
        else:
            return u"%s" % self.name

    class Meta:
        verbose_name = "Test Category"
        verbose_name_plural = "Test Categories"


class TestProfile(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u"%s" % self.name


class Analysis(models.Model):
    category = models.ForeignKey(TestCategory)
    name = models.CharField(max_length=60)
    short_name = models.CharField(max_length=30, blank=True, default='')
    result_type = models.SmallIntegerField(choices=RESULT_TYPE_CHOICE)
    reference_text = HTMLField(blank=True, default='')

    profiles = models.ManyToManyField(to=TestProfile, blank=True)

    def __unicode__(self):
        if self.short_name:
            return u"%s" % self.short_name
        else:
            return u"%s" % self.name

    class Meta:
        verbose_name_plural = "Analyses"
        ordering = ('name', )


class ResultMaster(models.Model):
    patient = models.ForeignKey(Patient)
    case_number = models.CharField(max_length=30)
    room_number = models.CharField(max_length=20)
    date = models.DateField(default=datetime.now)
    category = models.ForeignKey(TestCategory)

    def __unicode__(self):
        return u"%s #: %s - %s" % (
            self.patient.fullname,
            self.case_number,
            self.category)


class ResultDetail(models.Model):
    master = models.ForeignKey(ResultMaster)
    analysis = models.ForeignKey(Analysis)
    result = HTMLField()

    def __unicode__(self):
        return u"%s: %s" % (
            self.analysis,
            self.result,
        )
