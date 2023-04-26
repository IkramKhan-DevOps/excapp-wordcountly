from django.db import models
from django_resized import ResizedImageField
from tinymce import models as tinymce_models


class Content(models.Model):

    name = models.CharField(max_length=100, unique=True, default='Countly', help_text="Name of this application"),
    tagline = models.CharField(
        max_length=255, unique=True, default='Track your writing progress with Countly',
        help_text="Tagline or business line"
    ),
    base_url = models.URLField(
        default='http://127.0.0.1:8000/', unique=True,
        help_text="your application domain (base url) i.e https://example.com/"
    )
    favicon_icon = models.ImageField(
        upload_to='website/content/favicon', null=True, blank=True,
        help_text="upload a favico icon for your application, format must be png or .ico"
    )
    logo = models.ImageField(
        upload_to='website/content/logo', null=True, blank=True,
        help_text="upload a favico icon for your application, format must be png"
    )

    privacy_policy = tinymce_models.HTMLField(null=True, blank=True)
    contact_phone = models.CharField(max_length=15, unique=True, default='+1000000000')
    contact_email = models.EmailField(unique=True, default='support@example.com')
    address = models.CharField(max_length=1000, null=True, blank=True, help_text='Your office or physical address')
    lat = models.FloatField(default=43.000000, help_text="Latitude of your exact location, used for maps")
    long = models.FloatField(default=-75.000000, help_text="Longitude of your exact location, used for maps")

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Website Main Content"

    def __str__(self):
        return self.name


class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return self.name


class BlogTag(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Blog Tags"

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = ResizedImageField(size=[500, 500], crop=['middle', 'center'], upload_to='website/blog/thumbnail')
    category = models.ForeignKey(BlogCategory, null=True, blank=False, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(BlogTag, null=True, blank=True)
    description = models.TextField(null=True, blank=True, help_text="Short description for your blog")

    content = tinymce_models.HTMLField()

    read_time = models.PositiveIntegerField(default=0, help_text="read time in minutes")

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title

