from django.shortcuts import render, redirect

# Create your views here.
from petstagram.accounts.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None
