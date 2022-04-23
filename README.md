# notes_app_test
Django проект для работы с заметками.

# api endpoints:
/api/v1/auth/users/ - создание пользователя

/api/v1/auth/jwt/create/ - получение/обновление токена

/api/v1/note/ - список заметок пользователя

/api/v1/note/<note_id>/ - детальная информация о заметке

/api/v1/note/<note_id>/images/ - список изображений, прикреплённых к заметке

/api/v1/note/<note_id>/images/<images_id> - детальная информация о изображении
