$.ajax({
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    method: "GET",
    success: function (data) {
      dan = data.name;
      console.log(dan);
      name_id = $("#character");
      name_id.text(dan);
    },
  });
