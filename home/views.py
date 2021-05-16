from django.shortcuts import render, HttpResponse
from summarize import generate_summary

# Create your views here.
def home(request):
    #return HttpResponse("This is homepage")
    return render(request,'home.html')

#summary functions read,generate summary, similarity matrix 
def sumry(request):
    if request.method=="POST":
        texta=request.POST['textcontent']
        line=request.POST['dropdown']
        num=int(line)
        print(len(texta))
        a=texta.split(".")
        print("length of a:",len(a)) 
        if len(texta)<=200 or texta=="" or len(a)-1<num:
            return render(request,'summarygenerate.html', {'s1':"Text is summarized enough"})
        text_clean=texta.replace('\r\n', ' ')
        print(text_clean)
        sum=generate_summary(text_clean, num)
        print("This is summary from views.py")
        print("Summary:".join(sum))
        s1=".".join(sum)
        #print("This is s1"+s1)
        return render(request,'summarygenerate.html', {'s1':s1,'texta':texta})
    return render(request,'summarygenerate.html') 
    


