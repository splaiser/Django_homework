from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class TagInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            form.cleaned_data
            raise ValidationError('Тут всегда ошибка')
        return super().clean()


class TagInline(admin.TabularInline):
    model = Tag
    formset = TagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [TagInline]



