from odoo import http
from odoo.http import request
import openai

openai.api_key = 'I share my api key in the mail'

class RecruitmentChatbot(http.Controller):

    @http.route('/recruitment/chatbot', auth='public', methods=['POST'], type='json')
    def chatbot_interaction(self, company, role, skills):
      
        chatbot_prompt = (
            f"Given the company '{company}', role '{role}', and skills '{skills}', "
            "generate 10 relevant questions for a recruitment process."
        )

        chat_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=chatbot_prompt,
            max_tokens=200
        )

        questions = chat_response.choices[0].text.strip().split('\n')
        return {'questions': questions}
