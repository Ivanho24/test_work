import json
from django.shortcuts import render
from .forms import JSONUploadForm
from .models import JSONData

def upload_json(request):
    if request.method == 'POST':
        form = JSONUploadForm(request.POST, request.FILES)
        if form.is_valid():
            json_file = form.cleaned_data['json_file']
            try:
                data = json.load(json_file)
                for item in data:
                    JSONData.objects.create(
                        name=item['name'],
                        date=item['date']
                    )
                return render(request, 'success.html')
            except json.JSONDecodeError:
                form.add_error('json_file', 'Некорректный формат JSON-файла')
    else:
        form = JSONUploadForm()
    return render(request, 'upload.html', {'form': form})


def show_data(request):
    json_data = JSONData.objects.all()
    return render(request,'show_data.html',{'json_data' : json_data})