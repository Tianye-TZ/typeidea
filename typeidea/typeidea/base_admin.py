from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1. 自动补充文章，分类，标签，侧边栏，友链这些 model 的 owner 字段
    2. 用来针对 queryset 过滤当前用户的数据
    """
    exclude = ('owner', )

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)


class BaseCommentAdmin(admin.ModelAdmin):
    """
    1. 自动补充评论的 nickname 字段
    2. 用来针对 queryset 过滤当前用户的数据
    """
    exclude = ('nickname', )

    def save_model(self, request, obj, form, change):
        obj.nickname = request.user
        return super(BaseCommentAdmin, self).save_model(request, obj, form, change)
    
    def get_queryset(self, request):
        qs = super(BaseCommentAdmin, self).get_queryset(request)
        return qs.filter(nickname=request.user)