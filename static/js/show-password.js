$(document).ready(function() {
  $('[id^=id_password]').each(function(index) {
    var passwordField = $(this);
    var showPasswordDiv = $('<div class="show-password aling-center"></div>')
    var showPasswordCheckbox = $('<input class="form-check-input pointer" type="checkbox" id="showPassword'+index+'">');
    var showPasswordLabel = $('<label class="form-check-label pointer mx-2" for="showPassword'+index+'">Mostrar Senha</label>');
    
    showPasswordDiv.insertAfter(passwordField);
    showPasswordDiv.append(showPasswordCheckbox);
    showPasswordDiv.append(showPasswordLabel);
    
    showPasswordCheckbox.change(function() {
      var isChecked = $(this).prop('checked');
      if (isChecked) {
          passwordField.attr('type', 'text');
      } else {
          passwordField.attr('type', 'password');
      }
    });
  });
});