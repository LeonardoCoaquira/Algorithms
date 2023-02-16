const but = document.getElementById("boton");
const div = document.getElementById("result");

div.addEventListener('click', () => {
  const num = 42;
  fetch(`http://127.0.0.1:8080/table/${num}`)
    .then(response => response.text())
    .then(data => {
      fetchResult.innerHTML = data;
    });
});
  