from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_projek' : 'GoalHub',
        'npm' : '2406437155',
        'name': 'Yafi Alifuddin',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
