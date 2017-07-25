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
  $(document).click(handleDocumentClick);
}

function handleDocumentClick(event){
    var modalBox = $(".modal-content").get(0);
    var climateButton = $("#climatebutton").get(0);
    var issuesButton = $("#issuesbutton").get(0);
    if (!modalBox.contains(event.target)&&
        issuesButton != event.target &&
        climateButton != event.target) {
      exitModal();
    }
}

$(document).ready(setup)
