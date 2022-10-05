let department_select = document.getElementById('id_department');
let city_select = document.getElementById('id_city');

department_select.onchange = function() {

    department = department_select.value;
    fetch('/city/' + department).then(function(response){
        response.json().then(function(data){
        let optionHTML = '';

        for(let city of data.cities){
            optionHTML += '<option value="' + city.id + '">' + city.name + '</option>';
        }

        city_select.innerHTML =  optionHTML;
        });
    });

}

