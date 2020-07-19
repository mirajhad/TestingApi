const Twilio = require("twilio");
const { error } = require("console");

const client = new Twilio("AC614ab027351d5f6423512366e0eeae37", "152c9e03f06d6b322dc3595d5fe6a00e");

client.messages
    .list()
    .then(messages =>
        console.log(`the most recent message is ${messages[0].body}`)
    ).catch(err => console.log(err));

console.log('gathering your message log');