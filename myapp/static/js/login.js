function loginUser() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("http://127.0.0.1:1234/api/login/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        credentials: "include",   
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.user_id) {
            localStorage.setItem("user_id", data.user_id); 
            window.location.href = "/courses/";
        } else {
            alert("Invalid login");
        }
    })
    .catch(err => {
        alert("Login error");
    });
}
