#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  if (response.statusCode !== 200) {
    console.error('Invalid');
  } else {
    console.log(JSON.parse(body).title);
  }
});
