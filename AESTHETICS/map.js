function exitModal() {
  $(".modal").css({"display": "none"})
}

function showModal(topic) {
  $("#" + topic + "_modal").animate({width: "toggle"});
}

function showEnvironmentModal() {
  showModal("environment");
}

function showClimateModal() {
  showModal("climate");
}


function setup() {
  $("#environment_button").click(showEnvironmentModal);
  $("#climate_button").click(showClimateModal);
  $(".close").click(exitModal);
}

$(document).ready(setup)
