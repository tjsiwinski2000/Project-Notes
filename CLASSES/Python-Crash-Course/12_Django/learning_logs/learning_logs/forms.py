from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model  = Topic
        fields = ['text'] #blank label
        labels = {'text' :''}

class EntryForm(forms.ModelForm):
    class Meta:
        model  = Entry
        fields = ['text']
        labels = {'text' :''} #blank label
        widgets = {'text': forms.Textarea(attrs= {'cols':80})}