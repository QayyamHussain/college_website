from django.shortcuts import render
from .models import Add_teacher, Skills

# Create your views here.

def teacher_list(request):
	all_teachers = Add_teacher.objects.all()
	data = {'all_teachers': all_teachers}
	return render(request, 'teacher_list.html', data)

def get_teacher_skills(request, pk):
	get_teacher = Add_teacher.objects.get(id=pk)
	all_skill = get_teacher.select_skills.all()
	data = {'get_teacher': get_teacher, 'all_skill': all_skill}
	return render(request, 'skills.html', data)
