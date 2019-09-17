from django.db import models

# Create your models here.
# 影视模块表
class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=60)
    parentid = models.IntegerField()#0代表父模块，非0代表子模块
    # compere = models.CharField(max_length=30, blank=True, null=True)
    # description = models.CharField(max_length=1000, blank=True, null=True)
    orderby = models.IntegerField(blank=True, null=True)
    # namestyle = models.CharField(max_length=10, blank=True, null=True)
    # logo = models.CharField(max_length=200, blank=True, null=True)
    # themenum = models.IntegerField(blank=True, null=True)
    # replynum = models.IntegerField(blank=True, null=True)
    # lastpost = models.CharField(max_length=600, blank=True, null=True)



# 电影
class Film(models.Model):
    fid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=200)
    style = models.IntegerField()#1代表动作片，2代表喜剧片，3代表爱情片


#电视剧
class Teleplay(models.Model):
    tid = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=200)
    style = models.IntegerField()#1国产剧，2日韩剧，3欧美剧


# 综艺
class Shows(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=200)
    style = models.IntegerField()


# 动漫
class Cartoon(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=200)
    style = models.IntegerField()  # 1国产动漫，2日韩动漫


# 影视细节
class Videodetail(models.Model):
    staus = models.CharField(blank=True, null=True,max_length=500)#状态
    protagonist = models.CharField(blank=True, null=True,max_length=500)#主演
    correlation = models.CharField(blank=True, null=True,max_length=500)#相关
    type = models.CharField(blank=True, null=True,max_length=500)#类型
    director = models.CharField(blank=True, null=True,max_length=500)#导演
    year = models.IntegerField(blank=True, null=True)#年份
    update = models.DateTimeField(blank=True, null=True)#更新
    region = models.CharField(blank=True, null=True,max_length=500)#地区
    language = models.CharField(blank=True, null=True,max_length=500)#语言
    synopsis = models.CharField(blank=True, null=True,max_length=500)#剧情简介
    film = models.ForeignKey(Film, models.DO_NOTHING, db_column='fid', related_name='vdetail', blank=True, null=True)
    teleplay = models.ForeignKey(Teleplay, models.DO_NOTHING, db_column='tid', blank=True, related_name='vdetail', null=True)
    shows = models.ForeignKey(Shows, models.DO_NOTHING, db_column='sid', related_name='vdetail', blank=True, null=True)
    cartoon = models.ForeignKey(Cartoon, models.DO_NOTHING, db_column='cid', blank=True, related_name='vdetail', null=True)








