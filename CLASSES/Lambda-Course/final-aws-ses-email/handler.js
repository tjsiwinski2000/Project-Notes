"use strict";
const AWS = require("aws-sdk");
//instantiation of send e-mail
const ses = new AWS.SES({ region: 'us-east-1' });

module.exports.createContact = async (event, context) => {
  console.log("Received:::", event);
  const sResponse=JSON.stringify(event, null, 2)
  console.log("SHOW-PAYLOAD:", sResponse)
  const sResponseJSON= JSON.parse(sResponse);
  console.log("SHOW-PAYLOAD-BODY:", sResponseJSON.body);
  const data = JSON.parse(sResponseJSON.body)
  console.log("SHOW-PARSED-PAYLOAD" ,data.to ,data.from, data.subject, data.message )

  //"destruct" the event body; creating to/from/subject/message variables
  //const { to, from, subject, message } = JSON.parse(event.body);
  const { to, from, subject, message } = data;

  // if to/from/subject/message monked up=> end pre-maturerly
  if (!to || !from || !subject || !message) {
    return {
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Methods": "*",
        "Access-Control-Allow-Origin": "*",
      },
      statusCode: 400,
      body: JSON.stringify({ message: " to or from... are not set properly!" }),
    };
  }

  // this is the structrue we need to send msgs with SES
  const params = {
    Destination: {
      ToAddresses: [to]
    },
    Message:{
      Body: {
        Text: { Data: message }
      },
      Subject: { Data: subject},

    },
    Source: from
  }

  // try catch because things go wrong 
  try {
    //promise => 'we expect something back'
    await ses.sendEmail(params).promise();
    return {
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Methods": "*",
        "Access-Control-Allow-Origin": "*",
      },
      statusCode: 200,
      body: JSON.stringify({
        message: "email sent successfully!",
        success: true,
      }),
    };
  } catch (error) {
    console.error(error);
    return {
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Methods": "*",
        "Access-Control-Allow-Origin": "*",
      },
      statusCode: 400,
      body: JSON.stringify({
        message: "The email failed to send",
        success: true,
      }),
    };
  }

}
