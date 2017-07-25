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
  $("#issuesbutton").click(showIssuesModal);
  $("#climatebutton").click(showClimateModal);
  $(".close").click(exitModal);
}

$(document).ready(setup)
