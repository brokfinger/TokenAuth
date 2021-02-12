# TokenAuth
Небольшое приложение на Django, которое демонстрирует авторизацию через 
ссылку-токен и фиксирует количество авторизаций для каждого пользователя.

**Детальнее с условиями тестового задания можно ознакомиться по ссылке
https://docs.google.com/document/d/1SUuC69Xam2ujRRRpGb35b1KUP_GKyimC9RgIErdIrOo/edit#**

###Стек:
* Python
* Django
* Heroku (deploy)

###P.S. (пояснение)
Для решения данной задачи мой выбор пал на Django, так как это основной 
фреймворк с которым я работаю.
С начала задачу думал решить через REST framework, но проблема (для 
меня) была в невозможности сформировать ссылку с токеном, так как сам токен 
передавался в заголовке, а не самой ссылке.
Чуть позже нашел решение: воспользоваться встроенным в Django генератором 
токена (тот что для сброса пароля), для генерации токена.
Так же это решило несколько проблем: не используется стороннее решение, без
проблем формируется ссылка для отправки, и логику проверки меньше писать.
