function exitModal() {
  $(".modal").css({"display": 'none'})
}

function showModal() {
  $(".modal").animate({width: 'toggle'});
}

function Modal() {
  $("#myBtn").click(showModal);
  $(".close").click(exitModal);
}

$(document).ready(Modal)




$(document).ready(setupHandlers)
