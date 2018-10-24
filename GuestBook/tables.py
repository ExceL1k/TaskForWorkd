from .models import BookGuest
import django_tables2 as table


class BookTable(table.Table):
    class Meta:
        model = BookGuest
        template_name = 'django_tables2/bootstrap4.html'