function consultUser(){
    //Capturar ID
    let idUser = document.getElementById("id").value;
    let obj_user = {"id": idUser}
    
    fetch("/consult_user", {
        "method": "post",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify(obj_user)
    })
    
    .then(resp => resp.json())
    .then(data => {
        alert(data.status)
    })
    .catch(err => {
        alert("Error" + err)
    })
}