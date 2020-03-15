from django.http import JsonResponse
from django.http import HttpRequest 
from . import myScript
import os

#Set Allowed User IPs to Array
allowedIPList = ["127.0.0.1", "195.87.1.40"]


def post(HttpRequest):
    requesterIPAddress = HttpRequest.META['REMOTE_ADDR']
    if requesterIPAddress in allowedIPList:
        inputArg = HttpRequest.body
        result = myScript.myFunct(inputArg)
        context ={
                "Result": result,
                "Status":True
             }
    else:
        context = {
            "Status":False,
            "Result":"You don't have required access rights for this API, contact with an Admin."
        }
    
    return JsonResponse(context)