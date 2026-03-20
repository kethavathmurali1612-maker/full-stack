fetch("http://localhost:5000/student-details")
.then(res => res.json())
.then(data => {
  document.getElementById("name").innerText = data.name;
  document.getElementById("roll").innerText = data.roll;
  document.getElementById("reg").innerText = data.register;
})
.catch(err => console.log(err));
