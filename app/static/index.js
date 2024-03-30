var helptext = document.querySelectorAll('.helptext');
var li = document.querySelectorAll('li');
var label= document.querySelectorAll('label');
var input= document.querySelectorAll('input');

var elements = [];
elements = elements.concat(Array.from(helptext));
elements = elements.concat(Array.from(li));

elements.forEach(function(element) {
    element.style.display = 'block';
    element.innerHTML='';
});
label.forEach((label)=>{
  label.classList="sr-only"
})
input.forEach((input)=>{
  input.classList="form-control"
})
document.querySelector('#id_username').placeholder = 'Enter your username';
document.querySelector('#id_first_name').placeholder = 'Enter your first name';
document.querySelector('#id_last_name').placeholder = 'Enter your last name';
document.querySelector('#id_date_of_birth').placeholder = 'YYYY-MMM-DDD';
document.querySelector('#id_email').placeholder = 'Enter your email';
document.querySelector('#id_password').placeholder = 'Enter your password';
document.querySelector('#id_password1').placeholder = 'Enter your password';
document.querySelector('#id_password2').placeholder = 'Confirm your password';