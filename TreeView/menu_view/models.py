from django.db import models
from django.urls import reverse


# def get_slug(s):
#     new_slug = translit(s, 'ru')
#     new_slug = slugify(new_slug)
#     return new_slug + '-' + str(int(time()))


class TreeNodeModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    parent = models.CharField(blank=True, default="", verbose_name="Родитель")
    slug = models.SlugField(max_length=50, blank=True, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('treenode', kwargs={'treenode_slug': self.slug})

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.slug = get_slug(self.name)
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
