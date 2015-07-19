# -*- encoding: utf-8 -*-

from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from .testutil import SuperuserTestCase, UserTestCase, TestCase

from bpp.models.wydawnictwo_ciagle import Wydawnictwo_Ciagle
from bpp.system import groups
from bpp.tests.util import any_ciagle


from bpp.models import Jednostka, Autor, Zrodlo, Wydawnictwo_Zwarte, Praca_Doktorska, Praca_Habilitacyjna, Patent, Charakter_Formalny

from bpp import autocomplete_light_registry # Bez tego następny import się wywali
autocomplete_light_registry # Pycharm, zostaw to w spokoju

from bpp.views.admin import WydawnictwoCiagleTozView


class TestNormalUserAdmin(UserTestCase):
    def test_root(self):
        self.user.is_staff = True
        self.user.is_superuser = False

        for grupa in groups:
            self.user.groups.add(
                Group.objects.get_by_natural_key(grupa)
            )
        self.user.save()

        self.assertContains(
            self.client.get("/admin/"),
            "Administracja", status_code=200)


class TestAdmin(SuperuserTestCase):
    def test_root(self):
        self.assertContains(
            self.client.get("/admin/"),
            "Administracja", status_code=200)

    def test_custom_app_index(self):
        """Spowoduje wywołanie customappindex z django-admin-tools
            """
        self.assertContains(
            self.client.get("/admin/bpp/"),
            "Bpp", status_code=200)

    def test_wyszukiwanie(self):
        """Dla wielu różnych model spróbuj wyszukiwać w tabelce
        i zobacz, czy nie ma błędu."""
        for model in [Jednostka, Autor, Zrodlo, Wydawnictwo_Ciagle,
                      Wydawnictwo_Zwarte, Praca_Doktorska, Praca_Habilitacyjna,
                      Patent, Charakter_Formalny]:
            content_type = ContentType.objects.get_for_model(model)
            url = reverse("admin:%s_%s_changelist" % (
            content_type.app_label, content_type.model))
            res = self.client.get(url, data={"q": "wtf"})
            self.assertEquals(res.status_code, 200)
            pass


class TestAdminViews(TestCase):
    def test_wydawnictwociagletozview(self):
        c1 = any_ciagle()
        self.assertEquals(Wydawnictwo_Ciagle.objects.count(), 1)

        w = WydawnictwoCiagleTozView()
        url = w.get_redirect_url(c1.pk)

        # Czy jest poprawne ID w URLu?
        c2 = Wydawnictwo_Ciagle.objects.all().exclude(pk=c1.pk)
        self.assertIn(str(c2[0].pk), url)

        # Czy stworzył kopię?
        self.assertEquals(Wydawnictwo_Ciagle.objects.count(), 2)
