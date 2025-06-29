from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path

urlpatterns = [
    path("", include("arches.urls")),
    path("", include("arches_for_science.urls")),
    path("", include("arches_her.urls")),
    path("reports/", include("arches_templating.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Only handle i18n routing in active project. This will still handle the routes provided by Arches core and Arches applications,
# but handling i18n routes in multiple places causes application errors.
if settings.ROOT_URLCONF == __name__:
    if settings.SHOW_LANGUAGE_SWITCH is True:
        urlpatterns = i18n_patterns(*urlpatterns)

    urlpatterns.append(path("i18n/", include("django.conf.urls.i18n")))

if settings.DEBUG:
    from django.contrib.staticfiles import views
    from django.urls import re_path
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$$', views.serve),
    ]
