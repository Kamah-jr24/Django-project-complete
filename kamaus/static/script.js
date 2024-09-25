function openChat() {
      document.getElementById("chat-popup").style.display = "block";
  }
  
  function closeChat() {
      document.getElementById("chat-popup").style.display = "none";
  }
  
  function sendMessage() {
      var message = document.getElementById("message-input").value;
      document.getElementById("chat-box").value += "You: " + message + "\n";
      document.getElementById("message-input").value = "";
  }
