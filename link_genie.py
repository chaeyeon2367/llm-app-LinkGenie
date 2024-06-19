from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

from third_parties.linkedin import scrape_linkedin_profile

load_dotenv()

if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain!")

    # linkedin_profile_url = linkedin_lookup_agent(name="Chaeyeon Shim")

    summary_template = """
    given the information {information} about a person I want you to create :
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/chaeyeonshim0930/", mock=True
    )

    res = chain.invoke(input={"information": linkedin_data})

    print(res)

