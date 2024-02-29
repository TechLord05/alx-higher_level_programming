let toggle_header = $("#toggle_header");
let header = $("header");
toggle_header.on("click", function () {
  if (header.hasClass("red")) {
    header.removeClass("red").addClass("green");
  } else {
    header.removeClass("green").addClass("red");
  }
});
