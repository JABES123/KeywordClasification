(function(){

    
    var ButtonSavePin = document.querySelector("#save-pin-button");
    var ButtonCreateField = document.querySelector("#addRow");
    
    var counterField = 0;
    var previusField = 0;

  
    if(ButtonCreateField != null){
        ButtonCreateField.addEventListener('click', function(){
            createDinamicField();
            
            $('#contentLoader').html('<div class="loading"><img src="../img/loadingspinner.gif" alt="loading" /><br/>Un momento, por favor...</div>');
        })
    }
 
    

    
   
    

    var inputKeywordId = null;
    function createDinamicField(){
        var previousInputKeywordId = null;
        if(previusField< counterField){
            previousInputKeywordId = "keywordId"+previusField++
        }

        inputKeywordId ="keywordId"+counterField++;
        var html = '';
        html += '<div id="inputFormRow" class="dropable">';
        html += '<div class="input-group mb-3">';
        html += '<input id="'+inputKeywordId+'" type="text" name="title[]" class="form-control m-input" placeholder="Enter keyword to predict" autocomplete="off">';
        html += '</div>';
       //var dinamicInput = inputKeywordId.includes(1) ? "keywordId" : inputKeywordId
       if(previousInputKeywordId != null){
        var valueInput = $("#"+inputKeywordId+"").val();
        var valuePreviousInput = $("#"+previousInputKeywordId+"").val();

        if(valuePreviousInput == ""){
            $("#modalKeyWord").modal('show');
        }else{
            $('#newRow').append(html);

            var url = 'https://example.com/profile';

           
            //REST
            var RequestUrl  = 'http://localhost:5001/keyword/predict';
            //showInfoMessage("Getting markups");
            var keyword = $("#"+previousInputKeywordId+"").val()
            var mapRequest =  {'keyword':keyword}
            //JSON.stringify(mapRequest)
        

            $.ajax({
                url: RequestUrl,
                data: JSON.stringify(mapRequest),
                type: 'POST',
                dataType: 'json',
                contentType: 'application/json; charset=utf-8',
                crossDomain: true,
                headers:{
                    "accept": 'application/json',
                    "Acces-Control-Request-Origin": "x-requested-with"
                }
            }).done(function(result){
                if(result.status == 'success'){
                    var html2 = ''
                    html2 += '<div>'
                    html2 += "<span style='color: red;'>"+keyword+"</span> predicted with a: <span style='color: red;'>"+result.data.probability+"</span> belong to category <span style='color: red;'>"+result.data.category+"</span> "
                    html2 += '</div>'
                     $(".contentResult").append(html2)
                     $('#contentLoader').html("")
                    //showSuccessMessage(result.message);
                }else{
                    //showErrorMessage(result.message)
                }
            }).fail(function(error){
                //showErrorMessage(error);
                var html2 = ''
                html2 += '<div>'
                html2 += error.data
                html2 += '</div>'
                 $(".contentResult").append(html2)
            }).always(function () {
                //hideInfoMessage();
            });

           
        }
       }else{
        $('#newRow').append(html);
       }
        
    }

    $(document).on('click', '#removeRow', function () {
        alert("llega");
        $(this).closest(".dropable").remove();
    });

    

   /*
    function getMarkups(currentEsceneId){
        var RequestUrl  = ApiURL+'/'+currentEsceneId+'/markups/list';
        //showInfoMessage("Getting markups");
        $.ajax({
            url: RequestUrl,
            data: {'panoramaId':currentEsceneId},
            type: 'POST',
            dataType: 'json',
            traditional: true
        }).done(function(result){
            if(result.status == true){
                loadHostPot(result.data);
                //showSuccessMessage(result.message);
            }else{
                //showErrorMessage(result.message)
            }
        }).fail(function(error){
            //showErrorMessage(error);
        }).always(function () {
            //hideInfoMessage();
        });
    } 
    */
    
})();

