/*
    This js file is used to call the views.py method from index.html.
*/
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

function filterCrops(selectedState, selectedDistrict) {
    var state = selectedState.value;
    var district = selectedDistrict.value;
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