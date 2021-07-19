from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView

from boardapp.decorators import survey_ownership_required
from boardapp.models import surveyModel


@method_decorator(login_required, name="dispatch")
class surveyCreate(CreateView):
    model = surveyModel
    template_name = 'boardapp/createSurvey.html'
    fields = ['title', 'description', 'link', 'category', 'dueDate']

    def form_valid(self, form):
        temp_found = form.save(commit=False)
        temp_found.writer = self.request.user
        temp_found.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('boardapp:surveyList')


@method_decorator(login_required, name="dispatch")
class SurveyDetailView(DetailView):
    model = surveyModel
    context_object_name = 'target_survey'
    template_name = 'boardapp/detailView.html'
    fields = ['title', 'description', 'link', 'category', 'd_day']


@method_decorator(survey_ownership_required, 'get')
@method_decorator(survey_ownership_required, 'post')
class SurveyUpdateView(UpdateView):
    model = surveyModel
    context_object_name = 'target_survey'
    template_name = 'boardapp/editSurvey.html'
    fields = ['title', 'description', 'link', 'category', 'dueDate']

    def get_success_url(self):
        return reverse('boardapp:surveyDetail', kwargs={'pk': self.object.pk})


def survey_delete(request, pk):
    survey = surveyModel.objects.get(id=pk)
    if request.user != survey.writer:
        messages.error(request, "삭제권한이 없습니다")
    else:
        survey.delete()
        messages.success(request, "삭제되었습니다.")

    return HttpResponseRedirect(reverse('boardapp:surveyList'))