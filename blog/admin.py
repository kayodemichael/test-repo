from django.contrib import admin
from blog.models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Post, ArticleAdmin)
admin.site.register(Comment)
