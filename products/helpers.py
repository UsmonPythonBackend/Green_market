from django.db import models

class StatusChoices(models.TextChoices):
    PUBLISH = 'pb', 'Publish'
    DRAFT = 'df', 'Draft'

class MassaChoices(models.TextChoices):
    KG = 'kg', 'Kg'
    MG = 'mg', 'Mg'
    LG = 'lg', 'Lg'
    PC = 'pc', 'Piece'


class Pagination():
    @staticmethod
    def page_pagination(queryset: list, page_size: int, page: int):
        """
        queryset: data
        page_size: har bitta sahifada nechtadanligi
        page: sahifa tartibi
        """
        return queryset[page_size * (page - 1):page_size * page]






