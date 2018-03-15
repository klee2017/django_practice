from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # field = '__all__'
        fields = ['title', 'content']

    # title = forms.CharField(validators=[min_length_3_validator])
    # content = forms.CharField(widget=forms.Textarea)

    '''
    그냥 폼일 경우
    def save(self, commit=True):
        post = Post.objects.create(**self.cleaned_data)
        if commit:
            post.save()
        return post
        
    모델폼일 경우 모델 인스턴스를 내부적으로 유지하고 있어 save를 지원
    def save(self, commit=True):
        self.instance = Post.objects.create(**self.cleaned_data)
        if commit:
            self.instance.save()
        return self.instance
    
    '''
