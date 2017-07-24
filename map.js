function exitModal() {
  $(".modal").css({"display": "none"})
}

function showModal(topic) {
  $("#" + topic + "_modal").animate({width: "toggle"});
}

function showIssuesModal() {
  showModal("environment");
}

function showClimateModal() {
  showModal("climate");
}


function setup() {
  $("#issues_button").click(showIssuesModal);
  $("#climate_button").click(showClimateModal);
  $(".close").click(exitModal);
}

$(document).ready(setup)
