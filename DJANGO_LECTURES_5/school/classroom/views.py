#from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from classroom.forms import ContactForm
from classroom.models import Teacher

# Create your views here.
class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    model = Teacher
    # auto search "model_form.html"
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')

class TeacherListView(ListView):
    # model_list.html
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')
    context_object_name = "teacher_list"

class TeacherDetailView(DetailView):
    # RETURN ONLY ONE MODEL ENTRY PK
    # model_detail.html
    model = Teacher
    # PK --> {{teacher}}

class TeacherUpdateView(UpdateView):
    #SHARE model_form.html
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:list_teacher')

class TeacherDeleteView(DeleteView):
    #Form --> Confirm Delelte Button
    # default template name => model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    #URL NOT a template.html (This is just URL, NOT html)
    success_url = '/classroom/thank_you/'  #  =reverse_lazy('classroom:thank_you') => 객체를 반환

    # what to do with form?
    def form_valid(self,form):
        print(form.cleaned_data)
        # similar "contactForm(request.POST)"
        return super().form_valid(form)