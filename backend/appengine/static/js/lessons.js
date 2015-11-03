/**
 * Created by Bea on 07/05/2015.
 */
$(document).ready(function() {
    var $ajaxSaveGif = $('#ajax-save-gif');
    $ajaxSaveGif.hide();
    //var $tituloInput = $('#titulo-input');
    //var $descricaoInput = $('#descricao-input');
    var $tituloInput = $("input[name='titulo']");
    var $descricaoInput = $("input[name='descricao']");
    var $temaInput = $("input[name='tema']");
    var tema = document.getElementById('id_tema');
    var $lessonsUl = $('#lessons-ul');
    var listaL = document.getElementById('lessons-ul');

    function addLesson(lesson) {
        var li = '<li id="li-' + lesson.id + '"';
    li = li + '><button id="btn-deletar-' + lesson.id + '"';
    li = li + ' class="btn btn-danger"><i class="glyphicon glyphicon-trash"></i></button>';
    li = li + lesson.titulo + ' - ' + lesson.descricao + '</li>';
        $lessonsUl.append(li);
        $('#btn-deletar-'+lesson.id).click(function() {
			$.post('rest/lessons/deletar', {lesson_id: lesson.id}, function() {
				$('#li-'+lesson.id).remove();
			});
		});
    }

    $.get('/rest/lessons/listar', function(lessons) {
        $.each(lessons, function(i, lesson) {
            addLesson(lesson);
        });
    });

    function obterInputsLicao() {
        return {
            'titulo':$tituloInput.val(),
            'descricao':$descricaoInput.val(),
            'tema': tema.options[tema.selectedIndex].value
        };
    }
    var $salvarBotao = $('#salvar-btn');
    $salvarBotao.click(function() {
        $('div.has-error').removeClass('has-error');
        $('span.help-block').text('');
        $ajaxSaveGif.fadeIn();
        $salvarBotao.attr('disabled','disabled');
        $.post('/rest/lessons/salvar',
            obterInputsLicao(),
            function(lesson) {
                addLesson(lesson);

                $('input.form-control').val('');
            }).error(function(erro){
                var jsonError = erro.responseJSON;
                for(propriedade in jsonError) {
                    $('#'+propriedade+'-div').addClass('has-error');
                    $('#'+propriedade+'-span').text(jsonError[propriedade]);
                }

        }).always(function() {
                $ajaxSaveGif.fadeOut();
                $salvarBotao.removeAttr('disabled');
            });
    });
});