myButton = document.getElementById("btn_enviar");
myButton.addEventListener(
    "click", async function (){

        let response = await fetch("http://127.0.0.1:8000/");
        let data= await response.json();

        myResult = document.getElementById("txt_resultado");
        myResult.innerText= data;
    }
)   