$('document').ready(function () {
  $('div#add_item').on('click', () => {
    $('ul.my_list').add('<li>Item</li>').appendTo('ul.my_list');
  });

  $('div#remove_item').on('click', () => {
    $('ul.my_list li:last-child').remove();
  });

  $('div#clear_list').on('click', () => {
    $('ul.my_list').html('');
  });
});
