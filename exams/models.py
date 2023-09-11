from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, validate_comma_separated_integer_list
from django.db import models
from polymorphic.models import PolymorphicModel
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from core.models import BaseModel


class Quiz(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    is_random = models.BooleanField(default=False)
    show_correct = models.BooleanField(default=False)
    single_attempt = models.BooleanField(default=False)
    pass_mark = models.IntegerField(default=0, validators=[MaxValueValidator(100)])
    is_active = models.BooleanField(default=False)

    def save(
        self, force_insert=False, force_update=False, *args, **kwargs
    ):
        if self.pass_mark > 100:
            raise ValidationError("%s is above 100" % self.pass_mark)
        super(Quiz, self).save(force_insert, force_update, *args, **kwargs)

    def __str__(self):
        return f"Kuis {self.title}"

    def get_questions(self):
        return self.question_set.all()


class Question(BaseModel, PolymorphicModel):
    content = models.CharField(max_length=200)
    level = models.CharField(max_length=10)
    quiz = models.ManyToManyField(Quiz)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Take(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, verbose_name=_("Quiz"), on_delete=models.CASCADE)
    question_order = models.CharField(max_length=1024, validators=[validate_comma_separated_integer_list])
    question_list = models.CharField(max_length=1024, validators=[validate_comma_separated_integer_list])
    score = models.IntegerField()

    is_complete = models.BooleanField(default=False)
    start = models.DateTimeField(auto_now_add=True, null=True)
    end = models.DateTimeField(null=True, blank=True)

    def add_score(self, score):
        self.score += int(score)
        self.save()

    def _question_ids(self):
        return [int(i) for i in self.question_order.split(",")]

    def get_questions(self, with_answer=False):
        question_ids = self._question_ids()
        questions = sorted(self.quiz.question_set.filter(pk__in=question_ids),
                           key=lambda q: question_ids.index(q))
        if with_answer:
            pass
        return questions

    def new_take(self, user, quiz):
        if quiz.is_random:
            question_set = quiz.question_set.all().order_by("?")
        else:
            question_set = quiz.question_set.all()
        question_set = [item.id for item in question_set]

        if len(question_set) == 0:
            raise ValidationError("Question Set is empty")
        questions = ",".join(map(str, question_set)) + ","

        new_take = self.create(user=user,
                                  quiz=quiz,
                                  question_order=questions,
                                  question_list=questions
                                  )
        return new_take

    def user_sitting(self, user, quiz):
        try:
            take = self.get(user=user, quiz=quiz)
        except Take.DoesNotExist:
            take = self.new_take(user, quiz)
        except Take.MultipleObjectsReturned:
            take = self.filter(user=user, quiz=quiz)[0]
        return take

