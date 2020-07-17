/*
    This js file is used to call the views.py method from index.html.
*/

$(document).ready(function() {
    $('.actionBar .buttonFinish')[0].innerText = 'Predict';
    $(".actionBar .buttonFinish").removeClass("buttonFinish buttonDisabled btn btn-default").addClass("buttonFinish buttonDisabled btn btn-success");
    $(".actionBar .buttonNext").removeClass("btn-success" ).addClass("btn-warning");

    //-- Predict Values by passing through a function --//
    $('.actionBar .buttonFinish').click(function(){
        predictValues();
    });
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
            for(var district of districts.split(',')) {
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
                    cropsToHide.push(crop);
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

function predictValues () {
    var state = $('#selectedState').val();
    var district = $('#district-select').val();
    var year = $('#year-select').val();
    var season = $('#season-select').val();
    var landArea = $('#land-area').val();
    var crop = $('#selected-crop').val();
    //-- Pass this selected values to the views.py method using ajax --//
    $.ajax({
        type: "POST",
        url: "/home/predict",
        data: {
            state: state,
            district: district,
            year: year,
            season: season,
            landArea: landArea,
            crop: crop,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (yeild_status) {
            alert(yeild_status);
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