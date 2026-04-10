const textarea = document.querySelector("textarea");
const sendBtn = document.querySelector(".send-btn");
const messages = document.querySelector(".messages");
const typing = document.querySelector(".typing");
const welcome = document.querySelector(".welcome");


function addMessage(text, sender) {
  const msg = document.createElement("div");
  msg.classList.add("message", sender);
  msg.innerText = text;

  messages.appendChild(msg);
  scrollToBottom();
}


function scrollToBottom() {
  messages.scrollTop = messages.scrollHeight;
}