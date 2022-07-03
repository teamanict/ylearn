async function displayMessages(sender, receiver) {
  var messages = await fetch(`/sendMessage?sender=${sender}&receiver=${receiver}&method=get`)
  messages = await messages.json()
  for (message of messages) {
    if (message.sender == sender) {
      generate_message(message.message, 'self');
    } else if (message.sender == receiver) {
      generate_message(message.message, 'user');
    }
  }
}

async function sendMessage(form) {
  form = document.getElementById('messageInput');

  var sender = form.elements['sender'].value;
  var receiver = form.elements['receiver'].value;
  var message = form.elements['message'].value;
  var data = {
    sender: sender,
    receiver: receiver,
    message: message
  }
  var response = await fetch(`/sendMessage?sender=${sender}&receiver=${receiver}&message=${message}&method=send`)
  console.log(response)

}
var INDEX = 0;
$("#chat-submit").click(function (e) {
  e.preventDefault();
  var msg = $("#chat-input").val();
  if (msg.trim() == '') {
    return false;
  }
  generate_message(msg, 'self');
  var buttons = [
    {
      name: 'Existing User',
      value: 'existing'
    },
    {
      name: 'New User',
      value: 'new'
    }
  ];
  /*setTimeout(function() {      
    generate_message(msg, 'user');  
  }, 1000) */

})

function generate_message(msg, type) {
  INDEX++;
  var str = "";
  str += "<div id='cm-msg-" + INDEX + "' class=\"chat-msg " + type + "\">";
  /* str += "          <span class=\"msg-avatar\">";
  str += "            <img src=\"https:\/\/image.crisp.im\/avatar\/operator\/196af8cc-f6ad-4ef7-afd1-c45d5231387c\/240\/?1483361727745\">";
  str += "          <\/span>"; */
  str += "          <div class=\"cm-msg-text\">";
  str += msg;
  str += "          <\/div>";
  str += "        <\/div>";
  $(".chat-logs").append(str);
  $("#cm-msg-" + INDEX).hide().fadeIn(300);
  if (type == 'self') {
    $("#chat-input").val('');
  }
  $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight }, 1000);
}

function generate_button_message(msg, buttons) {
  /* Buttons should be object array 
    [
      {
        name: 'Existing User',
        value: 'existing'
      },
      {
        name: 'New User',
        value: 'new'
      }
    ]
  */
  INDEX++;
  var btn_obj = buttons.map(function (button) {
    return "              <li class=\"button\"><a href=\"javascript:;\" class=\"btn btn-primary chat-btn\" chat-value=\"" + button.value + "\">" + button.name + "<\/a><\/li>";
  }).join('');
  var str = "";
  str += "<div id='cm-msg-" + INDEX + "' class=\"chat-msg user\">";
  str += "          <span class=\"msg-avatar\">";
  str += "            <img src=\"https:\/\/image.crisp.im\/avatar\/operator\/196af8cc-f6ad-4ef7-afd1-c45d5231387c\/240\/?1483361727745\">";
  str += "          <\/span>";
  str += "          <div class=\"cm-msg-text\">";
  str += msg;
  str += "          <\/div>";
  str += "          <div class=\"cm-msg-button\">";
  str += "            <ul>";
  str += btn_obj;
  str += "            <\/ul>";
  str += "          <\/div>";
  str += "        <\/div>";
  $(".chat-logs").append(str);
  $("#cm-msg-" + INDEX).hide().fadeIn(300);
  $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight }, 1000);
  $("#chat-input").attr("disabled", true);
}

$(document).delegate(".chat-btn", "click", function () {
  var value = $(this).attr("chat-value");
  var name = $(this).html();
  $("#chat-input").attr("disabled", false);
  generate_message(name, 'self');
})

$("#chat-circle").click(function () {
  $("#chat-circle").toggle('scale');
  $(".chat-box").toggle('scale');
})

$(".chat-box-toggle").click(function () {
  $("#chat-circle").toggle('scale');
  $(".chat-box").toggle('scale');
})

	$(document).ready(function(){
		$("#myModal").modal('show');
	});