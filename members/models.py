from django.db import models
from django.utils import timezone  
from django.urls import reverse

from ckeditor.fields import RichTextField

# Create your models here.

class Members(models.Model):

	EDUCATION_LEVEL = (
		('d','دیپلم')  , 
		('b' , 'لیسانس') , 
		('m' , 'فوق لیسانس') , 
		('p' , 'دکترا')
		)
	firstname = models.CharField('نام'  , max_length = 200 )
	lastname  = models.CharField('نام خانوادگی'  , max_length = 200 )
	birthday  = models.DateTimeField('تاریخ تولد ')
	phone_number = models.IntegerField('شماره تلفن '  ) 
	code_melli = models.IntegerField('کد ملی ' ,  ) 
	education_level = models.CharField('تحصیلات  ' , max_length = 1 , choices = EDUCATION_LEVEL )

	
	def __str__(self) : 
		return self.firstname + ' _ ' + self.lastname 

	class Meta :  
		db_table = 'Members'
		verbose_name_plural = 'اعضا'



class Category(models.Model) : 

	name = models.CharField('نام گروه ' , help_text = "نام  گروه خبری " , max_length = 200 ) 
	slug = models.SlugField(verbose_name = 'آدرس اینترنتی ' , max_length = 200 ) 

	def __str__(self) : 
		return self.name 

	def get_absolute_url(self) : 
		pass 


	class Meta : 
		db_table = 'Category' 
		verbose_name_plural = 'دسته بندی ها '




class Article(models.Model) : 
	STATUS = (
		('p' , 'منتشر شود ') , 
		('d'  , 'پیش نویس باقی بماند ')
		)
	title = models.CharField('عنوان' , max_length = 200 )
	category = models.ForeignKey('Category' , verbose_name = 'دسته بندی ' , on_delete = models.SET_NULL , blank = True , null = True )
	slug  = models.SlugField('آدرس مقاله '  , max_length = 200 , unique = True  )
	picture = models.FileField('عکس سر تیتر ' , upload_to = "Article_picture" , blank = True , null = True )
	discription = RichTextField(blank = True , null = True , verbose_name = 'متن مقاله ')
	author = models.ForeignKey('Members'  , verbose_name = 'نویسنده'  , on_delete = models.CASCADE, null = True , blank = True )
	created = models.DateTimeField('زمان انتشار ' , default = timezone.now )

	updated = models.DateTimeField(auto_now_add = True  ) 
	status  = models.CharField('وضعیت' , choices = STATUS  , default ='d' , max_length = 1  ) 
	class Meta : 
		db_table = 'Article'
		verbose_name_plural  = 'محتوای خبری '


	def __str__(self) : 
		return self.title 


	def get_absolute_url(self) :
		return  reverse('detail_post' , args = [self.slug , str(self.id)])







class Contact(models.Model) : 
	full_name = models.CharField(verbose_name = 'نام و نام خانوادگی '  , max_length = 400 )
	title = models.CharField('عنوان' , max_length = 200 )
	email = models.EmailField(verbose_name = 'ایمیل')
	message = RichTextField(verbose_name = 'پیام' , blank = True , null = True ) 
	file = models.FileField(verbose_name = 'فایل'  , upload_to = 'Cantact_with_me' )

	def __str__(self) : 
		return self.title   


	class Meta : 
		db_table = 'Contact'
		verbose_name_plural = 'ارتباط با ما '


