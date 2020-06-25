from django.db import models
from django.db.models.signals import post_save, pre_delete, m2m_changed

TYPE_QUESTION = (
	('text', 'Текст'),
	('one', 'Один вариант'),
	('few', 'Несколько вариантов')
)

class CommonInfo(models.Model):
	date_add = models.DateTimeField(verbose_name="Дата добавления", auto_now_add=True)
	date_change = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

	class Meta:
		abstract = True

class Clients(CommonInfo):
	name = models.CharField(verbose_name="Имя", max_length=255)

	class Meta:
		verbose_name = "Клиент"
		verbose_name_plural = "Клиент"

	def __str__(self):
		return '{}.{}'.format(self.id, self.name)

class Polls(CommonInfo):
	name = models.CharField(verbose_name="Название", max_length=255)
	description = models.TextField(verbose_name="Описание")
	date_start = models.DateField(verbose_name="Дата старта")
	date_end = models.DateField(verbose_name="Дата окончания")

	class Meta:
		verbose_name = "Опрос"
		verbose_name_plural = "Опросы"

	def __str__(self):
		return '{}.{} {}'.format(self.id, self.name, self.date_end)

class Options(CommonInfo):
	text = models.TextField(verbose_name="Ответ")

	class Meta:
		verbose_name = "Вариант"
		verbose_name_plural = "Варианты"

	def __str__(self):
		return '{}.{}'.format(self.id, self.text)

class Questions(CommonInfo):
	poll = models.ForeignKey('Polls', on_delete=models.CASCADE, verbose_name="Опрос")
	text = models.TextField(verbose_name="Вопрос")
	type_qustion = models.CharField(verbose_name="Тип вопроса", max_length=255, choices=TYPE_QUESTION)

	options = models.ManyToManyField(Options, verbose_name="Варианты ответов", blank=True, null=True)

	class Meta:
		verbose_name = "Вопрос"
		verbose_name_plural = "Вопросы"

	def __str__(self):
		return '{}.{}'.format(self.id, self.text)

class Answers(CommonInfo):
	client = models.ForeignKey('Clients', on_delete=models.CASCADE, verbose_name="Клиент")
	question = models.ForeignKey('Questions', on_delete=models.CASCADE, verbose_name="Вопрос")
	text = models.TextField(verbose_name="Ответ", max_length=2000)

	class Meta:
		verbose_name = "Ответ"
		verbose_name_plural = "Ответы"

	def __str__(self):
		return '{}.{}'.format(self.id, self.question)

class DialogControll(CommonInfo):
	client = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name="Клиент")
	question = models.ForeignKey(Questions, on_delete=models.CASCADE, verbose_name="Вопрос")

	class Meta:
		verbose_name = "Диалог контроллер"
		verbose_name_plural = "Диалог контроллер"

	def __str__(self):
		return '{}.{}'.format(self.id, self.client)