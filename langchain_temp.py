import os
from api_key import gemini_key
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=gemini_key)




def gen_rap_name_and_lyrics(city):
        promt_name = PromptTemplate(
        input_variables= ['city'],
        template= "Write me a one stage name for a rapper based from -{city}. "
        )
        rap_name =  LLMChain(llm=llm, prompt=promt_name, output_key='rap_name')

        promt_lyrics = PromptTemplate(
        input_variables= ['rap_name'],
        template= "Generate lyrics for a rap song inculding an opening tag line from {rap_name}. "
        )

        rap_lyrics = LLMChain(llm=llm, prompt=promt_lyrics,output_key='lyrics')

        chain = SequentialChain(
            chains =[rap_name,rap_lyrics],
            input_variables =['city',],
            output_variables = ['rap_name','lyrics']
        )

        response= chain({"city":city})

        return response

# if __name__ == "__main__":
#         print(gen_rap_name_and_lyrics("Kozhikode"))
