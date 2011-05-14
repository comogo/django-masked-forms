$(document).ready(function(){
   $('.masked').each(function(){
       $(this).mask($(this).attr('mask'));
   });
});