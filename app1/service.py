from .models import MyModel

def model_worker():
    return MyModel.objects.get(id=1).name
