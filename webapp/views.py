from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def blog(request):
    if request.method=="GET":
        result=[]

        blogs=Post.objects.all()
        for blog in blogs:
            data={
                "creator":blog.creator,
                "description":blog.description,
                "comments":blog.comments
            }
            result.append(data)
        return HttpResponse(json.dumps(result))
    
    if request.method=="POST":
        body_unicode=request.body.decode('utf=8')
        data=json.loads(body_unicode)
        creator=data['creator']
        description=data['description']
        comments=data['comments']

        blog=Post(creator=creator,description=description,comments=comments)
        blog.save()
        return HttpResponse({"company added successfully"})
    
    if request.method=="DELETE":
        body_unicode=request.body.decode('utf=8')
        data=json.loads(body_unicode)
        creator=data['creator']
        blog=Post.objects.filter(creator=creator).delete()
        return HttpResponse({"company deleted successfully"})


    if request.method=="PUT":
         Id=request.GET.get("id")
         body_unicode=request.body.decode('utf=8')
         data=json.loads(body_unicode)
         creator=data['creator']
         description=data['description']
         comments=data['comments']
         blog=Post.objects.filter(Id=id).first()
         blog.update()
         blog.save()
         return HttpResponse({"company updated successfully"})

        
           