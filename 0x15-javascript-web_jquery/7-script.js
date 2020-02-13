#!/usr/bin/node

$.getJSON("https://swapi.co/api/people/5/?format=json", (data_json) => {
    $("#character").text(data_json.name);
})