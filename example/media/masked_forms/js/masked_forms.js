$(document).ready(function(){
   $('input.masked').each(function(){
       $(this).mask($(this).attr('mask'));
   });
});
