from api.models import *
from rest_framework import serializers

class PollsSerializers(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Polls
		fields = (
					'id', 'name', 'description',
					'date_start','date_end'
				)

class OptionsSerializers(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Options
		fields = (
					'id', 'text'
				)

class AnswerSerializers(serializers.HyperlinkedModelSerializer):
	question_text = serializers.SerializerMethodField('get_question')

	def get_question(self, obj):
		return obj.question.text

	class Meta:
		model = Answers
		fields = (
					'question_text', 'text'
				)

class QuestionsSerializers(serializers.HyperlinkedModelSerializer):
	# type_question = serializers.SerializerMethodField('get_type')
	option_list = serializers.SerializerMethodField('get_options')
	# poll_id = serializers.SerializerMethodField('get_poll_id')

	def get_type(self, obj):
		if(obj.type_qustion == 'text'):
			return 'Введите ответ в виде текста'
		elif(obj.type_qustion in ['one', 'few']):
			if(obj.type_qustion == 'one'):
				return 'Укажите номер ответа'
			else:
				return 'Укажите номера ответов через запятую'

	def get_options(self, obj):
		if(obj.type_qustion in ['one', 'few']):
			return (OptionsSerializers(obj.options.all(), many=True)).data
		else:
			return ''

	# def get_poll_id(self, obj):
	# 	return obj.poll.id

	class Meta:
		model = Questions
		fields = (
					'poll_id', 'text', 'option_list', 'type_qustion'
				)