import pytest


class TestTemplateView:
    @pytest.mark.django_db(transaction=True)
    def test_view_polls(self, client):
        urls = ['/polls/', ]
        for url in urls:
            try:
                response = client.get(url)
            except Exception as e:
                assert False, f'''Страница `{url}` работает неправильно. Ошибка: `{e}`'''
            assert response.status_code != 404, (
                f'Страница `{url}` не найдена, проверьте этот адрес в *urls.py*'
            )

            assert response.status_code == 200, (
                f'Ошибка {response.status_code} при открытиии `{url}`. Проверьте ее view-функцию'
            )
            assert response.content == b"Hello, world. You're at the polls index.", (
                f'Ошибка {response.content} при открытиии `{url}`. Проверьте ее view-функцию'
            )
