const Twilio = require("twilio");
const { error } = require("console");

const client = new Twilio("SID", "TOKEN ");

client.messages
    .list()
    .then(messages =>
        console.log(`the most recent message is ${messages[0].body}`)
    ).catch(err => console.log(err));

console.log('gathering your message log');
