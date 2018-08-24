from django.db import models
from DjangoUeditor.models import UEditorField
from django.utils import timezone

# Create your models here.




class BlogCtg(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name


class BlogsPost(models.Model):
    title = models.CharField( u"文章标题" ,max_length=150)    # 博客标题
    content = UEditorField(u"文章正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/meimg/",
                           toolbars='besttome', filePath='uploads/mefile/')
    timestamp = models.DateTimeField(u"上传时间", default=timezone.now())          # 创建时间
    category = models.ForeignKey(BlogCtg,  blank=True, null=True)

    def __unicode__(self):
        return self.category.name


