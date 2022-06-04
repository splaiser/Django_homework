from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Topic, Scope


class TopicInlineFormset(BaseInlineFormSet):
    def clean(self):
        main = 0
        for form in self.forms:
            exception = form.cleaned_data
            print(exception)
            if exception != {}:
                if exception['is_main']:
                    main += 1

        if main == 0:
            raise ValidationError('Не указанно ни одного главного раздела')
        elif main > 1:
            raise ValidationError('Указанно больше одного главного раздела')
        else:
            return super().clean()


class TopicInline(admin.TabularInline):
    model = Topic
    formset = TopicInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [TopicInline]


@admin.register(Scope)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name']
