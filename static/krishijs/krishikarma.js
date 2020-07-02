/*
    This js file is used to call the views.py method from index.html.
*/

$(document).ready(function() {
    $('.actionBar .buttonFinish')[0].innerText = 'Predict';
    $(".actionBar .buttonFinish").removeClass("buttonFinish buttonDisabled btn btn-default").addClass("buttonFinish buttonDisabled btn btn-success");
    $(".actionBar .buttonNext").removeClass("btn-success" ).addClass("btn-warning");

    //-- Predict Values by passing through a function --//
    $('.actionBar .buttonFinish').click(function(){
        var stateValue = $('#selectedState').val();
        var districtValue = $('#district-selec').val();
        var yearValue = $('#year-select').val();
        var seasonValue = $('#season-select').val();
        var landAreaValue = $('#land-area').val();
        var cropValue = $('#selected-crop').val;
        
        predictValues( stateValue, districtValue, yearValue, seasonValue, landAreaValue, cropValue );
    })
});

function filterDistricts(selectedState) {
    var state = selectedState.value;
    //-- Pass this selected state value to the views.py method using ajax --//
    $.ajax({
        type: "POST",
        url: "/home/state",
        data: {
            state: state,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (districts) {
            for(district of districts.split(',')) {
                $('#district-select').append(
                    new Option( text = district, value = district )
                );
            }
        }
    });
}

function filterCrops(selectedDistrict) {
    var state = $('#selectedState').val();
    var district = selectedDistrict.value;
    //-- Pass this selected state value to the views.py method using ajax --//
    $.ajax({
        type: "POST",
        url: "/home/state/district",
        data: {
            state: state,
            district: district,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (data_to_page) {

            var allCropsDiv = $('#all_crops > div');
            var allCropsList = data_to_page.split('====')[0].split(',');
            var desiredCrops = data_to_page.split('====')[1].split(',');
            var cropsToHide = [];

            //-- Make all the fruits visible for start of method --//
            for ( i = 0; i < allCropsDiv.length; i++ ) {
                if (allCropsDiv[i].style.display === 'none') {
                    allCropsDiv[i].style.display = '';
                }
            }
            
            allCropsList.forEach(crop => {
                if ( desiredCrops.indexOf(crop) === -1 ) {
                    cropsToHide.push(crop)
                }
            });

            //-- Remove hide all the crops which are not present --//
            for ( i = 0; i < allCropsDiv.length; i++ ) {
                if (cropsToHide.indexOf(allCropsDiv[i].id) !== -1) {
                    allCropsDiv[i].style.display = 'none';
                }
            }
        }
    });
}

function predictValues ( stateValue, districtValue, yearValue, seasonValue, landAreaValue, cropValue ) {
    //-- Pass this selected values to the views.py method using ajax --//
    $.ajax({
        type: "POST",
        url: "/home/predict",
        data: {
            state: stateValue,
            district: districtValue,
            year: yearValue,
            season: seasonValue,
            land: landAreaValue,
            crop: cropValue,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (districts) {
            
        }
    });
}

function setSelectedCrop(selectedCrop) {
    $('#selected-crop').val(selectedCrop);
    new PNotify({
        title: 'You Selected '+selectedCrop,
        type: 'success',
        styling: 'bootstrap3'
    });
    $('.actionBar .buttonFinish').removeClass("buttonFinish buttonDisabled btn btn-default").addClass("buttonFinish btn btn-success");
}