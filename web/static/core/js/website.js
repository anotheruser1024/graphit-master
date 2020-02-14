/* Display file name after using Browse button */
$('.custom-file-input').change(function (e) {
    var files = [];
    for (var i = 0; i < $(this)[0].files.length; i++) {
        files.push($(this)[0].files[i].name);
    }
    $(this).next('.custom-file-label').text(files.join(', '));
});

/* Check if valid extension */
var _validFileExtensions = ['.gml', '.txt'];
function ValidateExtension(oForm) {
    // Get all inputsa
    var arrInputs = oForm.getElementsByTagName("input");
    // for each input do:
    for (var i = 0; i < arrInputs.length; i++) {
        // select a single input from the array
        var oInput = arrInputs[i];
        // check if input type is file
        if (oInput.type == "file") {
            // get file name from the input
            var sFileName = oInput.value;
            if (sFileName.length > 0) {
                var blnValid = false;
                for (var j = 0; j < _validFileExtensions.length; j++) {
                    var sCurExtension = _validFileExtensions[j];
                    if (sFileName.substr(sFileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
                        blnValid = true;
                        break;
                    }
                }

                if (!blnValid) {
                    alert("Sorry, " + sFileName + " is invalid, allowed extensions are: " + _validFileExtensions.join(", "));
                    return false;
                }
            }
        }
    }

    return true;
}
