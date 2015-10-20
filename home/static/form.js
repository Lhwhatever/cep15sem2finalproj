setup = function() {

    jQuery.ajaxSettings.traditional = true;

    getCookie = function(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for(i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }

        return cookieValue;
    }

    csrftoken = getCookie('csrftoken');

    csrfSafeMethod = function(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    try {
        $(".datetimepicker").datetimepicker({
            format: 'Y-m-d H:i',
            inline: true
        });
    } catch(err) {
        console.log("skipping date time picker");
    }

    $("label").addClass("col-sm-2 control-label");
    $(".form-group>div>input, .form-group>div>textarea, .form-group>div>select").addClass("form-control");
    $(".form-group>div>input[type=checkbox]").removeClass("form-control").parent().addClass("checkbox");

    $(".form-group>div>input[type=text]").attr("placeholder", "Input text here.");
    $(".form-group>div>.colorpicker-child").parent().removeClass("col-sm-10").addClass("colorpicker col-sm-4");

    $(".form-group>div>textarea").attr("placeholder", "Input text here.");

    try {
        $(".colorpicker>.temp").addClass("input-group-addon");
        $(".colorpicker").attr("placeholder", "Input color hex code.");
        $(".colorpicker").colorpicker();
    } catch(err) {
        console.log("skipping color picker");
    }
}