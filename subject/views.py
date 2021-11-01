from django.shortcuts import render
from subject.models import Add_subject

def add_subject(request):
	all_subjects = Add_subject.objects.all()
	data={'all_subjects':all_subjects}
	return render(request, 'subject_list.html',data)