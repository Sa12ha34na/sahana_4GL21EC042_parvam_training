const form = document.getElementById("registration_form");
// form.style.backgroundColor = "lightyellow";
// form.style.backgroundImage = URL("..\media\coffee-plantation.jpg");

// Qodo Gen: Options|Test this function 
function validateForm(event){
    event.preventDefault();

    const studentName = document.getElementById("student_name");
    const nameError = document.getElementsByClassName("name_error");
    
    if(studentName.value == ''){
        studentName.style.border = "2px solid red";
        nameError[0].textContent = "Name cannot be empty!";
    }   
}
// studentName.style.border = "2px solid red";