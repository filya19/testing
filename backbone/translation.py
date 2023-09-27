from modeltranslation.translator import translator, TranslationOptions
from .models import Student


# for Student model
class StudentTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'patronymic', 'accused', 'judgment', 'description', 'status')


translator.register(Student, StudentTranslationOptions)
