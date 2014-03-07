from django.db import models


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
    mother = models.ForeignKey('self', blank=True, null=True, related_name='mother_to', limit_choices_to={'sex': 'f'})
    father = models.ForeignKey('self', blank=True, null=True, related_name='father_to', limit_choices_to={'sex': 'm'})

    def __unicode__(self):
        if self.suffix:
            return "%s %s %s" % (self.first_name, self.last_name, self.get_suffix_display())
        else:
            return "%s %s" % (self.first_name, self.last_name)
