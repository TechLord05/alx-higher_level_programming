$.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    method: "GET",
    success: function (data) {
      movies = data.results;
      console.log(movies);
      list_movies = $("#list_movies");
      movies.forEach(function (movie) {
        $("<li>").text(movie.title).appendTo("ul#list_movies");
      });
    },
  });
