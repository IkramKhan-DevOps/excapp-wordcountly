from src.website.models import Content


def get_or_create_website():
    content = Content.objects.all()
    return content[0] if content else Content.objects.create()
