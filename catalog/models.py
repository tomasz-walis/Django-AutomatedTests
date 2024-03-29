from django.db import models
from django.urls import reverse
import uuid
from datetime import date
from django.contrib.auth.models import User


# book genre
class Genre(models.Model):

    name = models.CharField(max_length=200, help_text="Enter a book genre.")
    
    def __str__(self):
        return self.name


# book language
class Language(models.Model):

    name = models.CharField(max_length=200, help_text="Enter Language")
    
    def __str__(self):
        return self.name


# model representing a book
class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have many books
    summary = models.TextField(max_length=1000, help_text="Enter book description")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Characters')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    # ManyToManyField used because a genre can contain many books and a Book can have many genres.
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
      
    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
        display_genre.short_description = 'Genre'

    # return ur to the book
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    # model object
    def __str__(self):
        return self.title


# book instance/copy of the book
class BookInstance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this book")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set book as returned"),)   

    # model object string
    def __str__(self):
        return '{0} ({1})'.format(self.id, self.book.title)


# Author model
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    # return url to the author
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    # model object
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.last_name, self.first_name)
