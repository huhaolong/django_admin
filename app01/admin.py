# Register your models here.
from django.contrib import admin
from .models import *
from .views import *
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 文章列表里显示想要显示的字段
    list_display = ('title',)
    # 满50条数据就自动分页
    list_per_page = 50
    #添加需要搜索的字段
    search_fields = ('title',)
@admin.register(Cat_Content)
class FeedbackStatsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_content=None):
        return myblog(request)