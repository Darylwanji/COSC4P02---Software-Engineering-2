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

const trigger = [ //Temp User statements
    //0 
    ["hi", "hey", "hello"],
    //1
    ["how are you", "how are things"],
    //2
    ["what is going on", "what is up"],
    //3
    ["happy", "good", "well", "fantastic", "cool"],
    //4
    ["bad", "bored", "tired", "sad"],
    //5
    ["tell me story", "tell me joke"],
    //6
    ["thanks", "thank you"],
    //7
    ["bye", "good bye", "goodbye"]
];

const reply = [ //Temp bot responses
    //0 
    ["Hello!", "Hi!", "Hey!", "Hi there!"], 
    //1
    [
        "Fine... how are you?",
        "Pretty well, how are you?",
        "Fantastic, how are you?"
        ],
    //2
    [
        "Nothing much",
        "Exciting things!"
        ],
    //3
    ["Glad to hear it"],
    //4
    ["Why?", "Cheer up buddy"],
    //5
    ["What about?", "Once upon a time..."],
    //6
    ["You're welcome", "No problem"],
    //7
    ["Goodbye", "See you later"],
];

const alternative = [ //Temp alternative replies
    "Same",
    "Go on...",
    "Try again",
    "I'm listening...",
    "Bro..."
];

function output(input) { //Temporary for testing the interface, simply filters the input for a response
    let response;
    //remove all characters except word characters, space, and digits
    let text = (input.toLowerCase()).replace(/[^\w\s\d]/gi, "");

    // 'tell me a story' -> 'tell me story'
    // 'i feel happy' -> 'happy'
    text = text
    .replace(/ a /g, " ")
    .replace(/i feel /g, "")
    .replace(/whats/g, "what is")
    .replace(/please /g, "")
    .replace(/ please/g, "");

    //compare arrays
    //then search keyword
    //then random alternative

    if (compare(trigger, reply, text)) { //Temp condition for response
        response = compare(trigger, reply, text);
    } else {
        response = alternative[Math.floor(Math.random() * alternative.length)];
    }

    addChat(input, response); //Updates the chatbox with the input and response

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

function compare(triggerArray, replyArray, text) { //Temporary pair input with response
    let item;
    for (let x = 0; x < triggerArray.length; x++) {
        for (let y = 0; y < replyArray.length; y++) {
            if (triggerArray[x][y] == text) {
                items = replyArray[x];
                item = items[Math.floor(Math.random() * items.length)];
            }
        }
    }
    return item;
}