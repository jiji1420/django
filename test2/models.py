from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)

class Category(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    created_ad = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)



    
    def __str__(self):
        return self.title

#  from tets2.models import Category, Post, Tag
#  c = Category(title = 'sport')
# c.save()
# p = Post(title='hello', text='',, category=c)
# p.save()

# p1 = Post.objects.create(title='hello2', text='', category=c)


# SELECT * from test2_post where id = 1;
# select * from test2_post;
# select text from test2_post;