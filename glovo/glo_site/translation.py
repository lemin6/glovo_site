from .models import UserProfile
from modeltranslation.translator import TranslationOptions,register


@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')