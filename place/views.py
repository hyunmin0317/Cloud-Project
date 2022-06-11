from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from naver_api import search, place_search
from place.forms import CommentForm
from place.models import Place, Comment


def detail(request, region):
    place = search(region)

    exist = Place.objects.filter(title=place['title'])
    if not exist:
        Place.objects.create(title=place['title'], address=place['address'] , roadAddress=place['roadAddress'] , category=place['category'] , image=place['image'] , website=place['link'] , mapx=place['mapx'] , mapy=place['mapy'] )
    data = Place.objects.get(title=place['title'])
    context = {'data':data, 'comment_form':CommentForm}
    return render(request, 'place/detail.html', context)


def search_place(request):
    region = request.GET.get('query', '')  # 검색어
    data_list = place_search(region)
    context = {'data_list':data_list}
    return render(request, 'place/search.html', context)


@login_required()
def new_comment(request, region):
    if request.user.is_authenticated:
        place = get_object_or_404(Place, title=region)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST, request.FILES)
            print(request.FILES)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.place = place
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
            else:
                return redirect(place.get_absolute_url())
        else:
            raise PermissionDenied


@login_required()
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect(comment.get_absolute_url())


@login_required()
def modify_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('home')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.save()
            return redirect(comment.get_absolute_url())
        else:
            return redirect(comment.get_absolute_url())
    else:
        form = CommentForm(instance=comment)
        context = {'comment_form':form}
        return render(request, 'place/modify.html', context)


@login_required()
def like_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place.voter.add(request.user)
    return redirect(place.get_absolute_url())

@login_required()
def unlike_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place.voter.remove(request.user)
    return redirect(place.get_absolute_url())