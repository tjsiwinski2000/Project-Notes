const AWS = require('aws-sdk');
const TODO_TABLE = process.env.TODO_TABLE; // Get table name from environment variable
const dynamoDb = new AWS.DynamoDB.DocumentClient();

module.exports.updateTodo=(event,context,callback) => {
  const datetime=new Date().toISOString();
  //line below provide by instructor [causes: Unexpected token u in JSON at position 0]
  //const data=JSON.parse(event.body);

  //5lines  TJS
  const sResponse=JSON.stringify(event, null, 2)
  console.log("SHOW-PAYLOAD:", sResponse)
  const sResponseJSON= JSON.parse(sResponse);
  console.log("SHOW-PAYLOAD-BODY:", sResponseJSON.body);
  const data = JSON.parse(sResponseJSON.body)
  console.log("SHOW-PARSED-PAYLOAD" ,data.todo ,data.checked)
  console.log("event.pathParameters.id:",event.pathParameters.id)
  
  if (typeof data.todo !== "string"
  || typeof data.checked !== "boolean") {
        console.error("Value of todo or done is invalid")
        return;
    }

  const params = {
    TableName: TODO_TABLE,
    Key : {
      userId: event.pathParameters.id
    },
    ExpressionAttributeNames: {
      "#todo_text" : "todo"
    },
    ExpressionAttributeValues: {
      ":todo" : data.todo,
      ":checked" : data.checked,
      ":updatedAt" : datetime
    },
    UpdateExpression:
        "SET #todo_text = :todo, checked = :checked, updatedAt = :updatedAt",
    ReturnValues: "ALL_NEW"
  };
    dynamoDb.update(params, (error,data) => {
          if (error) {
            console.error(error);
            callback(new Error(error));
            return;
          }
          const response ={
            statusCode: 200,
            body: JSON.stringify(data.Attributes)
          }
          callback(null, response)
    });
};

