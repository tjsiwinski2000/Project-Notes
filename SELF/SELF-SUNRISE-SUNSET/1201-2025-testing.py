import json
s={
  "statusCode": 200,
  "body": "{\"data\": {\"response_code\": 0, \"results\": [{\"type\": \"boolean\", \"difficulty\": \"medium\", \"category\": \"Sports\", \"question\": \"Formula E is an auto racing series that uses hybrid electric race cars.\", \"correct_answer\": \"False\", \"incorrect_answers\": [\"True\"]}, {\"type\": \"boolean\", \"difficulty\": \"easy\", \"category\": \"Sports\", \"question\": \"Roger Federer is a famous soccer player.\", \"correct_answer\": \"False\", \"incorrect_answers\": [\"True\"]}, {\"type\": \"boolean\", \"difficulty\": \"medium\", \"category\": \"Sports\", \"question\": \"Skateboarding was included in the 2020 Summer Olympics in Tokyo.\", \"correct_answer\": \"True\", \"incorrect_answers\": [\"False\"]}, {\"type\": \"boolean\", \"difficulty\": \"medium\", \"category\": \"Sports\", \"question\": \"The Olympics tennis court is a giant green screen.\", \"correct_answer\": \"True\", \"incorrect_answers\": [\"False\"]}, {\"type\": \"boolean\", \"difficulty\": \"easy\", \"category\": \"Sports\", \"question\": \"Peyton Manning retired after winning Super Bowl XLIX.\", \"correct_answer\": \"False\", \"incorrect_answers\": [\"True\"]}, {\"type\": \"boolean\", \"difficulty\": \"medium\", \"category\": \"Sports\", \"question\": \"Soccer player Cristiano Ronaldo opened a museum dedicated to himself.\", \"correct_answer\": \"True\", \"incorrect_answers\": [\"False\"]}, {\"type\": \"boolean\", \"difficulty\": \"medium\", \"category\": \"Sports\", \"question\": \"Wilt Chamberlain scored his infamous 100-point-game against the New York Knicks in 1962.\", \"correct_answer\": \"True\", \"incorrect_answers\": [\"False\"]}, {\"type\": \"boolean\", \"difficulty\": \"easy\", \"category\": \"Sports\", \"question\": \"There are a total of 20 races in Formula One 2016 season.\", \"correct_answer\": \"False\", \"incorrect_answers\": [\"True\"]}, {\"type\": \"boolean\", \"difficulty\": \"easy\", \"category\": \"Sports\", \"question\": \"In Rugby League, performing a &quot;40-20&quot; is punished by a free kick for the opposing team.\", \"correct_answer\": \"False\", \"incorrect_answers\": [\"True\"]}, {\"type\": \"boolean\", \"difficulty\": \"easy\", \"category\": \"Sports\", \"question\": \"Shaquille O&rsquo;Neal has only made one three pointer in his career.\", \"correct_answer\": \"True\", \"incorrect_answers\": [\"False\"]}]}}"
}

data = s.json()

print(data)

# for key in s.keys():
#     print(key)

# t=s["body"]
# t= dict(t)
print(type(t))
print(t)