from odoo import models, fields

class RecruitmentBotUser(models.Model):
    _name = 'recruitment.bot.user'
    _description = 'User Data for Recruitment Chatbot'


    user_name = fields.Char('Name')
    selected_company = fields.Many2one('res.company', string='Company')
    role = fields.Selection([('intern', 'Intern'), ('professional', 'Professional')], string='Role')
    expertise = fields.Char('Key Skills')
    assessment_score = fields.Float('Assessment Score')
    is_eligible = fields.Boolean('Eligible for Application', default=False)


    def evaluate_eligibility(self, responses):
        total_score = sum(10 for response in responses if response.is_correct)
        self.assessment_score = total_score
        self.is_eligible = total_score >= 70
