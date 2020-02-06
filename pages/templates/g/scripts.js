const app = document.getElementById('root');

const logo = document.createElement('img');
logo.src = 'logo.png';

const container = document.createElement('div');
container.setAttribute('class', 'container');

app.appendChild(logo);
app.appendChild(container);

var request = new XMLHttpRequest();
request.open('GET', 'https://ghibliapi.herokuapp.com/films', true);
request.onload = function () {

  // Begin accessing JSON data here
  var data = JSON.parse(this.response);
  data =[
    {
        "id": 3,
        "firstname": "roy",
        "lastname": "dfs",
        "emp_id": 1
    },
    {
        "id": 4,
        "firstname": "dadf",
        "lastname": "dee",
        "emp_id": 2
    },
    {
        "id": 5,
        "firstname": "hnvb",
        "lastname": "ewreq",
        "emp_id": 3
    },
    {
        "id": 6,
        "firstname": "abfdr",
        "lastname": "liao",
        "emp_id": 4
    }
];
  if (request.status >= 200 && request.status < 400) {
    data.forEach(movie => {
      const card = document.createElement('div');
      card.setAttribute('class', 'card');

      const h1 = document.createElement('h1');
      h1.textContent = movie.firstname;

      const p = document.createElement('p');
      movie.lastname = movie.lastname.substring(0, 300);
      p.textContent = `${movie.lastname}...`;

      container.appendChild(card);
      card.appendChild(h1);
      card.appendChild(p);
    });
  } else {
    const errorMessage = document.createElement('marquee');
    errorMessage.textContent = `Gah, it's not working!`;
    app.appendChild(errorMessage);
  }
}

request.send();