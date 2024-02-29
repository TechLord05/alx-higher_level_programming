$.ajax({
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    method: "GET",
    success: function (data) {
      hello = data.hello;
      console.log(hello);
      $("#hello").text(hello);
    },
  });
