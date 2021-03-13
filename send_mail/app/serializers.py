# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 11:30:38 2021

@author: TIMER
"""

from rest_framework import serializers
from app.models import ReplyMail

class ReplyMailSer(serializers.ModelSerializer):
    class Meta:
        model = ReplyMail
        fields = ["id", "email", "name", "message"]