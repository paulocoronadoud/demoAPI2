myButton = document.getElementById("btn_enviar");
myButton.addEventListener(
    "click", async function (){

        let mySelection = document.getElementById("localidad");
        let url = "http://127.0.0.1:8000/getjson?localidad="+mySelection.value;
        console.log(url);
        let response = await fetch(url);
        let data= await response.json();
        let myResult = document.getElementById("txt_resultado");
        myResult.innerText= data.mensaje;
    }
)   