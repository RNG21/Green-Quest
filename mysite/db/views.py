from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from db.create_db_entries import create_entries

@staff_member_required
def create_db_from_script(request):
    create_entries()
    return render(request, "db/create_entries.html")
