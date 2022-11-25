from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import DocumentForm
from .models import Document, ConstructionMaterial

import pandas as pd
from sqlalchemy import create_engine


def upload_csv(request):
    """
    Загрузка файла в модель Document.
    """
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/success/")
    else:
        form = DocumentForm()
    return render(request, 'main_app/upload.html', {'form': form})


def parsing_request(request):
    """
    Вывод шаблона с полями для ввода запроса на парсинг.
    """
    last_file = Document.objects.last()
    fields = [f.verbose_name for f in ConstructionMaterial._meta.get_fields()]
    return render(request, 'main_app/parser.html', {'document': last_file, 'fields': fields[1:]})


def parsing_result(request):
    """
    Получение запрашиваемой в парсинге информации, чтение последнего загруженного .csv файла через pandas.
    """
    searching_field = request.POST.getlist("searching_field")
    fields = [f.verbose_name for f in ConstructionMaterial._meta.get_fields()]
    fields = fields[1:]
    current_search = {fields[i]: searching_field[i] for i in range(len(fields)) if searching_field[i] != ''}

    def search_df(length, **kwargs):
        """
        Поиск побитового соответствия запрашиваемого поля в dataframe pandas.
        """
        latest_csv = Document.objects.latest('file')
        df = pd.read_csv(latest_csv.file.path, sep=';', engine='python', quoting=3, error_bad_lines=False)
        if length == 0:
            res = "Необходимо выбрать хотя бы одно поле для поиска"
        else:
            for key, value in kwargs.items():
                res = df[df[key].astype(str).str.contains(value, na=False)]  # Доработать множественный поиск
        return res

    global result
    result = search_df(len(current_search), **current_search)
    result_html = result.to_html()

    return render(request, 'main_app/parser_result.html', {'result_html': result_html, 'result': result})


def save_to_db(request):
    """
    Сохранение информации которую удалось спарсить в модель ConstructionMaterial.
    """
    if request.method == 'GET':
        # result = request.GET["result"]
        print(type(result))
        engine = create_engine('sqlite:///db.sqlite3')
        result.to_sql(ConstructionMaterial._meta.db_table, if_exists='append', con=engine, index=False)
        context = {"success": "Данная выборка успешно сохранена"}
    # return HttpResponse("Данная выборка успешно сохранена")
    return render(request, 'main_app/parser_result.html', context)
