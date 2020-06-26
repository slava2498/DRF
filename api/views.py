from api.models import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from api.serializers import PollsSerializers, QuestionsSerializers, AnswerSerializers
from rest_framework.authtoken.models import Token
from rest_framework import authentication, permissions, viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework import status
from datetime import datetime, timedelta, date
from rest_framework.authtoken.models import Token
from rest_framework import authentication, permissions

class Input(APIView):
	def get(self, request, format=None):
		return Response({
			'poll': reverse('polls', request=request),
			'question': reverse('questions', request=request),
			'start': reverse('start_polls', request=request),
		})

	def post(self, request, format=None):
		email = request.data.get("email")
		password = request.data.get("password")
		user = User.objects.filter(email=email, password=password)
		if user:
			already = Token.objects.filter(user=user[0])
			if (already): already.delete()
			token = Token.objects.create(user=user[0])
			return Response({"token": token.pk})
		else:
			return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class PollsAnswer(ListModelMixin, GenericAPIView):
	def get(self, request):
		user_id = self.request.data.get('user_id')
		poll_id = self.request.data.get('poll_id')
		print(user_id, poll_id)
		if(not (user_id and poll_id)):
			return Response({"error": "Укажите user_id и poll_id"}, status=status.HTTP_400_BAD_REQUEST)

		client = Clients.objects.get(id=user_id)
		if(not client):
			return Response({"error": "Пользователь не найден"}, status=status.HTTP_400_BAD_REQUEST)
		controller = DialogControll.objects.filter(client=client)
		if(controller):
			answer = self.request.data.get('answer')
			if(not answer):
				return Response({"error": "Укажите answer"}, status=status.HTTP_400_BAD_REQUEST)

			controller = controller[0]
			if(controller.question.type_qustion == 'one'):
				option = controller.question.options.filter(id=answer)
				if(not option):
					return Response(
										{"error": "Ответа с номером {} не найдено".format(x)},
										status=status.HTTP_400_BAD_REQUEST
									)
				Answers.objects.create(client=client, question=controller.question, text=option[0].text)

			elif(controller.question.type_qustion == 'few'):
				if(not ',' in answer):
					return Response({"error": "Укажите ответ в формате '1,2,3'"}, status=status.HTTP_400_BAD_REQUEST)

				messageanswer = ''
				answer.replace(' ', '')
				for x in answer.split(','):
					option = controller.question.options.filter(id=x)
					if(not option):
						return Response(
											{"error": "Ответа с номером {} не найдено".format(x)},
											status=status.HTTP_400_BAD_REQUEST
										)
					messageanswer += option[0].text + ', '

				Answers.objects.create(client=client, question=controller.question, text=messageanswer)

			elif(controller.question.type_qustion == 'text'):
				Answers.objects.create(client=client, question=controller.question, text=answer)

		poll = Polls.objects.filter(id=poll_id, date_start__lte=datetime.now(), date_end__gte=datetime.now())
		if(not poll):
			return Response({"error": "Опрос не найден"}, status=status.HTTP_400_BAD_REQUEST)

		poll = poll[0]
		questions_id = Answers.objects.filter(client=client).values('question_id')
		question = Questions.objects.filter(poll=poll).exclude(id__in=questions_id)
		controller.delete()
		if(not question):
			return Response({'data': 'Опрос окончен'})

		DialogControll.objects.create(client=client, question=question[0])
		serializer = QuestionsSerializers(question[0])
		return Response(serializer.data)

class PollsResult(ListModelMixin, GenericAPIView):
	def get(self, request):
		user_id = self.request.data.get('user_id')
		poll_id = self.request.data.get('poll_id')
		print(user_id, poll_id)
		if(not (user_id and poll_id)):
			return Response({"error": "Укажите user_id и poll_id"}, status=status.HTTP_400_BAD_REQUEST)

		client = Clients.objects.get(id=user_id)
		if(not client):
			return Response({"error": "Пользователь не найден"}, status=status.HTTP_400_BAD_REQUEST)

		poll = Polls.objects.filter(id=poll_id)
		if(not poll):
			return Response({"error": "Опрос не найден"}, status=status.HTTP_400_BAD_REQUEST)

		poll = poll[0]
		answer = Answers.objects.filter(client=client, question__poll=poll)
		serializer = AnswerSerializers(answer, many=True)
		return Response(serializer.data)

class PollsView(viewsets.ModelViewSet):
	# authentication_classes = [authentication.TokenAuthentication]
	# permission_classes = [permissions.IsAuthenticated]

	serializer_class = PollsSerializers
	queryset = Polls.objects.all()

class QuestionsView(viewsets.ModelViewSet):
	# authentication_classes = [authentication.TokenAuthentication]
	# permission_classes = [permissions.IsAuthenticated]

	serializer_class = QuestionsSerializers
	queryset = Questions.objects.all()
	def create(self, request):
		poll = get_object_or_404(Polls, id=self.request.data.get('poll_id'))
		text = self.request.data.get('text')
		type_qustion = self.request.data.get('type_qustion')
		array = []
		question = Questions.objects.create(poll=poll, text=text, type_qustion=type_qustion)
		if(type_qustion == 'few'):
			options = self.request.data.get('options_id')
			options.replace(' ', '')
			for x in options.split(','):
				question.options.add(Options.objects.filter(id=x))

		elif(type_qustion == 'one'):
			question.options.add(Options.objects.filter(id=self.request.data.get('options_id')))

		serializer = QuestionsSerializers(question)
		return Response(serializer.data)


