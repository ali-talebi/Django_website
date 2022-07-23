from django.contrib import admin
from .models import Members , Article  , Contact   , Category  
# Register your models here.
@admin.register(Members)
class MembersAdmin(admin.ModelAdmin) : 
	list_display = ('firstname' , 'lastname' , 'birthday' , 'phone_number' , 'code_melli' , 'education_level' )
	list_filter = ('education_level'  , )
	list_editable = ('education_level' ,  )
	search_fields = ('firstname' , 'lastname' , 'phone_number' , 'code_melli') 

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin) : 
	list_display = ('title' ,'author' ,'created' , 'status' )
	list_filter = ('status' , )
	search_fields = ('title' , 'description' , )
	list_editable = (    'status' , 'author'   )
	prepopulated_fields = {'slug' : ('title' , )}
	ordering = ('-created' , )



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin) : 
	list_display = ('title' , 'full_name'  , 'email' )
	search_fields = ('title' , 'full_name' , 'email' )


@admin.register(Category) 
class CategoryAdmin(admin.ModelAdmin) : 
	list_display  = ['name' , 'slug' ]
	search_fields = ['name' , 'slug' ]
	prepopulated_fields = {'slug' : ('name' , ) }
	 

