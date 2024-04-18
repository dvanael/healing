$(document).ready(function() {
  $('[id^=id_password]').each(function() {
    var passwordField = $(this);
    var showPasswordCheckbox = $('<input class="form-check-input ms-1 mt-2" type="checkbox">');
    var showPasswordLabel = $('<label class="form-check-label ms-2 mt-1 opacity-75" for="flexCheckChecked">Mostrar Senha</label>');
    
    showPasswordCheckbox.insertAfter(passwordField);
    showPasswordLabel.insertAfter(showPasswordCheckbox);
    
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