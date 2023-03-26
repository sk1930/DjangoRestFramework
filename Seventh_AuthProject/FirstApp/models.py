from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 
# we are using user provided by Django

# Create your models here.

class Genre(models.Model):

    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name 


class Language(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name 




class Book(models.Model):

    title = models.CharField(max_length=200)
    ''' a book can have multipe authors but here we are considering only one author.'''
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    # models.ForeignKey()
    # Book has a foreign key for author 
    # an author can write multiple books so its better to have author as a separate table.
    # on_delete=models.SET_NULL  this means that  if author is deleted, this field is set to null in Book.
    # whenever on delete is set to set_null, null = True should be there

    summary = models.TextField(max_length=600)
    isbn = models.CharField('ISBN',max_length=13,unique=True)
    '''models.CharField() verbose_name: str | None = ..., name: str | None = ...,
     primary_key: bool = ..., max_length: int = ..., db_collation: 
    '''

    ''' a book can have many genres'''
    genre = models.ManyToManyField(Genre)
    # a book is in a single language 
    language = models.ForeignKey('Language',on_delete=models.SET_NULL,null=True)
    # MORE TO COME

    def __str__(self):
        return self.title 
    
        # it returns a url to access a particular book details
        # on creation of a book if success_url is not defined in the views.py,
        #  it calls get_absolute_url for the success_url redirect.
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True,blank=True)

    class Meta:
        # this is to dictate  the behaviour in the admin view
        ordering = ['last_name','first_name']
        # while  doing add book in the admin view the dropdown for author showed the names of author 
        # as lastname, firstname

    # it returns a url to access a particular author details
    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.last_name} , {self.first_name}"


import uuid
# unique identifier generator
class BookInstance(models.Model):


    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    # as primary_key= True is set here the DB doesnt generate another id as primary key
    # like in case genre  for example primary keys are 1,2,3... http://127.0.0.1:8080/admin/FirstApp/genre/3/change/
    # but here it is like 4ceca917-7109-44bb-9bc3-45ddf12d8083  http://127.0.0.1:8080/admin/FirstApp/bookinstance/4ceca917-7109-44bb-9bc3-45ddf12d8083/change/
    book = models.ForeignKey("Book",on_delete=models.RESTRICT,null=True) # whether it is "Book" or
    # Book without quotes it is not making any difference. i tried creating a book instance in both cases it worked fine.
    # models.restrict --- restricts from deleting Book if there is a book instance

    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True,blank=True)
    borrower = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    ''' but here use User withour quotes,  if u use "User" we are getting errors FirstApp.BookInstance.borrower: (fields.E300) Field defines a relation with model 'models.User', which is either not installed, or is abstract.
FirstApp.BookInstance.borrower: (fields.E307) The field FirstApp.BookInstance.borrower was declared with a lazy reference to 'models.user', but app 'models' isn't installed.


the reason might be User is from a different package'''

    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On Loan'),
        ('a','Available'),
        ('r','Reserved')
    )

    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m') 
    # default is displayed in the dropdown and as blank=True we can just select the blank value from the dropdown

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        # self.book.title --- referring to title form the bookusing the foreign key book
        return f'{self.id} ({self.book.title})'
