import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render

from .models import Crop, Yield

crops = Crop.objects.all()
yields = Yield.objects.all()
yield_df = pd.DataFrame.from_records(yields.values())
crops_df = pd.DataFrame.from_records(crops.values())
prediction_model_ready = False

    
def index(request):
    data_sd = values_for_homepage(yield_df)
    
    return render(request, 'index.html', {
        'crops': crops,
        'states': data_sd
    })

'''
    This method is returning the states and districts to be shown on the homepage.
'''
def values_for_homepage(yield_df):
    return yield_df['state_name'].unique()


def filter_districts(request):
    if request.method == 'POST':
        state = request.POST['state']
        filtered_df = yield_df[yield_df.state_name == state]
        uniq_dist = filtered_df['district_name'].unique()
        districts_string = ','.join(map(str, uniq_dist))
        
        return HttpResponse(districts_string)


def filter_crops(request):
    if request.method == 'POST':
        state = request.POST['state']
        district = request.POST['district']
        filtered_df = yield_df[ (yield_df.state_name == state) & (yield_df.district_name == district) ]
        uniq_crops = filtered_df['crop'].unique()
        crops_string = ','.join(map(str, uniq_crops))

        # Get all crops and also send it for comparison and hiding
        all_crops = crops_df['name'].unique()
        all_crops_string = ','.join(map(str, all_crops))
        string_to_send = all_crops_string + '====' + crops_string
        
        return HttpResponse(string_to_send);


def predict_yield(request):
    if request.method == 'POST':
        state = request.POST['state']
