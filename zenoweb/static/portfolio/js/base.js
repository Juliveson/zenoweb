function DisplayNotification(message){
    $('.demo-notice').removeClass('hide')
    $('.notice-text').html(message)
    $('.demo-notice').css({'display': 'flex'})
    setTimeout(function() {
        $('.demo-notice').addClass('hide');
    }, 6000);
}