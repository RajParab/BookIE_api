from django.db import models

class Book(models.Model):
	genreChoices=(
			('Business','Business'),
			('Personal Finance','Personal Finance'),
			('Entrepreneurship','Entrepreneurship'),
			('Novel','Novel'),
			('Fiction','Fiction'),
			('Other','Other')
		)
	title=models.CharField(max_length=50)
	slug=models.SlugField(max_length=50,unique=True)
	author=models.CharField(max_length=50)
	rating=models.IntegerField()
	isbn=models.CharField(max_length=50)
	description=models.TextField()
	imageURL=models.ImageField(upload_to='book_cover')
	genre=models.CharField(max_length=50,choices=genreChoices)

	def __str__(self):
		return self.title

class Chapter(models.Model):
	bookName=models.ForeignKey('Book', on_delete=models.CASCADE)
	chapterNo=models.IntegerField()
	chapterTitle=models.CharField(max_length=50)
	chapterContent=models.TextField()

	def __str__(self):
		return str(self.bookName)+' : Chapter - '+str(self.chapterNo)