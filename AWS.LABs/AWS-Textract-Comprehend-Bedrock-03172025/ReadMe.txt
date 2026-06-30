03-17-2025 AWS Project: Amazon Textract, Comprehend and Bedrock 
EXPLAINED: Hands-On Tutorial for Beginners

https://www.youtube.com/watch?v=3pc4SNOl8Ho

03-17-2025, finished 03-21-2025
- made progress
- got zzz , deleted NB and will redo tomorrow

(/) Bedrock, Model access, Claude 3.5 Haiku 
() SageMaker, do AI Version, create NoteBook
- while NB creation -> IAM; roles  (search SageMaker) 
- - - Add Policies [Textract.FullAccess ; Comprehend.FullAccess; Bedrock.FullAccess]

- created jpynb notebook, add image [STEVE JOBS QUOTE] same folder CLICK [>]

==KEY CONCEPTS==
def extract_text_from_image(image_path):
    """Extract text from the image using Amazon Textract."""
    client = boto3.client('textract')

boto     - python SDK   
Textract   - extracts text, it doesn't try to make sense of it
Comprehend - make sens of text, key words , sentiment
Bedrock    - extract text and find meaning 
SageMkae   - Jupyter notebook to write/run code
    




MISC Notes

