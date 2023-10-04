$('div#add_item').on('click', () => {
  $('ul.my_list').add('<li>Item</li>').appendTo('ul.my_list');
})