from django.shortcuts import render,HttpResponse,redirect
from .forms import imageForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required,permission_required
import os
import sys
from django.core.files import File
from detect.copy_move_detection.CopyMoveDetection import *
from threading import Thread
import threading
import cv2

threadLimiter = threading.BoundedSemaphore(1)

class MyThread(threading.Thread):

    def run(self):
        threadLimiter.acquire()
        try:
            self.disp1()
        finally:
            threadLimiter.release()

    def disp1(self):
        main()
        messages.info(request,"Thank you for being Patient, ThankYou")
        return render(request,"final.html",{})
        





BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



allowed_extention = ["jpeg","jpg","png"]


# Create your views here.
@login_required(login_url='/')
def detect(request):
    if request.method == "POST":

        data = request.FILES['sample_image']
        data1 = str(data)
        img, extention = data1.split(".")
        if extention in allowed_extention:
            with open("accounts/media/detect/empty.png", "wb") as img:
                with data as image:
                    myfile = File(img)
                    for i in image:
                        myfile.write(i)

                    img.close()
                    myfile.close()

            image = cv2.imread("accounts/media/detect/empty.png",1)
 
            img = cv2.resize(image, (512, 512),  
               interpolation = cv2.INTER_NEAREST)
            cv2.imwrite("accounts/media/detect/empty.png", img)   
            main()
            messages.info(request,"Thank you for being Patient, ThankYou")
            return render(request,"final.html",{})
     

        else:
            messages.ERROR(request,"Please provide Valid Image File(JPEG/JPG/PNG)")
            return redirect('detect:detector')

    else:
        return render(request,"upload.html",{'image_form':imageForm})
