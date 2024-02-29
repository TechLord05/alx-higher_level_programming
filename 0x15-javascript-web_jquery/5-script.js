let add_item = $("#add_item");
let my_list = $(".my_list");
add_item.on("click", function () {
  $("<li>").text("Item").appendTo("ul.my_list");
});
