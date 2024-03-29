from django import forms
from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

    
class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    form = PostAdminForm
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
# admin.site.register(Comment)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'author', 'body', 'approved', 'created_on')
    list_filter = ('approved', 'created_on',)
    search_fields = ['body', 'author__username', 'post__title']

    def post_title(self, obj):
        return obj.post.title
    post_title.admin_order_field = 'post__title'  # Allows column order sorting
    post_title.short_description = 'Post Title'  # Renames column head