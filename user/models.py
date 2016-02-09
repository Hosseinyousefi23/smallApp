from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', )

# ------------------------------------------------------------------------

class Portfolio(models.Model):
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)


class SuperInstitution(models.Model):
    name = models.CharField(max_length=100)
    is_formal = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    # class Meta:
    #     abstract = True


class Role(models.Model):
    portfolio = models.ForeignKey(Portfolio, null=True, blank=True)
    super_institution = models.ForeignKey(SuperInstitution, null=True, blank=True)

    def __str__(self):
        return 'salam'


class RoleType(models.Model):
    role = models.ForeignKey(Role, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# ---------------------------------------------------------------- #


class Permission(models.Model):
    name = models.CharField(max_length=100)
    role = models.ForeignKey(Role, null=True)

    def __str__(self):
        self.name


# ---------------------------------------------------------------- #

class University(SuperInstitution):
    # superInstitution = models.ForeignKey(SuperInstitution, null=True, blank=True)

    def __str__(self):
        return self.name


class Group(SuperInstitution):
    # university = models.ForeignKey(University, null=True, related_name="%(app_label)s_%(class)s_related")
    is_department_group = models.BooleanField(default=False)

    def __str__(self):
        return self.superInstitution.name

# ---------------------------------------------------------------- #


class Department(SuperInstitution):
    related_university = models.ForeignKey(University, null=True, blank=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    # to extend django User class
    user = models.OneToOneField(User)

    followers = models.ManyToManyField('self', related_name='followers', blank=True)
    following = models.ManyToManyField('self', related_name='following', blank=True)
    national_id = models.CharField(max_length=100, null=True, blank=True)
    sharif_mail_address = models.EmailField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image', null=True, blank=True)
    super_institution = models.ManyToManyField(SuperInstitution, blank=True)
    interested_tags = models.ManyToManyField(Tag, blank=True)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Studentity(models.Model):
    person = models.ForeignKey(Person, null=True, blank=True)
    department = models.ForeignKey(Department, null=True, blank=True)
    student_id = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    field_of_study = models.CharField(max_length=100)

    def __str__(self):
        return self.person.user.username + ' ' + self.student_id

    def is_graduated(self):
        if self.end_date == timezone.now:
            return True

# ---------------------------------------------------------------- #


