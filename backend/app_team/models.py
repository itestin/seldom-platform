from django.db import models

# Create your models here.
class Team(models.Model):
    '''
    测试团队
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField("团队名",max_length=200,null=False)
    is_delete = models.BooleanField('删除',default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name