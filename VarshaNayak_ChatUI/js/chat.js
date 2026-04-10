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


function showTyping() {
  typing.classList.remove("d-none");
}

function hideTyping() {
  typing.classList.add("d-none");
}


const responses = [
  "That's interesting!",
  "Tell me more 🙂",
  "I can help with that!",
  "Let's break it down step by step.",
  "Great question!"
];

function getAIResponse() {
  return responses[Math.floor(Math.random() * responses.length)];
}