#!/usr/bin/node
const request = require('request');

function fetchCharacters (movieId) {
  request.get(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, { json: true }, async (err, res, body) => {
    if (err) console.log(err);
    for (const character of body.characters) {
      request.get(character, { json: true }, (error, res, body) => {
        if (error) console.log(error);
        console.log(body.name);
      });
      await new Promise((resolve) => setTimeout(resolve, 200));
    }
  });
}

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a movie ID (e.g., 3 for "Return of the Jedi").');
} else {
  fetchCharacters(movieId);
}
