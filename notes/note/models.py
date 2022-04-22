from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Note(models.Model):
    text = models.TextField("Текст заметки")
    pub_date = models.DateTimeField("Дата заметки",
                                    auto_now_add=True,
                                    db_index=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='note')

    def __str__(self):
        return self.text[:15]


class NoteImage(models.Model):
    note = models.ForeignKey(Note,
                             on_delete=models.CASCADE,
                             related_name='note_images'
                             )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='note_images'
                               )
    image = models.ImageField(
        'Картинка',
        upload_to='notes_images/',
        null=True,
        blank=True
    )
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )
    image_url = models.URLField(
        max_length=500,
        default='https://upload.wikimedia.org/wikipedia/commons/thumb/9/99'
                '/Full_stop.png/180px-Full_stop.png'
    )


class TemporaryImage(models.Model):
    image = models.ImageField(upload_to='temp_images/', blank=True, null=True)
    key = models.CharField(max_length=100)
