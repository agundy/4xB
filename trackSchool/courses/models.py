from django.db import models
from django.contrib.auth.models import User


class School(models.Model):
    name = models.CharField(max_length=256, blank=False)

    email_domain = models.CharField(max_length=256, blank=False)

    website = models.URLField(max_length=256)

    def __unicode__(self):
        """
        outputs name of School
        """
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=256)

    dept = models.CharField(max_length=6)

    courseID = models.CharField(max_length=16)

    school = models.ForeignKey(School)

    def __unicode__(self):
        """
        outputs name of course
        """
        return self.dept + " " + self.courseID + ": " + self.title


class Section(models.Model):
    term_choices = [('Winter', 'Winter'), ('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall')]

    year = models.IntegerField()

    term = models.CharField(max_length=10, choices=term_choices)

    course = models.ForeignKey(Course)

    professor = models.CharField(max_length=256)

    id_no = models.CharField(max_length=16)

    # content = document()

    # meeting times

    def __unicode__(self):
        """
        outputs course name, term and year
        """
        return str(self.id) + " " + str(self.course) + " " + self.term + ", " + str(self.year)


class Student(models.Model):
    user = models.OneToOneField(User)

    school = models.ForeignKey(School, null=True)

    edu_email = models.EmailField(null=True)

    confirmation_code = models.CharField(max_length=256, null=True)

    verified_edu_email = models.BooleanField(default=False)

    current_courses = models.ManyToManyField(Section, related_name='current_courses')

    past_courses = models.ManyToManyField(Section, related_name='past_courses')

    def __unicode__(self):
        """
        outputs name of student

        """
        return self.user.first_name + " " + self.user.last_name


class CourseItem(models.Model):
    name = models.CharField(max_length=256)

    courseInstance = models.ForeignKey(Section)

    due_date = models.DateTimeField()
    
    slug = models.SlugField(unique=True, null=True)
