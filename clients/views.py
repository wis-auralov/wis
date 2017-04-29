from io import BytesIO

from django.core.exceptions import FieldError
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView

from xlsxwriter.workbook import Workbook

from clients.models import Client


class ClientList(ListView):
    model = Client
    template_name = "clients/client_list.html"
    ordering = 'first_name'

    def get_queryset(self):
        qs = super(ClientList, self).get_queryset()

        keyword = self.request.GET.get('keyword', '').strip()
        if keyword:
            qs = qs.filter(Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword))

        order_by = self.request.GET.get('order_by', '').strip()
        if order_by:
            try:
                qs = qs.order_by(order_by)
            except FieldError:
                pass
        return qs


class ClientDetail(DetailView):
    model = Client
    template_name = "clients/client_detail.html"


class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')


class ClientCreate(CreateView):
    model = Client
    fields = ['first_name', 'last_name', 'birth_date', 'image_url']
    template_name = "clients/client_create.html"
    success_url = reverse_lazy('client_list')


class ClientScores(TemplateView):
    template_name = "clients/client_scores.html"


def download_xlsx(request):
    rows = tuple(Client.objects.values_list())
    output = BytesIO()

    book = Workbook(output)
    sheet = book.add_worksheet('test')
    headers = (
        'id', 'first_name', 'last_name', 'birth_date', 'image_url', 'score'
    )
    for col_num in range(len(headers)):
        sheet.write(0, col_num, headers[col_num])
    for row_num, row in enumerate(rows, start=1):
        for col_num in range(len(row)):
            sheet.write(row_num, col_num, row[col_num])
    book.close()

    output.seek(0)
    response = HttpResponse(output.read(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=test.xlsx"

    return response
