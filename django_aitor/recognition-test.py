import boto3

session = boto3.Session(region_name='us-west-2')
rekognition = session.client('rekognition')

with open('./media/pics/Me_2.JPG', 'rb') as image_file:
    image = image_file.read()

response = rekognition.detect_faces(Image = {'Bytes': image}, Attributes = ['ALL'])

filtered_faces = filter(lambda face: face["AgeRange"]["Low"] >= 18, response['FaceDetails'])
filtered_faces = list(map(lambda face: face['BoundingBox'], filtered_faces))
for face in filtered_faces:
  print(face)