const AWS = require('aws-sdk');

const TODO_TABLE = process.env.TODO_TABLE; // Get table name from environment variable
const dynamoDb = new AWS.DynamoDB.DocumentClient();
const uuid = require("uuid");

module.exports.createTodo =  (event, context,callback) => {
    const sResponse=JSON.stringify(event, null, 2)
    console.log("SHOW-PAYLOAD:", sResponse)
    const sResponseJSON= JSON.parse(sResponse);
    console.log("SHOW-PAYLOAD-BODY:", sResponseJSON.body);
    const data = JSON.parse(sResponseJSON.body)
    const timestamp=new Date().getTime();
    //const data = JSON.parse(event.body);
    if (typeof data.todo !== "string"){
      console.error("Validation Failed")
      return;
    }

    const params = {
        TableName: TODO_TABLE,
        Item: {
          userId: uuid.v1(),
          todo: data.todo,
          checked: false,
          createdAt: timestamp,
          updatedAt: timestamp
        }
    }

  dynamoDb.put(params, (error,data) =>{
    if (error) {
        console.error(error);
        callback(new Error(error));
        return;
    }
  })

    //create response
    const response = {
        statusCode: 200,
        body: JSON.stringify(data.Item),
    } 
    callback(null, response)
  }