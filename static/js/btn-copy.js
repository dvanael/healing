$(document).ready(function() {
  $('.btn-copy').click(function() {
    // Seleciona o valor do input com o ID 'id_link'
    var linkValue = $('#id_link').val();

    // Cria um elemento temporário para copiar o valor
    var tempInput = $('<input>');
    $('body').append(tempInput);
    tempInput.val(linkValue).select();
    document.execCommand('copy');
    tempInput.remove();

    $(this).html($('<div><i class="bi bi-check-lg me-2"></i> Copiado</div>'));
    setTimeout(function() {
      $('.btn-copy').html('Copiar Link');
    }, 2000);
  });
});