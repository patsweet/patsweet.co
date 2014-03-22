from django.db import models
from django.core.urlresolvers import reverse


class FamilyMember(models.Model):
    SEX_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    SUFFIX_CHOICES = (
        ('JR', 'Jr.'),
        ('SR', 'Sr.'),
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
    )
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    suffix = models.CharField(max_length=5, choices=SUFFIX_CHOICES, blank=True, null=True)
    maiden_name = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    birthday = models.DateField(blank=True, null=True)
    died_on = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    mother = models.ForeignKey('self', blank=True, null=True, related_name='mother_to', limit_choices_to={'sex': 'f'})
    father = models.ForeignKey('self', blank=True, null=True, related_name='father_to', limit_choices_to={'sex': 'm'})

    class Meta:
        ordering = ['birthday', 'died_on']

    def __unicode__(self):
        return self.full_name()

    def full_name(self):
        if self.middle_name:
            name = "%s %s %s" % (self.first_name, self.middle_name, self.last_name)
        else:
            name = "%s %s" % (self.first_name, self.last_name)
        if self.suffix:
            return name + " " + self.get_suffix_display()
        return name

    def get_absolute_url(self):
        return reverse('family-detail', kwargs={'pk':self.id})

