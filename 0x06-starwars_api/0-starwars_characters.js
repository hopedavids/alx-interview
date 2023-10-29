const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: node 0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

const swapiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(swapiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status Code:', response.statusCode);
  } else {
    try {
      const film = JSON.parse(body);
      const characters = film.characters;

      if (characters.length === 0) {
        console.log('No characters found for this movie.');
      } else {
        characters.forEach((characterUrl) => {
          request(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
              console.error('Error:', charError);
            } else if (charResponse.statusCode !== 200) {
              console.error('Status Code:', charResponse.statusCode);
            } else {
              const character = JSON.parse(charBody);
              console.log(character.name);
            }
          });
        });
      }
    } catch (parseError) {
      console.error('Error parsing response:', parseError);
    }
  }
});
