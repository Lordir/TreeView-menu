from django.db import models
from django.urls import reverse


class TreeNodeModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    parent = models.ForeignKey('NameParent', on_delete=models.PROTECT, blank=True, default=1, verbose_name="Родитель")
    slug = models.SlugField(max_length=50, blank=True, unique=True, db_index=True, verbose_name="URL")
    level = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('treenode', kwargs={'treenode_slug': self.slug})

    def save(self, *args, **kwargs):
        if not NameParent.objects.filter(name=self.name):
            data = NameParent(self.pk, self.name)
            data.save()
        if str(self.parent) == "":
            self.level = 0
        else:
            level_parent = TreeNodeModel.objects.get(name=self.parent)
            self.level = level_parent.level + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class NameParent(models.Model):
    name = models.CharField(max_length=50, blank=True, default="", verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Родитель звена'
        verbose_name_plural = 'Родитель звена'
