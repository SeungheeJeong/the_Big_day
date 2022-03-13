from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Challenge, Photo
from . import forms


@login_required(login_url='users:login')  # 로그인을 어노테이션 - 로그인 상태에서 작동되게
def Challenge_create(request):
    """
    챌린지 게시하기
    """
    if request.method == 'POST':
        form = forms.CreateChallengeForm(request.POST)
        if form.is_valid():
            # 데이터베이스에 저장하기 전에 commit=False는 임시저장, date를 생성하기 위해 잠시 기다리는 중
            challenge = form.save(commit=False)
            challenge.host = request.user
            challenge.save()
            # 저장이 끝나면 index(질문목록) 화면으로 돌아간다.
            return redirect('challenges:list')
    else:
        form = forms.CreateChallengeForm()
        context = {'form': form}
    return render(request, 'challenges/challenge_create.html', context)


# class ChallengeDetailView(DetailView):
#     challenge = models.Challenge
#     template_name = "challenges/challenge_detail.html"
#     form_class = forms.ChallengeDetailForm

@login_required(login_url='users:login')
def challengedetail(request, challenge_id):
    """
    내용 출력
    """
    challenge = Challenge.objects.get(id=challenge_id)
    context = {'challenge': challenge}
    return render(request, 'challenges/challenge_detail.html', context)


@login_required(login_url='users:login')
def challenger(request, challenge_id):
    #current = get_object_or_404(Challenge, pk=challenge_id)
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    challengers_list = challenge.challenger.all()
    if request.user in challenge.challenger.all():
        challenge.challenger.remove(request.user)
    else:
        challenge.challenger.add(request.user)
    return redirect('challenges:detail', challenge_id=challenge.id)


def ChallengeList(request):
    page = request.GET.get('page', '1')
    challenge_list = Challenge.objects.all()
    paginator = Paginator(challenge_list, 10)
    page_obj = paginator.get_page(page)
    print(vars(page_obj.paginator))
    context = {"challenge_list": page_obj}
    return render(request, "challenges/challenge_list.html", context)


@login_required(login_url='users:login')
def challenge_delete(request, challenge_id):
    """
    challenge삭제
    """
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    if request.user != challenge.host:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('challenges:detail', challenge_id=challenge.id)
    challenge.delete()
    return redirect('challenges:list')
