from .models import Tariff
from modeltranslation.translator import translator, TranslationOptions


class TariffTranslate(TranslationOptions):
    fields = ('name',"text")

translator.register(Tariff, TariffTranslate)
