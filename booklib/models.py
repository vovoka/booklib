from django.db import models
import uuid # Required for unique book instances
# Create your models here.



class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        return unicode(self.name, 'utf-8')
        """

class Author(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=255)
    # books = models.ManyToManyField(Book)
  
    def __str__(self):
        """
        String for representing the Model object.
        """
        return unicode(self.name, 'utf-8')


class Book(models.Model):
    """
    Model representing a book (but not a specific instance of a book).
    """
    title = models.CharField(max_length=255)
    author = models.ManyToManyField('Author')
    # Many to Many used because a book can have several authors.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    
    # def get_absolute_url(self):
    #     """
    #     Returns the url to access a particular book instance.
    #     """
    #     return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be offered by user).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('n', 'New'),
        ('r', 'Read'),
        ('u', 'Used'),
        ('p', 'Poor'),
    )

    condition = models.CharField(max_length=1, choices=LOAN_STATUS, blank=False, default='r', help_text='Book condition')
       

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id,self.book.title)