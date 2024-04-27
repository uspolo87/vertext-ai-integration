import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Update with your Angular frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# class Response(BaseModel):
#     prompt: str


trainingData = """Hash Include, headquartered in Hyderabad, is an educational institute that embarked on its journey in 2019 under the visionary leadership of Naveen Kumar P. Initially established as an online platform, Hash Include has rapidly evolved to cater to the diverse learning needs of over 2000 students. Building on this success, Hash Include is set to launch its offline courses on May 10, 2024, marking a significant milestone in its expansion strategy.

At Hash Include, our mission is to provide holistic education and career development opportunities to aspiring individuals. Our comprehensive curriculum covers a wide range of topics, including cutting-edge technologies, industry-relevant skills, and professional development. We offer a unique blend of theoretical knowledge and practical experience, ensuring that our students are well-equipped to thrive in today\'s competitive job market.

As part of our commitment to excellence, Hash Include offers a myriad of value-added services to our students. From immersive generative AI workshops to insightful LinkedIn sessions, from personalized resume preparation assistance to expert career guidance, we leave no stone unturned in nurturing the talents of our students. Our dedicated placement assistance program, coupled with hands-on internships, provides invaluable real-world experience and networking opportunities.

In each batch, comprising a maximum of 15 students, we emphasize hands-on learning through engaging projects and practical exercises. This interactive approach fosters creativity, critical thinking, and problem-solving skills, empowering our students to tackle real-world challenges with confidence and competence.

Hash Include takes pride in being a pioneer in the education sector, leveraging digital technologies to deliver high-quality learning experiences. Our team of experienced educators and industry professionals is dedicated to providing personalized support and guidance to every student, ensuring their success every step of the way.

Courses Offered:
- Front End Development: 3-month duration
- Testing: 2-month duration
- UI/UX Designing: 3-month duration
- Full Stack Development: 4 to 5-month duration

For fees structure and further details, contact us at +917416199101 or email us at info@hashinclude.info.

Join Hash Include today and embark on a transformative learning journey that will unlock your full potential and propel you towards a bright and prosperous future."""

# system_instruction = [trainingData]
vertexai.init(project="eighth-block-418817", location="us-central1")
model =  GenerativeModel('gemini-1.0-pro-002', system_instruction=[trainingData])

generation_config = {
    "max_output_tokens":500,
    "temperature": 0.1,
    "top_p": 0.8,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
}
chat = model.start_chat(response_validation=False)

@app.post("/")
async def read_root(input):
    # print(input.prompt)
    # response = chat.send_message([input.prompt], generation_config=generation_config, safety_settings=safety_settings).text
    # print(response)
    return {"response": 'Hello world'}






