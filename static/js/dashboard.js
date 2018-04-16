
$('#exampleModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var recipient = button.data('whatever') // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var arr = ['Salary','Refunds','Business','Pension','Bonus','Other'];
  var modal = $(this)
  modal.find('.modal-title').text(recipient)
  if (jQuery.inArray(recipient, arr) > -1) {
  	modal.find('.name-of-expense').hide();
  	modal.find('#main-form').attr('action','/addExpense/Income/'+recipient);
  }
  else {
  	modal.find('.name-of-expense').show();
    // modal.find('.exp').hide();
    modal.find('.exp').attr('hidden','hidden');
    cls = '.' + recipient.toLowerCase();
    // modal.find(cls).show();
    modal.find(cls).removeAttr('hidden');
    // value = $(cls).val()
    // console.log(value)
  	modal.find('#main-form').attr('action','/addExpense/'+recipient);
  }

  // modal.find('.exp').hide();
  // cls = '.' + recipient.toLowerCase();
  // modal.find(cls).show();
  
  // console.log(cls);
  // modal.find('.modal-body input').val(recipient)
})