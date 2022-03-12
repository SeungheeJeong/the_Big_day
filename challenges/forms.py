from django import forms
from .models import Challenge, Photo


class CreateChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge  # 사용할 모델
        fields = ['subject', 'description', 'routine', 'num_of_auth_per_day', 'date_start',
                  'date_finish']  # QuestionForm 에서 사용할 Question 모델의 속성


class UserAuthForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['file', 'caption']
        labels = {
            'file': '인증사진',
            'caption': ''
        }


class ChallengeDetailForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['subject', 'description', 'routine', 'date_start',
                  'date_finish']
