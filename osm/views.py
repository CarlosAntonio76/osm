from django.shortcuts import render
from django.http import HttpResponse
#from . utils import password_is_valid, email_html
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth
import os
from django.conf import settings
#from .models import Ativacao
from hashlib import sha256

