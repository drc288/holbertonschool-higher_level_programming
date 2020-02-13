#!/usr/bin/node

$.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", (data_json) => {
    $("#hello").text(data_json.hello);
})