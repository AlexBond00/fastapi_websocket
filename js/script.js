var ws = new WebSocket("ws://localhost:8000/api/v1/ws");
ws.onmessage = function(event) {
    var messages = document.getElementById('messages')
    var message = document.createElement('li')
    var dataFromJson = JSON.parse(event.data)
    let dataString = dataFromJson.id + '.'+ ' ' + " - " + dataFromJson.message
    var content = document.createTextNode(dataString)
    message.appendChild(content)
    messages.appendChild(message)
};
function sendMessage(event) {
    var input = document.getElementById("messageText")
    if (!input.value){
        alert('Enter your message')
        return false
    }
    ws.send(JSON.stringify({
           'message': input.value
    }))
    input.value = ''
    event.preventDefault()
}
