window.$(document).ready(function () {
  const i = 'https://swapi-api.hbtn.io/api/films/?format=json';
  window.$.get(i, function (data) {
    const f = data.results;
    for (const k in f) {
      window.$('#list_movies').append(`<li>${f[k].title}</li>`);
    }
  });
});
