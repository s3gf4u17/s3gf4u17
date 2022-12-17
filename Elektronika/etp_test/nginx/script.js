var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('stdout')
                var message = document.createElement('span')
                var content = document.createTextNode(event.data)
                var br = document.createElement("br")
                message.appendChild(content)
                messages.appendChild(message)
                messages.appendChild(br)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }