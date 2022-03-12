from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField(label="이메일주소")
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error(
                    "password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError(
                "User does not exist"))


class SignUpForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = ("first_name", "email", "hp")
        labels = {
            'first_name': '사용자이름',
            'email': '이메일주소',
            'hp': '전화번호',
        }
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")
    password1 = forms.CharField(
        widget=forms.PasswordInput, label="비밀번호 확인")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("이미 사용중인 이메일입니다.")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)

        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()
