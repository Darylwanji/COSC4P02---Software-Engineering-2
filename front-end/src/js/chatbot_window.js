document.addEventListener("DOMContentLoaded", () => { //Wait for html to load
    const inputField = document.getElementById("input"); // get the input field
    document.getElementById("submitButton").onclick = function(){ //run submit function when arrow is pressed
        submit();
    }
    inputField.addEventListener("keydown", function(e) { //If enter key is pressed and input field is active run submit function
        if (e.code === "Enter") {
            submit();
        }
    });
});

function submit(){
    let input = document.getElementById("input").value; //get input field
    if(input!=''){ //Submit if user has typed something
        output(input);
    }
}

function output(input) { //Will recieve answer from back-end based on input
    var API_URL = 'https://4r6bkh99fk.execute-api.us-east-2.amazonaws.com/dev/chat';
	$(document).ready(function(){
		$.ajax({
			type: 'GET',
			url: API_URL,
			success: function(data){
				addChat(input, data); //Updates the chatbox with the input and response
			}
		});
	});

    document.getElementById("input").value = ""; //Clears the input box
}

function addChat(input, response) {
    const chatDiv = document.getElementById("chatBox"); //Get chatbox element
    let userDiv = document.createElement("div"); //build a container for the chat bubble
    let userText = document.createElement("div");//build the chat bubble
    userDiv.id = "user"; //user chat bubble container id
    userDiv.className = "chatContainer"; //chat bubble container class
    userText.id = "userText"; //user chat bubble id
    userText.className = "bubble"; //chat bubble class
    userText.innerHTML = `<span class="message"><b>You:</b></span> ${input}`; //Insert user input into chat bubble
    userDiv.appendChild(userText); //insert chat bubble into container
    chatDiv.appendChild(userDiv); //insert chat bubble container into chat box
    chatDiv.scrollTop = chatDiv.scrollHeight; //scroll to the bottom of chat box

    let botDiv = document.createElement("div"); //Similar to user chat bubble but for bot response
    let botText = document.createElement("div");
    botDiv.id = "bot";
    botDiv.className = "chatContainer";
    botText.id = "botText";
    botText.className = "bubble";
    botText.innerHTML = `<span class="message"><b>MoBi:</b></span> ${response}`; //Insert bot response
    botDiv.appendChild(botText);
    
    setTimeout(function(){ //Wait effect for bot response to show
        chatDiv.appendChild(botDiv);
        chatDiv.scrollTop = chatDiv.scrollHeight;
    }, 1000);
}