window.$(document).ready(function () {
  const i = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  window.$.get(i, function (data) {
    window.$('#character').text(data.name);
  });
});
