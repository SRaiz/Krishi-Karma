import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render

from apps.ml.cropsyield_classifier import random_forest

from .models import Crop, Yield

crops = Crop.objects.all()
yields = Yield.objects.all()
yield_df = pd.DataFrame.from_records(yields.values())
crops_df = pd.DataFrame.from_records(crops.values())

    
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
        state = request.POST.get('state', False);
        district = request.POST.get('district', False);
        year = request.POST.get('year', False);
        season = request.POST.get('season', False);
        landArea = request.POST.get('landArea', False);
        crop = request.POST.get('crop', False);

        # Filter the dataframe on basis of district state and year to get the rainfall data
        filtered_df = yield_df[ (yield_df.state_name == state) & (yield_df.district_name == district) & (yield_df.crop_year == int(year)) ]

        filtered_df_prod = yield_df[ (yield_df.state_name == state) & (yield_df.district_name == district) & (yield_df.crop_year == int(year)) & (yield_df.crop == crop) ]

        minimum_rainfall = filtered_df['min_rainfall'].unique()[0]
        maximum_rainfall = filtered_df['max_rainfall'].unique()[0]
        average_rainfall = filtered_df['mean_rainfall'].unique()[0]
        total_annual_rainfall = filtered_df['annual_rainfall'].unique()[0]
        production = filtered_df_prod['production'].unique()[0].max()
        crop_yield = (production / float(landArea)).round(3)
        
        # Get the prediction and show it on screen
        input_data = {
            "state_name": state,
            "district_name": district,
            "crop_year": int(year),
            "season": season,
            "crop": crop,
            "area": float(landArea),
            "min_rainfall": minimum_rainfall,
            "max_rainfall": maximum_rainfall,
            "mean_rainfall": average_rainfall,
            "annual_rainfall": total_annual_rainfall,
            "production": production,
            "yield": crop_yield
        }
        rf_alg = random_forest.RandomForestClassifier()
        response = rf_alg.compute_prediction(input_data)
        
        return HttpResponse(response.get('label'))
