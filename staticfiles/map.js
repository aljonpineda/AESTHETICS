function tempStorage() {
  debugger;
  var climate = $("#climate_submission").val();
  var env = $("#issue_submission").val();
}

function exitModal() {
  $(".modal").css({"display": "none"})
}

function showModal(topic) {
  $("#" + topic + "_modal").animate({height: "toggle"});
}

function showIssuesModal() {
  showModal("environment");
}

function showClimateModal() {
  showModal("climate");
}

function handleDocumentClick(event){
    var climateBox = $("#climate_stuff").get(0);
    var issuesBox = $("#environment_stuff").get(0);
    var climateButton = $("#climatebutton").get(0);
    var issuesButton = $("#issuesbutton").get(0);
    if (!climateBox.contains(event.target)&&
        !issuesBox.contains(event.target)&&
        issuesButton != event.target &&
        climateButton != event.target) {
      exitModal();
    }
}

function setup() {
  $("#issuesbutton").click(showIssuesModal);
  $("#climatebutton").click(showClimateModal);
  $(".close").click(exitModal);
  $(document).click(handleDocumentClick);
  $("#ok_button").click(tempStorage);
}


$(document).ready(setup)


function setupTooltips(){
  $(".icon").mouseover(function() {
    $(this).children(".icontext").show();
}).mouseout(function() {
    $(this).children(".icontext").hide();
});
}


$(document).ready(setupTooltips)
