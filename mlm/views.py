from django.http import JsonResponse
from .model_handler import model
import json

def predict_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        input_data = data.get('data', None)

        if input_data:
            # Use the loaded model to make predictions
            prediction = model.predict(input_data)
            return JsonResponse({'prediction': prediction.tolist()})
        else:
            return JsonResponse({'error': 'Invalid input data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
