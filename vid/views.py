from django.shortcuts import render
from django.http import HttpResponse
#from contact_form.forms import ContactForm
from .forms import MyVideoForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import MyVideo
import subprocess


def post_list(request):
    return render(request, 'vid/vid_list.html', {})


def index(request):
    Command = "python manage.py runscript scripts.myscripts"
    process = subprocess.check_output(Command.split())

    videos = MyVideo.objects.all()
    return render(request, 'vid/index.html', {'videos': videos,'process':process})

'''
def vid_detail(request, pk):
        video = get_object_or_404(MyVideo, pk=pk)
        if request.method == "POST":
            form = MyVideoForm(request.POST,instance=video)
            if form.is_valid():
                video = form.save(commit=False)
                video.save()
                return redirect('vid_detail', pk=video.pk)
        else:
            form = MyVideoForm()
        return render(request, 'vid/embed.html', {'form': form}) '''


def vid_detail(request, pk):
    video = get_object_or_404(MyVideo, pk=pk)
    return render(request, 'vid/vid_detail.html', {'video': video})


def embed(request):
    if request.method == "POST":
        form = MyVideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.save()
            return redirect('vid_detail', pk=video.pk)
    else:
        form = MyVideoForm()
    return render(request, 'vid/embed.html', {'form': form})