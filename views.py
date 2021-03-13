from django.shortcuts import render
from .forms import videoupload , fadeinn , speedx1,volumex1,gammacorrection1,rotate1,subclip1
import os
from django.http import HttpResponseRedirect
from moviepy.editor import *
from django.template import RequestContext
# Create your views here.
def handler404(request, *args, **argv):
    response = render('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
def screen1(request)  :
    return render(request,"404.html")
def handle_uploaded_file1(f):
    global r
    path="static/"
    r=f.name
    with open(path+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def home_view1(request,*args):
    if request.POST:
        form = videoupload(request.POST, request.FILES)
        if form.is_valid():

           handle_uploaded_file1(request.FILES["Choose_File"])
           return HttpResponseRedirect('/coralcut/')
    else:
       form = videoupload()
       try :newclip1=VideoFileClip("static\%s"%(r)).duration
       except:pass
       try :args={'form':form,'r':r,'newclip1':newclip1}
       except :
              try :args={'form':form,'r':r}
              except :
                     try :args={'form':form}
                     except: pass
       return render(request, "coralcut.html", args)

def bandw(request):
    global r
    myclip=VideoFileClip("static\%s"%(r))
    newclip = myclip.fx( vfx.blackwhite,RGB=None, preserve_luminosity=True)
    newclip.write_videofile("static/1%s"%(r))
    r="1%s"%(r)
    return HttpResponseRedirect('/coralcut/')

def painting(request):
    global r
    myclip=VideoFileClip("static\%s"%(r))
    newclip = myclip.fx( vfx.painting,saturation=1.4, black=0.006)
    newclip.write_videofile("static/2%s"%(r))
    r="2%s"%(r)
    return HttpResponseRedirect('/coralcut/')

def mirrorx(request):
    global r
    myclip=VideoFileClip("static\%s"%(r))
    newclip = myclip.fx( vfx.mirror_x, apply_to='mask')
    newclip.write_videofile("static/3%s"%(r))
    r="3%s"%(r)
    return HttpResponseRedirect('/coralcut/')

def mirrory(request):
    global r
    myclip=VideoFileClip("static\%s"%(r))
    newclip = myclip.fx( vfx.mirror_y, apply_to='mask')
    newclip.write_videofile("static/4%s"%(r))
    r="4%s"%(r)
    return HttpResponseRedirect('/coralcut/')

def fadein(request):
    global r
    form=fadeinn(request.POST)
    if form.is_valid():
     myclip=VideoFileClip("static\%s"%(r))
     newclip = myclip.fx( vfx.fadein,form.cleaned_data['duration'] , initial_color=form.cleaned_data['initial_color'])
     newclip.write_videofile("static/5%s"%(r))
     r="5%s"%(r)
     return HttpResponseRedirect('/coralcut/')

def fadeout(request):
    global r
    form=fadeinn(request.POST)
    if form.is_valid():
     myclip=VideoFileClip("static\%s"%(r))
     newclip = myclip.fx( vfx.fadeout,form.cleaned_data['duration'] , final_color=form.cleaned_data['initial_color'])
     newclip.write_videofile("static/6%s"%(r))
     r="6%s"%(r)
     return HttpResponseRedirect('/coralcut/')

def invertcolor(request):
    global r
    myclip=VideoFileClip("static\%s"%(r))
    newclip = myclip.fx( vfx.invert_colors)
    newclip.write_videofile("static/7%s"%(r))
    r="7%s"%(r)
    return HttpResponseRedirect('/coralcut/')
def speedx(request):
    global r
    form=speedx1(request.POST)
    if form.is_valid():
     myclip=VideoFileClip("static\%s"%(r))
     newclip = myclip.fx( vfx.speedx,final_duration=form.cleaned_data['final_duration'])
     newclip.write_videofile("static/8%s"%(r))
     r="8%s"%(r)
     return HttpResponseRedirect('/coralcut/')
def volumex(request):
    global r
    form=volumex1(request.POST)
    if form.is_valid():
     myclip=VideoFileClip("static\%s"%(r))
     newclip = myclip.volumex(form.cleaned_data['factor'])
     newclip.write_videofile("static/9%s"%(r))
     r="9%s"%(r)
     return HttpResponseRedirect('/coralcut/')
def timesymmetrize(request):
    global r
    myclip=VideoFileClip("static\%s"%(r))
    newclip = myclip.fx( vfx.time_symmetrize)
    newclip.write_videofile("static/10%s"%(r))
    r="10%s"%(r)
    return HttpResponseRedirect('/coralcut/')
def contrast(request):
    global r
    myclip=VideoFileClip("static\%s"%(r))
    newclip = myclip.fx( vfx.lum_contrast,lum=0, contrast=0, contrast_thr=127)
    newclip.write_videofile("static/11%s"%(r))
    r="11%s"%(r)
    return HttpResponseRedirect('/coralcut/')
def reverse(request):
    global r
    myclip=VideoFileClip("static\%s"%(r))
    newclip = myclip.fx( vfx.time_mirror)
    newclip.write_videofile("static/12%s"%(r))
    r="12%s"%(r)
    return HttpResponseRedirect('/coralcut/')
def rotate(request):
    global r
    form=rotate1(request.POST)
    if form.is_valid():
     myclip=VideoFileClip("static\%s"%(r))
     newclip = myclip.add_mask().rotate(form.cleaned_data['angle'], unit='deg', resample='bicubic', expand=True)
     newclip.write_videofile("static/13%s"%(r))
     r="13%s"%(r)
     return HttpResponseRedirect('/coralcut/')
def gammacorrection(request):
    global r
    form=gammacorrection1(request.POST)
    if form.is_valid():
     myclip=VideoFileClip("static\%s"%(r))
     newclip = myclip.fx( vfx.gamma_corr,form.cleaned_data['factor1'])
     newclip.write_videofile("static/14%s"%(r))
     r="14%s"%(r)
     return HttpResponseRedirect('/coralcut/')
def subclip(request):
    global r
    form=subclip1(request.POST)
    if form.is_valid():
     myclip=VideoFileClip("static\%s"%(r))
     newclip = myclip.subclip(form.cleaned_data['start_time'],form.cleaned_data['end_time'])
     newclip.write_videofile("static/15%s"%(r))
     r="15%s"%(r)
     return HttpResponseRedirect('/coralcut/')
def evensize(request):
     global r
     myclip=VideoFileClip("static\%s"%(r))
     newclip = myclip.fx( vfx.even_size)
     newclip.write_videofile("static/16%s"%(r))
     r="16%s"%(r)
     return HttpResponseRedirect('/coralcut/')
