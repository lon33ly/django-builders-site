from django.db import models
from django.dispatch import receiver


# Create your models here.
class Projects(models.Model):
    photo = models.ImageField(upload_to='media/projects-photo/', verbose_name='Фот')
    location = models.CharField(max_length=300, null=False, default="Локация")
    title = models.CharField(max_length=300, null=False, default="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Team(models.Model):
    photo = models.ImageField(upload_to='media/team/', verbose_name='Фото')
    name = models.CharField(max_length=200, null=False)
    position = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Команда"


class IndexBadges(models.Model):
    photo = models.ImageField(upload_to='media/index-badges/')
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.CharField(max_length=500, verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Значок с главной"
        verbose_name_plural = "Значки с главной"


class ContactBadges(models.Model):
    photo = models.ImageField(upload_to='media/contact-badges')
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.CharField(max_length=500, verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Значок контактов"
        verbose_name_plural = "Значки контактов"


class Requests(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    email = models.CharField(max_length=200, verbose_name="Email")
    subject = models.CharField(max_length=150, verbose_name="Тема сообщения")
    message = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


# удалние фотки привязанной к модели в случае удаления модели
@receiver(models.signals.post_delete, sender=ContactBadges)
@receiver(models.signals.post_delete, sender=IndexBadges)
@receiver(models.signals.post_delete, sender=Projects)
@receiver(models.signals.post_delete, sender=Team)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.photo.delete(save=False)
    except Exception:
        pass


# удалние фотки привязанной к модели в случае изменения фотки модели
@receiver(models.signals.pre_save, sender=ContactBadges)
@receiver(models.signals.pre_save, sender=IndexBadges)
@receiver(models.signals.pre_save, sender=Projects)
@receiver(models.signals.pre_save, sender=Team)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).photo.path
        try:
            new_img = instance.photo.path
        except Exception:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except Exception:
        pass
