async function login() {
	var uname = document.forms["form"]["uname"].value;
	var upass = document.forms["form"]["upassword"].value;
	if (uname == "" || upass == "") {
		alert("!!! FILL ALL THE FIELDS !!!");
		return false;
	} else {
		var user_check = await eel.log(uname, upass)();
		if (user_check == "0") {
			window.location.href = "main.html";
			return true;
		} else if (user_check == "1") {
			alert("WRONG PASSWORD");
			return false;
		} else if (user_check == "2") {
			alert("WRONG USERNAME");
			document.querySelector('.cont').classList.toggle('s-signup');
			return false;
		} else {
			alert("SOMETHING WENT WRONG");
			return false;
		}
	}
}

async function validateForm() {
	var name = document.forms["Form"]["uname"].value;
	var email = document.forms["Form"]["email"].value;
	var password = document.forms["Form"]["password"].value;
	var city = document.forms["Form"]["city"].value;
	var number = document.forms["Form"]["Phone"].value;

	if (name == "" && email == "" && password == "" && city == "" && number == "") {
		alert("!!! FILL ALL THE FIELDS !!!");
		return false;
	} else if (name == "") {
		alert("FILL THE USERNAME FIELD");
		return false;
	} else if (email == "") {
		alert("FILL EMAIL FIELD");
		return false;
	} else if (password == "") {
		alert("FILL PASSWORD FIELD");
		return false;
	} else if (city == "") {
		alert("FILL CITY FIELD");
		return false;
	} else if (number == "") {
		alert("FILLE NUMBER FIELD");
		return false;
	} else {
		var reg_check = await eel.reg(name, email, password, city, number)();
		if (reg_check == "true") {
			alert("REGISTERED SUCCESSFULLY!!!!!!");
			document.querySelector('.cont').classList.toggle('s-signup');
		} else if (reg_check == "false") {
			alert("Username alredy exists");
		}
	}
	document.getElementById("myForm").reset();
}

document.querySelector('.img-btn').addEventListener('click', function () {
	document.querySelector('.cont').classList.toggle('s-signup')
});