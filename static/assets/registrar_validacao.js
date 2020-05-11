$(document).ready(function(){
        
    $("input#nome").on("keyup", function(){
        if ($(this).val() == '') {
            $(this).removeClass("is-valid").addClass("is-invalid");
        } else {
            $(this).removeClass("is-invalid").addClass("is-valid");
        }
    });

    $("input#sobrenome").on("keyup", function(){
        if ($(this).val() == '') {
            $(this).removeClass("is-valid").addClass("is-invalid");
        } else {
            $(this).removeClass("is-invalid").addClass("is-valid");
        }
    });

    $("input#usuario").on("keyup", function(){
        if ($(this).val().length < $(this).attr("minlength")) {
            $(this).removeClass("is-valid").addClass("is-invalid");
            $("#usuario-feedback").html("Este campo deve conter no mínimo " + $(this).attr("minlength") + " caracteres.")
        } else {
            $(this).removeClass("is-invalid").addClass("is-valid");
        }
    });        

    $("input#senha").on("keyup", function(){
        if ($(this).val().length < $(this).attr("minlength")) {
            $(this).removeClass("is-valid").addClass("is-invalid");
            $("#senha-feedback").html("Este campo deve conter no mínimo " + $(this).attr("minlength") + " caracteres (letras e números).")
        } else {
            $(this).removeClass("is-invalid").addClass("is-valid");
        }
    });
    
    $("input#senha_repetida").on("keyup", function(){
        if ($(this).val().length < $(this).attr("minlength")) {
            $(this).removeClass("is-valid").addClass("is-invalid");
        } else {
            $(this).removeClass("is-invalid").addClass("is-valid");
        }
    });              
  
});