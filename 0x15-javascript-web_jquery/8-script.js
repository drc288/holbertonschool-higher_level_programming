#!/usr/bin/node

$.getJSON('https://swapi.co/api/films/?format=json', (data_json) => {
  $.each(data_json.results, (idx, value) => {
    $('UL#list_movies').append(`<li>${value.title}</li>`);
  });
});
