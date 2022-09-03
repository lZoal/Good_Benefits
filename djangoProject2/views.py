from django.shortcuts import render
from rest_framework.views import APIView
from Good_Benefits.models import Feed


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all()
        return render(request, 'Good_Benefits/main.html', context=dict(feed_list=feed_list))